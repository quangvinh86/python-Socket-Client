import socket
# Create a socket object
s = socket.socket()
# Get local machine name
host = socket.gethostname()
# Reserve a port for your service.
port = 1312
# Bind to the port
s.bind((host, port))
# Now wait for client connection.
s.listen(5)
print('start listen client connection...')
# stop when count == 2
count = 0
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    print("Send response to client")
    c.send('Thank {} for connecting'.format(':'.join([str(item) for item in addr])))
    # Close the connectionne
    c.close()
    count += 1
    if count == 2:
        break
s.close()