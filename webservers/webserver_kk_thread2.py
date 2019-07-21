#lsof -i :8080 #list of open files
#netstat -an

import socket
import threading
import traceback

class Server():

    def create_socket():
        HOST = 'localhost'
        PORT = 8080
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((HOST, PORT))
        # argument to listen tells the socket library
        # that we want it to queue up as many as 5 connect requests (the normal max) before refusing outside connections.
        # If the rest of the code is written properly, that should be plenty.
        listen_socket.listen(1)
        print('Serving on port %s ...' % PORT)
        return listen_socket

    def get_request(client_socket):
        request = client_socket.recv(1024)
        print(request)
        client_socket.sendall(request)

        if request == b'':  # empty bytes
            # ir dar butinai reikia uzdaryti
            print("Bye")
            client_socket.close()
        #Uzdaryti!
        client_socket.close()

    def accept_connection(socket):

        client_socket, client_address = socket.accept()
        print("my client socket", client_socket)
        try:
            get_request_thread = threading.Thread(target=Server.get_request, args=(client_socket,))
            get_request_thread.start()
            print("started thread", get_request_thread)
        except:
            print('Terible error!')
            traceback.print_exc()

    def main():

        #lock = threading.local()
        socket = Server.create_socket()
        # After creating the listener socket, you want to loop around accept, kicking off a new client
        # thread for each accepted connection, right? So, you want to call it in a loop, either inside connection,
        # or at the top level (in which case connection has to return s)
        while True:
            Server.accept_connection(socket)


if __name__ == '__main__':
    Server.main()