#lsof -i :8080 #list of open files
#netstat -an
#sudo strace -p 12345

import socket
import threading
import traceback
import race_condition
import queue
import logging


class Server():

    global que
    que = queue.Queue()

    def create_socket():
        HOST = 'localhost'
        PORT = 8080
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((HOST, PORT))
        listen_socket.listen(1)
        print('Serving on port %s ...' % PORT)
        return listen_socket

    def get_balance1(client_socket, balance, que):
        logging.info("Thread: starting")
        balance.add_remove(20)
        result = balance.getbalance()
        que.put(result)
        logging.info("Thread: stoped, result %d", result)
        while not que.empty():
            print("O", que.get(), end=' ')

    def get_que():
        return que

    def main():

        new_socket = Server.create_socket()

        Balance = race_condition.RaceCondition1()
        result = Balance.getbalance()
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")

        threads = []
        while True:
            client_socket, client_address = new_socket.accept()
            #print("my client socket", client_socket)

            try:
                get_request_thread = threading.Thread(target=Server.get_balance1, args=(client_socket, Balance, que))
                get_request_thread.start()
                print("started thread", get_request_thread)
                threads.append(get_request_thread)
                #Be sito threadai nesibaigia
                for t in threads:
                    t.join()
            except:
                print('Terible error!')
                traceback.print_exc()
        client_socket.close()

if __name__ == '__main__':
    Server.main()
