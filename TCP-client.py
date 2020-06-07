#!/usr/bin/python3.8
#Based on realpython.com/python-sockets/

import socket


#Configure remote host IP and port 
HOST = '127.0.0.1'
PORT = 65432

#Init TCP Socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Connect to remote host on configure IP and port
    s.connect((HOST, PORT))
    #Send data to remote host in socket
    s.sendall(b'Hello World')
    #Receive data from remote host in socket
    data = s.recv(1024)

#Print data from var data to shell
print('Received', repr(data))

