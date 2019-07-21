#TODO
# Multi Procesai
# Async ???
# Pratestuoti race condition
# unittestai su start/stop ???
#https://ruslanspivak.com/lsbaws-part3/
#https://docs.python.org/3/howto/sockets.html
#https://realpython.com/python-concurrency/
#https://realpython.com/intro-to-python-threading/
#Async https://stackoverflow.com/questions/49005651/how-does-asyncio-actually-work/51116910#51116910
#https://docs.python.org/3/library/threading.html
#https://docs.python.org/3/howto/sockets.html
#https://docs.python.org/3/library/multiprocessing.html

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
    #Persiuncia va tiek byt'u informacijos
    request = client_connection.recv(1024)
    print(request)

    #now do something with the clientsocket
    #in this case, we'll pretend this is a threaded server
    #ct = client_thread(clientsocket)
    #ct.run()

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response.encode())
    #ir dar butinai reikia uzdaryti
    client_connection.close()

    