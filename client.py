import json
import socket
from time import sleep


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.4.63"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            msg = self.client.recv(2048).decode()
            print(msg)
            return msg
        except socket.error as e:
            print(e)

client = Network()
client.connect()
player_status = {"Gabriel": "Really Cool"}
while True:
    sleep(1)
    client.send(json.dumps(player_status))