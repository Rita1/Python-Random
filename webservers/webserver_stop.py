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
    def send_queue(self, client_socket, t_number):

        # return queue

        que_list = list(self.que.queue)
        msg_to_send = ' '.join(map(str, que_list))
        client_socket.sendall(msg_to_send.encode(encoding='utf-8', errors='strict'))

        # Signal to stop server
        self.stop = True
        print("T_number, self.stop", t_number, self.stop)
        logging.info("Thread %d: stoped from send_queue", t_number)
        client_socket.close()

    def handle(self, balance, t_number):


        logging.info("Thread %d: starting", t_number)
        # waith for request, block server
        client_socket, client_address = new_socket.accept()
        # get msg
        msg = client_socket.recv(1024)

        # check for Stop
        msg_string = msg.decode()

        if msg_string == "Stop":
            self.send_queue(client_socket, t_number)

        # Calculate balance and add result to queue
        else:
            logging.info("Thread: %d", t_number)
            balance.add_remove(20)

            result = balance.getbalance()
            self.que.put(result)
            logging.info("Thread %d: stoped, result %d", t_number, result)
            logging.info("Que result from thread %d, %s", t_number, list(self.que.queue))

    def main(self):

        new_socket = Server.create_socket()
        Balance = race_condition.RaceCondition1()

        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")

        threads = []
        t_number = 0
        while True:

            print("1", self.stop)

            try:
                # 1 block until request arrives

                get_request_thread = threading.Thread(target=self.handle, args=(t_number, ))
                get_request_thread.start()
                t_number += 1
                print("2")
                # 2 check if needs break
                # 3 compute answer

                logging.info("Thread: starting from main %s, %d", get_request_thread, t_number)
                threads.append(get_request_thread)

                print("3", self.stop)
                if self.stop:
                    print("4")
                    logging.info("Main: server stoping from main, result from que %s", list(self.que.queue))
                    client_socket.close()
                    for t in threads:
                        t.join()
                    break
            except KeyboardInterrupt:
                    logging.info("Main: stop %s", list(self.que.queue))
                    self.send_queue(client_socket)

if __name__ == '__main__':
    c1 = Server()
    c1.main()
