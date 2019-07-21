import socket

# create a socket and connect to a server


#f = open("avengers.txt", "r", encoding="utf-8")
# for line in f:
#         print("line", line)
#         #print("f", f)
#         #Send only bytes
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect(('localhost', 8080))
#         bytes_line = line.encode(encoding='utf-8', errors='strict')
#         sock.send(bytes_line)
#         #Get back
#         data = sock.recvmsg(1024)
#         print(data)
#
#         sock.close()
# listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)listen_socket.bind((HOST, PORT))        # send data

#2V
#############################################
message = "KnockKnock"

count_client = 0

while True:
    #Connect to socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8080))

    #Encode msg to bytes
    msg = message + " " + str (count_client)
    msg_bytes_to_send = msg.encode(encoding='utf-8', errors='strict')
    print("before", msg_bytes_to_send)
    #Send
    #bytes_send = sock.send(msg_bytes_to_send) TODO naudoti sendall
    sock.send(msg_bytes_to_send)
    #Get back
    msg_bytes_get = sock.recv(1024)
    print("got msg", msg_bytes_get)
    count_client += 1
    #Close socket
    sock.close()