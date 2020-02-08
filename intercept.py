#!/usr/bin/python3
import socket

IP = "127.0.0.1"
port = 8080

#create socket object
s = socket.socket()          
s.bind(('', port))
print (f"socket binded to {port}")

#set listner
s.listen(5)      
print ("socket is listening")
            
while True: 
  
   c, addr = s.accept()      
   print ('Got connection from', addr) 

   c.close() 


