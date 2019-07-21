# lsof -i :8080 #list of open files
# sudo strace -p 12345
# netstat -an |grep 8080
# https://softwareengineering.stackexchange.com/questions/196105/testing-multi-threaded-race-conditions
# https://docs.python.org/3/library/threading.html#event-objects


import socket
import threading
import logging
import queue
import race_condition
import signal


class Server:

    inst = (race_condition.RaceCondition1(), race_condition.RaceCondition2())

    # que      - eile rezultatams
    # e        - eventas, kada galima siusti rezultatus - laukia kol bus pasibaige visi threadai
    #            (isskyrus main ir pacio send que). Pasileidzia is check_thread_stop
    # e1       - eventas, kuris patikrina ar tikrai gautas stop signalas, nes kartais nespeja uzsideti stop,
    #            pasileidzia, kai uzdedamas stop is send_que, arba is testavimo thread'o
    # t_number - paleistu threadu skaicius
    # lock     - skaiciuoti kiek threadu pasibaige
    # t_done   - kiek threadu pasibaige
    # stop     - gautas stop signalas

    def __init__(self):

        self.que = queue.Queue()
        self.e = threading.Event()
        self.e1 = threading.Event()
        self.t_number = 0
        self.lock = threading.Lock()
        self.t_done = 0
        self.stop = False
        self.test3_cache = {}

    @staticmethod
    def create_socket():
        host = 'localhost'
        port = 8080
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((host, port))
        # max value - sysctl -a | grep net.core.somaxconn
        listen_socket.listen(128)
        print('Serving on port %s ...' % port)
        return listen_socket

    # checks if all active threads stoped, if true changes event flag
    def check_thread_stop(self):

        # pirma reikia palaukti ar tikrai stop uzsidejo
        self.e1.wait()
        if self.stop and (self.t_number - self.t_done) <= 2:
            self.e.set()

    def send_queue(self, client_socket, t_number):

        logging.info("Thread from send_queue %d: starting", t_number)

        self.stop = True
        self.e1.set()
        self.check_thread_stop()

        # palaukia, kol visi thread'ai pasibaigia

        self.e.wait()

        logging.info("Thread from send_queue %d: unfreez", t_number)

        # return queue

        que_list = list(self.que.queue)
        msg_to_send = ",".join("(%s,%s)" % tup for tup in que_list)

        client_socket.sendall(msg_to_send.encode(encoding='utf-8', errors='strict'))
        logging.info("Thread %d: stoped from send_queue", t_number)

        # reset all values

        self.__init__()
        client_socket.close()

    def handle(self, client_socket, t_number):
        logging.info("Thread %d: starting", t_number)

        # get msg
        msg = client_socket.recv(1024)

        # check msg
        msg_string = msg.decode()
        if msg_string == "Stop":

            self.send_queue(client_socket, t_number)

        # Calculate test result and add result to queue
        else:
            # cia ne stop, galim realisinti e1 eventa
            self.e1.set()
            logging.info("Thread: %d", t_number)

            if msg_string == "1":
                i = Server.inst[0]
                i.add_remove(20)
                result = i.getbalance()

            if msg_string == "2":
                i = Server.inst[1]
                i.get_instance()
                result = (i.instance_made() - 2) # du turi buti, vienas nuo testo, kitas is threadu

            if msg_string == "3":

                result = race_condition.RaceCondition3.is_number(self.test3_cache, 1)
                print("result", result)
                print("cache", self.test3_cache)

            self.que.put((t_number, result))
            logging.info("Thread %d: stoped, result %d", t_number, result)
            with self.lock:
                self.t_done += 1

            # dar patikrinam ar cia paskutinis neivykdytas threadas
            self.check_thread_stop()
            logging.info("Que result from thread %d, %s", t_number, list(self.que.queue))

    def signal_handle(signal, frame):
        logging.info("Main: stop from signal handler")
        client_socket.close()

    def main(self):

        new_socket = Server.create_socket()

        my_format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=my_format, level=logging.INFO,
                            datefmt="%H:%M:%S")

        while True:
            signal.signal(signal.SIGINT, Server.signal_handle)
            global client_socket
            client_socket, client_address = new_socket.accept()

            try:
                get_request_thread = threading.Thread(target=self.handle, args=(client_socket, self.t_number))
                get_request_thread.start()
                self.t_number += 1
                logging.info("Thread: starting from main %s, %d", get_request_thread, self.t_number)

            except KeyboardInterrupt:
                print("from keyboard")
                logging.info("Main: stop %s", list(self.que.queue))

if __name__ == '__main__':
    c1 = Server()
    c1.main()
