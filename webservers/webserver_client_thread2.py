import socket
import logging
import concurrent.futures

class Client():

    def get_receive_msg(name):
        count = 0
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 8080))
            logging.info("Thread %s: starting", name)
            # Encode msg to bytes
            message = "Thread name " + str(name) + "count " + str(count)
            msg_bytes_to_send = message.encode(encoding='utf-8', errors='strict')
            print("before", msg_bytes_to_send)
            sock.sendall(msg_bytes_to_send)
            msg_bytes_get = sock.recv(1024)
            print("got msg", msg_bytes_get)
            count += 1
            sock.close()
            logging.info("Thread %s: stoping", name)

    @staticmethod
    def main():
        clients_numb = 500         #As many threads
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        #nemeto klaidu !
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(Client.get_receive_msg, range(clients_numb))


if __name__ == '__main__':
    Client.main()