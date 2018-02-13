import socket
# Create a socket object
s = socket.socket()
# Get local machine name
host = socket.gethostname()
# Reserve a port for your service.
port = 1312

s.connect((host, port))
# print respone from server
print('respone from server: {}'.format(s.recv(1024)))
# Close the socket when done
s.close