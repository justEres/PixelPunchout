import socket
from time import sleep
from threading import Thread


def recv(server: socket.socket):
    while True:
        buffer = server.recv(1024)
        buffer = buffer.decode("utf-8")
        print(buffer)


if __name__ == "__main__":
    #name = input("dein name:")
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    thread = Thread(target=recv, args=(server,))
    thread.start()

    '''while True:
        string = name + ": " + input("")
        # string = "haskklfj"
        # sleep(20)
        server.send(bytes(f"Theo: {string}", 'utf-8'))'''

    ##husten
