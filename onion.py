from Crypto import Random 
from Crypto.PublicKey import RSA

class NetworkDevice:
    def __init__(self):
        seed = Random.new().read
        self.key_pair = RSA.generate(2048, seed)
        self.public_key = self.key_pair.publickey()

    def exchange_public_key(self):
        return self.public_key
    
    def decrypt_string(self, ciphertext):
        if type(ciphertext) is bytes:
            cleartext = self.key_pair.decrypt(ciphertext)
        else:
            cleartext = self.key_pair.decrypt(ciphertext).decode(encoding='UTF-8')
        return cleartext

    def encrypt_string(self, string, public_key):
        if type(string) is str:
            enc_data = public_key.encrypt(string.encode(),48)
        else:
            enc_data = public_key.encrypt(string, 48)
        return enc_data[0]


if __name__ == "__main__":
    # Alice wants to learn some cool hacks from a website
    alice = NetworkDevice()
    dest_ip_addr = '1.3.3.7'

    # she decides to use Tor, and chooses an entry node
    entry_node = NetworkDevice()
    
    # she gets in contact with the entry node and exchanges public keys
    entry_node_public_key = entry_node.exchange_public_key()

    # now she picks some tor nodes to route through
    tor_node1 = NetworkDevice()
    tor_node1_public_key = tor_node1.exchange_public_key()
    tor_node2 = NetworkDevice()
    tor_node2_public_key = tor_node2.exchange_public_key()

    # now she picks an exit node
    exit_node = NetworkDevice()
    exit_node_public_key = exit_node.exchange_public_key()

    # Alice encrypts her dest ip with the last session key (the exit node's)
    encrypted_message = alice.encrypt_string(dest_ip_addr, exit_node_public_key)
    #encrypted_message += 'goto node2'
    # and puts on the other layers of encryption...
    message_to_node2 = alice.encrypt_string(encrypted_message, tor_node2_public_key)
    message_to_node1 = alice.encrypt_string(message_to_node2, tor_node1_public_key)
    message_to_entry_node = alice.encrypt_string(message_to_node1, entry_node_public_key)
    
    # Alice sends the message to the entry node
    
    # the entry node recieves the message and decrypts it to discover its contents...
    decrypted1 = entry_node.decrypt_string(message_to_entry_node)
    # this message is still encrypted and will only reveal the ip of the next hop
    print('decrypted message: ', decrypted1)
    # the entry node sends the message to the next hop, who decrypts and sends to the next
    decrypted2 = tor_node1.decrypt_string(decrypted1)
    # removing each layer like the layers of an onion... omg the name makes sense!
    decrypted3 = tor_node2.decrypt_string(decrypted2)
    # the exit node peels off the last layer of the onion
    decrypted_message = exit_node.decrypt_string(decrypted3)
    print('decrypted message: ', decrypted_message)
