import socket
s = socket.socket()
port = 4563
s.connect(('127.0.0.1', port))
print('The following message was received from the server : \n', s.recv(1024))
print('Closing connection..')
s.close()
