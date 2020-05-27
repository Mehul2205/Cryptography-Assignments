import socket
s = socket.socket()
port = 4563
s.bind(('', port))
print('Socket bound')
s.listen()
print('Socket Listening')
while True:
	c, addr = s.accept()
	print('Connected to : ', addr)
	c.send('Hello, this is server.'.encode())
	c.close()

