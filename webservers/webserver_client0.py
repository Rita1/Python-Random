import socket

# create a socket and connect to a server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))
message = 'test'
# send and receive some data
sock.sendall(message.encode())
data = sock.recv(1024)
print(data.decode())