import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

message = 'hello, world!'
sock.send(message.encode())

data = sock.recv(1024)
sock.close()

print(data.decode())