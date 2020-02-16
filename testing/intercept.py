#!/usr/bin/python3
import socket
import time

IP = "127.0.0.1"
port = 8080

#create socket object
s = socket.socket()          
s.bind(('', port))
print (f"socket binded to {port}")

#set listner
s.listen(5)      
print ("socket is listening")

 
with open('./response.txt', 'r')as fp:
    resp = fp.read()

resp = resp.encode('utf-8')

while True: 
    c, addr = s.accept()      
    print ('Got a connection')
    rec = (c.recv(1024))
    print(rec.decode('utf-8'))

    time.sleep(999)
    
    c.send(resp)

    c.close() 


