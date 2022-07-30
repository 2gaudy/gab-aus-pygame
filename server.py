import socket
from _thread import *
import sys
import json

server = "192.168.4.63"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

player_status = {}
def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                json_reply =  json.loads(reply)
                print(f"Current player status is {player_status}")
                for key in json_reply:
                    player_status[key] = json_reply[key]
                print("Sending : ", str(player_status))

            conn.sendall(str.encode(str(player_status)))
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))