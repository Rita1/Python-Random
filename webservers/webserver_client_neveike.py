import socket

# create a socket and connect to a server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

f = open("avengers.txt", "r", encoding="utf-8")

for line in f:
        print("line", line)
        #print("f", f)
        #Send only bytes
        bytes_line = line.encode(encoding='utf-8', errors='strict')
        sock.send(bytes_line)
        #???
        # send data
        #Get back
        #data = sock.recvmsg(1024)
        #print(data)

