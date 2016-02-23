from socket import socket
from time import sleep

s = socket()
s.connect(('games.cnsuva.io',33333))
print '** server says: ', s.recv(100)
highest = 10000
lowest = 1
guess = 5000
guesses = 0
s.send('5000')
print 'trying: ', guess
response = str(s.recv(100))
print '** server says: ', response
while True:
    if response[4] == 'g':
        print 'Total guesses: ', guesses
        break
    elif response[4] == 'l':
        lowest = guess
        guess = int((highest + lowest)/2)
    elif response[4] == 'h':
        highest = guess
        guess = int((highest + lowest)/2)
    s.send(str(guess))
    sleep(0.2)
    print 'trying: ', guess
    response = str(s.recv(100))
    print '** server says: ', response
    guesses += 1
