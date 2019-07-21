import socket
from multiprocessing import Process
import logging
import os

class Client():

    def get_receive_msg(name):
        count = 0
        logging.info("Proc %s, %d: starting", name, os.getpid())
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 8080))
            # Encode msg to bytes
            message = "Proc name " + str(name) + "count " + str(count)
            msg_bytes_to_send = message.encode(encoding='utf-8', errors='strict')
            #print("before", msg_bytes_to_send)
            sock.sendall(msg_bytes_to_send)
            msg_bytes_get = sock.recv(1024)
            #print("got msg", msg_bytes_get)
            count += 1
            sock.close()
        logging.info("Proc %s, %d: stoping", name, os.getpid())

    @staticmethod
    def main():

        clients_numb = 5         #As many threads
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        logging.info("Main    : parent process pid %d.", os.getppid())
        proc = []
        for i in range(clients_numb):
            logging.info("Main    : create and start proc %d.", i)
            x = Process(target=Client.get_receive_msg, args=(i,))
            proc.append(x)
            x.start()

        print(proc)
        for i, p in enumerate(proc):
            logging.info("Main    : before joining proc %d.", i)
            p.join()
            logging.info("Main    : proc %d done", i)

if __name__ == '__main__':
    Client.main()