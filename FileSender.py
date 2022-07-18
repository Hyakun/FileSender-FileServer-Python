# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:27:22 2021

@author: xdany
"""

import socket
import tqdm
import os
import argparse

SEPARATOR = "?"
BUFFER_SIZE = 1024 * 4

def send_file(filename, host, port):
    filesize = os.path.getsize(filename)
    
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    
    progress = tqdm.tqdm(range(filesize),f"Sending {filename}", unit="8", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            
            
            s.sendall(bytes_read)
            progress.update(len(bytes_read))
    s.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Sender")
    parser.add_argument("file", help="File name to send")
    parser.add_argument("host", help="The host/IP address of the reciver")
    parser.add_argument("-p","--port", help="Port to use default is 5001", default = 5001)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    send_file(filename, host, port)
    
    
    
    
    
    
    
    
    
    
    

            