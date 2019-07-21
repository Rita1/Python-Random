# lsof -i :8080 #list of open files
# sudo strace -p 12345
# netstat -an |grep 8080
# https://softwareengineering.stackexchange.com/questions/196105/testing-multi-threaded-race-conditions

import socket
import threading
import logging
import queue
import race_condition


class Server:

    def __init__(self):
        self.que = queue.Queue()
        self.stop = False

    stop = False

    @staticmethod
    def create_socket():
        HOST = 'localhost'
        PORT = 8080
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((HOST, PORT))
        # max value - sysctl -a | grep net.core.somaxconn
        listen_socket.listen(128)
        print('Serving on port %s ...' % PORT)
        return listen_socket

    # Return queue and stop server
    def send_queue(self, client_socket):

        # return queue

        que_list = list(self.que.queue)
        msg_to_send = ' '.join(map(str, que_list))
        client_socket.sendall(msg_to_send.encode(encoding='utf-8', errors='strict'))

        # Signal to stop server
        self.stop = True
        Server.stop = True
        print("self.stop",self.stop)
        logging.info("Thread: stoped from send_queue")
        client_socket.close()

    def handle(self, client_socket, balance):
        logging.info("Thread: starting")

        # get msg
        msg = client_socket.recv(1024)

        # check for Stop
        msg_string = msg.decode()

        if msg_string == "Stop":
            self.send_queue(client_socket)

        # Calculate balance and add result to queue
        else:
            logging.info("Thread: HY")
            balance.add_remove(20)

            result = balance.getbalance()
            self.que.put(result)
            logging.info("Thread: stoped, result %d", result)
            logging.info("Que result from thread %s", list(self.que.queue))

    def main(self):

        new_socket = Server.create_socket()
        Balance = race_condition.RaceCondition1()

        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")

        threads = []
        print("Server.stop1", Server.stop)
        client_socket, client_address = new_socket.accept()
        while not Server.stop:
            print("Server.stop2", Server.stop)

            print("1")
            try:
                get_request_thread = threading.Thread(target=self.handle, args=(client_socket, Balance,))
                get_request_thread.start()
                logging.info("Thread: starting from main %s", get_request_thread)
                threads.append(get_request_thread)
                # Be sito threadai nesibaigia
                print("2")
                if self.stop:
                    print("Stop")
                    logging.info("Main: server stoping from main, result from que %s", list(self.que.queue))
                    client_socket.close()
                    #for t in threads:
                    #    t.join()
                    break

            except KeyboardInterrupt:
                    logging.info("Main: stop from Keybord %s", list(self.que.queue))
                    self.send_queue(client_socket)
            print("3")
        print("5")
        for t in threads:
            print("4")
            t.join()
        logging.info("Main: stop %s", list(self.que.queue))
        client_socket.close()

if __name__ == '__main__':
    c1 = Server()
    c1.main()
