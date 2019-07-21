import socket
import threading
import logging
from time import sleep
import random
import io
import unittest
import webserver_que

class Client:

    def __init__(self):

        # Thread-local data are data whose values are thread specific.
        # To manage thread-local data, just create an instance of local (or a subclass) and store attributes on it:

        self.thread_local = threading.local()


    def create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 4444))
        self.thread_local = sock
        return self.thread_local

    # Send msg stop
    def get_msg(self):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 4444))

        # Send stop
        message = "Stop"
        msg_bytes_to_send = message.encode(encoding='utf-8', errors='strict')
        sock.sendall(msg_bytes_to_send)

        # Get answer
        buffer = io.BytesIO()
        # TODO pasiziureti ar tikrai viska persiuncia
        while True:
            msg_bytes_get = sock.recv(1024)
            buffer.write(msg_bytes_get)
            if msg_bytes_get == b'':
                break
        result = buffer.getvalue()
        buffer.close()
        sock.close()
        return result.decode()

    # name - thread name
    # test nmb - test number send to server

    def send_msg(self, name, test_nmb):

        with self.create_socket() as sock:
            logging.info("Thread %s: starting", name)
            str_test_nmb = str(test_nmb)
            bytes_test_nmb = str_test_nmb.encode(encoding='utf-8', errors='strict')
            sock.sendall(bytes_test_nmb)
            sock.close()
            logging.info("Thread %s: stoping", name)

    # return only non zero
    def check_result(self, result):

        result_list = eval("[%s]" % result)
        list_of_err = []
        for i in result_list:
            if i[1] != 0:
                list_of_err.append(i)

        return list_of_err

    # test nmb - which test should test
    #    - 1 - balance
    #    - 2 - instance
    #    clients_numb - how many threads
    # returns results, which has errors

    def main(self, test_nmb, clients_numb):

        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        threads = []
        for i in range(clients_numb):
            try:
                logging.info("Main    : create and start thread %d.", i)
                x = threading.Thread(target=self.send_msg, args=(i, test_nmb))
                threads.append(x)
                x.start()
            except KeyboardInterrupt:
                logging.info("Main    : result after %s", self.get_msg())

        for i, thread in enumerate(threads):
            logging.info("Main    : before joining thread %d.", i)
            thread.join()
            logging.info("Main    : thread %d done", i)

        result = self.get_msg()
        result_err = self.check_result(result)
        logging.info("Main    : result after %s", result_err)
        return result_err


#if __name__ == '__main__':
#    c1 = Client()
#    c1.main(1, 1)

class TestRaceConditions(unittest.TestCase):

    def test_balance(self):

        c1 = Client()
        result = c1.main(1, 50)
        print("Result1", result)
        self.assertTrue(len(result) == 0)

    def test_instance(self):

        c1 = Client()
        result = c1.main(2, 50)
        print("result 2", result)
        self.assertTrue(len(result) == 0)

    def test_instance(self):
        c1 = Client()
        result = c1.main(3, 50)
        print("result 2", result)
        self.assertTrue(len(result) == 0)

if __name__ == '__main__':
    unittest.main()