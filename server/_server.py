import queue
import socket
from threading import Thread

from queue import Queue


def clientSendData(client:socket.socket, qDict, address):
    q = qDict[address]

    while True:
        data = q.get()
        try:
            client.send(bytes(data, "utf-8"))
        except:
            pass

def clientHandler(client:socket.socket, address, qDict):
    print(f"Connection Established - {address}")
    q = qDict[address]
    thread = Thread(target=clientSendData, args=(client, qDict, address))
    thread.start()
    while True:
        string = client.recv(1024)
        if not string: break
        string = string.decode("utf-8")
        for i in qDict:
            if i == address:
                continue
            else:
               qDict[i].put(string)
    print("Client Disconnected")

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234
    connection_list = []
    q = Queue()
    qDict = {}

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        address = f"{address[0]}:{address[1]}"
        qDict[address] = Queue()

        thread = Thread(target=clientHandler, args = (client, address, qDict))
        thread.start()


