#!/usr/bin/env python3
import socket
import requests
import re
import time

class proxscan:
    
    def __init__(self,port):
        self.port = port
        self.s = socket.socket() 
        self.rdata = None

    def listen(self):
        self.s.bind(('', self.port))
        self.s.listen(999)
        (self.c, self.addr) = self.s.accept()
        rec = (self.c.recv(1024))
        info = {"header": rec, "addr": self.addr}

        self.rdata = rec
        
        return info

    def get_content(self):
        clean = self.rdata.decode('utf-8')
        bytehost = re.findall(r'POST .+? HTTP/', clean)
        host = bytehost[0][5:-6]
        response = requests.post(f" {self.addr[0]}:{self.addr[1]} ", data = host)
        response = response.content
        time.sleep(0.5)

        self.response = response


    def close_listen(self):
        self.c.send(self.response)

    