import socket
import queue
from threading import Thread
import json




def executor(package: str):
    package = json.loads(package)
    if package["id"] == "PLAYERPOS":
        args = list(package["args"])
        print(args)
    else:
        print("[DEBUG] unknown package:\n" + json.dumps(package))


def reciever(server: socket.socket):
    while True:
        buffer = server.recv(1024)
        buffer = buffer.decode("utf-8")
        executor(buffer)


def init():
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    thread = Thread(target=reciever, args=(server,))
    thread.start()
    return server
    """
    while True:
        data = ""

        server.send(bytes(data, "utf-8"))
    
    
    """
def packageSender(playerID, type, args, server):
    data = {
        'id': playerID,
        'type': type,
        'args': [args[0], args[1]]
    }
    data = json.dumps(data)

    server.send(bytes(data, "utf-8"))



