#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = "" #same as local host 
PORT = 8001 #consistent port 
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3, use on of this
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2) #constsitent listing 
        
        #continuously listen for connections
        while True: #connection
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close() #no shut down 

if __name__ == "__main__":
    main()
