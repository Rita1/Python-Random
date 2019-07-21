import socket

message = "KnockKnock"

count_client = 0

# Connect to socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))
print("sock", sock)

while True:
    #Encode msg to bytes
    msg = message + " " + str (count_client)
    msg_bytes_to_send = msg.encode(encoding='utf-8', errors='strict')
    print("before", msg_bytes_to_send)
    #Send
    sock.send(msg_bytes_to_send)
    #Get back
    msg_bytes_get = sock.recv(1024)
    print("got msg", msg_bytes_get)
    count_client += 1
#Close socket
sock.close()