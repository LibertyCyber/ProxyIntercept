#!/usr/bin/env python3
import socket

class proxscan:
    
    def __init__(self,port):
        self.port = port
        self.s = socket.socket() 
        self.rdata = None

    def listen(self):
        self.s.bind(('', self.port))
        self.s.listen(999)
        (c, addr) = self.s.accept()
        rec = (c.recv(1024))
        info = {"header": rec, "addr": addr}

        self.rdata = rec
        
        return info

    