# Echo client program
import socket
import sys

HOST = '10.10.104.92'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#socket_data = ' '.join(sys.argv[1:])
print socket_data
s.send("%s %d %s %s %d %s", sys.argv[1:])
data = s.recv(2048)
s.close()

print 'Received', repr(data)
