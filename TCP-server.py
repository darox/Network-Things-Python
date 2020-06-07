#!/usr/bin/python3.8
#Based on realpython.com/python-sockets/

import socket


#Configure host and port to bind on to
HOST = '127.0.0.1'
PORT = 65432



#Init a TCP socket with family INET and socket kind SOCK_STREAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Bind to the above configured host and port
    s.bind((HOST, PORT))
    #Listen on configured host and port
    s.listen()
    #Assign result from accept method to var conn and addr
    conn, addr = s.accept()
    with conn:
        #Print address of host which connected to local socket
        print('Connected by', addr)
        #Loop to receive the data from the remote host
        while True:
            #Assign result from connect receive method to var data i.e it's the payload what the remote host sends (get 1024 bytes every time)
            data = conn.recv(1024)
            if not data:
                #break loop if no data was received
                break
            #Send back payload which was received back to remote host
            conn.sendall(data)




    



