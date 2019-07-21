import socket

HOST, PORT = '', 8080

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
#argument to listen tells the socket library
#that we want it to queue up as many as 5 connect requests (the normal max) before refusing outside connections.
# If the rest of the code is written properly, that should be plenty.
listen_socket.listen(1)
print('Serving HTTP on port %s ...'%PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    #Atsisiuncia va tiek byt'u informacijos
    request = client_connection.recv(1024)
    print(request)

    #    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    #ct = client_thread(clientsocket)
    #ct.run()

    client_connection.sendall(request)
    #ir dar butinai reikia uzdaryti
    #client_connection.close()