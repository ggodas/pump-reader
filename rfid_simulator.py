#!/usr/bin/env python3

import socket
from time import sleep

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8888       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    count = 0
    with conn:
        print('Connected by', addr)
        while True:
            conn.sendall("Said Hello".encode())
            sleep(10000)
            count += 1
            if count >= 10:
                conn.detach()
                conn.close()
                s.detach()
                s.close()
                break
