import queue
import socket
from threading import Thread
import json
from queue import Queue


def debugpackage():
    data = {
        'id': 'PLAYERPOS',
        'args': [120, 134]
    }
    data = json.dumps(data)
    return data


def clientSendData(client: socket.socket, qDict, address):
    #Diese Funktion sendet dem Client alles was auf seiner eigenen Queue liegt.
    q = qDict[address]

    #client.send(bytes(debugpackage(), "utf-8"))
    while True:

        data = q.get()
        try:
            pass

            client.send(bytes(data, "utf-8"))
        except:

            pass


# Baut die Verbindung mit dem Client auf.
def clientHandler(client: socket.socket, address, qDict):
    print(f"Connection Established - {address}")
    q = qDict[address]

    # Startet für den jeweiligen Client einen Thread zum Senden von Daten.
    # Der seine Addresse und Queue number übermittelt bekommt
    thread = Thread(target=clientSendData, args=(client, qDict, address))
    thread.start()
    while True:

        # Alles was der Client sendet kommt hier an.
        string = client.recv(1024)
        string = string.decode("utf-8")
        if not string: break

        # Die Daten die gesendet werden auf die einzelnen Queues verteilt
        # Die eigene Queue jedoch nicht
        for i in qDict:
            if i == address:
                continue

            else:
                qDict[i].put(string)

    print("Client Disconnected")

# Diese Funktion sendet die SETUP Info's
def sendPlayerSetUpInfo(client:socket.socket, qDict):
    PlayerId = len(qDict)
    setUpInfo = {
        "id": PlayerId,
        "type": "SETUPINFO",
        "args": []
    }
    setUpInfo = json.dumps(setUpInfo)
    client.send(bytes(setUpInfo, "utf-8"))


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234
    connection_list = []
    q = Queue()
    qDict = {}

    # Setzt den Server auf
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        address = f"{address[0]}:{address[1]}"


        qDict[address] = Queue()
        sendPlayerSetUpInfo(client, qDict)

        #Für jeden Client wird ein eigener Handler Thread erstellt.
        thread = Thread(target=clientHandler, args=(client, address, qDict))
        thread.start()


