import json
import socket
from threading import Thread


def executor(package: str,newPlayerFunc,setPlayerPosFunc):
    package = json.loads(package)
    if package["type"] == "PLAYERPOS":
        args = list(package["args"])
        id = package["id"]
        setPlayerPosFunc(id,args)
        print(f"client {id} Position: {args}")
    elif package["type"] == "SETUPINFO":
        id = int(package["id"])
        return id
    elif package["type"] == "NEWPLAYER":
        id = int(package["id"])
        newPlayerFunc(id)

    else:
        print("[DEBUG] unknown package:\n" + json.dumps(package))


def reciever(server: socket.socket,newPlayerFunc,setPlayerPosFunc):
    while True:
        buffer = server.recv(1024)
        buffer = buffer.decode("utf-8")
        executor(buffer,newPlayerFunc,setPlayerPosFunc)


def init(newPlayerFunc,setPlayerPosFunc):
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    ## Connection start handshake
    setupinfo = server.recv(1024)
    setupinfo = setupinfo.decode("utf-8")
    playerid = executor(setupinfo)
    packageSender(playerid,"NEWPLAYER",[],server)


    thread = Thread(target=reciever, args=(server,newPlayerFunc,setPlayerPosFunc))
    thread.start()
    return server

def packageSender(playerID, type, args, server):
    data = {
        'id': playerID,
        'type': type,
        'args': [args[0], args[1]]
    }
    data = json.dumps(data)

    server.send(bytes(data, "utf-8"))



