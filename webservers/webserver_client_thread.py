import socket
import threading
import logging
import time
import webserver_racecondition

class Client:

    def get_receive_msg(name):
        count = 0
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 8080))
        logging.info("Thread %s: starting", name)
        time.sleep(10)
        sock.close()
        logging.info("Thread %s: stoping", name)




    @staticmethod
    def main():
        clients_numb = 50         #As many threads
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        threads = []
        for i in range(clients_numb):
            logging.info("Main    : create and start thread %d.", i)
            x = threading.Thread(target=Client.get_receive_msg, args=(i,))
            threads.append(x)
            x.start()

        print(threads)
        for i, thread in enumerate(threads):
            logging.info("Main    : before joining thread %d.", i)
            thread.join()
            logging.info("Main    : thread %d done", i)

        result = webserver_racecondition.Server.get_que()
        #result = webserver_racecondition.get_que()
        print("empty?", result.empty())
        while not result.empty():
            print("O", result.get(), end=' ')
        logging.info("Main    : result after threads %s", result)

if __name__ == '__main__':
    Client.main()