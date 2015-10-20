from Crypto import Random 
from Crypto.PublicKey import RSA

class NetworkDevice:
    def __init__(self):
        rand_func = Random.new().read
        self.key_pair = RSA.generate(2048, rand_func)
        self.public_key = self.key_pair.publickey()

    def exchange_public_key(self):
        return self.public_key
    
    def decrypt_string(self, ciphertext):
        cleartext = self.key_pair.decrypt(ciphertext)
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
    print('where alice wants to go: ', dest_ip_addr, '\n')

    # she decides to use Tor, and chooses an entry node from the Tor Directory
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
    # and puts on the other layers of encryption...
    message_to_node2 = alice.encrypt_string(encrypted_message, tor_node2_public_key)
    message_to_node1 = alice.encrypt_string(message_to_node2, tor_node1_public_key)
    message_to_entry_node = alice.encrypt_string(message_to_node1, entry_node_public_key)
    
    # Alice sends the message to the entry node
    
    # the entry node recieves the message and decrypts it to discover its contents...
    decrypted1 = entry_node.decrypt_string(message_to_entry_node)
    # this message is still encrypted and will only reveal the ip of the next hop
    print('what entry node sees: ', decrypted1, '\n')
    # the entry node sends the message to the next hop, who decrypts and sends to the next
    decrypted2 = tor_node1.decrypt_string(decrypted1)
    print('what node1 sees: ', decrypted2, '\n')
    # removing each layer like the layers of an onion... omg the name makes sense!
    decrypted3 = tor_node2.decrypt_string(decrypted2)
    print('what node2 sees: ', decrypted3, '\n')
    # the exit node peels off the last layer of the onion
    # it also performs a checksum calculation to make sure the data has not been tampered with 
    decrypted_message = exit_node.decrypt_string(decrypted3)
    print('what exit node sees: ', decrypted_message.decode(encoding='UTF-8'))
