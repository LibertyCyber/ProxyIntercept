#!/usr/bin/env python3
import socket
import time
import requests
from proxy_interceptor import Intercept

port = 1234


while True:
    s = socket.socket()          
    s.bind(('', port))
    s.listen(5)

    (c, addr) = s.accept()
    rec = (c.recv(1024))

    rdata = rec.decode('utf-8')
    currentobj = Intercept(rdata)
    
    print(currentobj)
    
    correct_requ = input("save this to your collection(y/n): ")

    if(correct_requ == "y" or correct_requ == "Y"):
        break
    elif(correct_requ == "n" or correct_requ == "N"):
        print("continuing scan")
        c.send(b"HTTP/1.1 200 OK")
    
