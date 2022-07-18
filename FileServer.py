# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:27:24 2021

@author: xdany
"""

import socket
import tqdm
import os

SERVER_HOST = socket.gethostname()
SERVER_PORT = 5001

BUFFER_SIZE = 4096
SEPARATOR = "?"

s = socket.socket()

s.bind((SERVER_HOST,SERVER_PORT))

s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = s.accept()
print(f"[+] {address} is connected.")

recived = client_socket.recv(BUFFER_SIZE)
print(recived)
filename, filesize = recived.decode().split(SEPARATOR)

print(filename)
filename = os.path.basename(filename)

filesize = int(filesize)
print(filesize)

progress = tqdm.tqdm(range(filesize), f"Reciving {filename}", unit="8", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for _ in progress:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))

client_socket.close()
s.close()





























