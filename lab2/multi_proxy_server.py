#!/usr/bin/env python3
import socket, time, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

# TO-DO: get_remote_ip() method
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip

# TO-DO: handle_request() method
def handle_request(conn,proxy_end):
    full_data = conn.recv(BUFFER_SIZE)
    print(f"Sending recieved data {full_data} to google com")
    proxy_end.sendall(full_data)
    proxy_end.shutdown(socket.SHUT_WR)
    data = proxy_end.recv(BUFFER_SIZE)
    print(f"Sending recieved data {data} to client")
    #send back
    conn.send(data)
    

def main():

# TO-DO: establish localhost, extern_host (google), port, buffer size
    extern_host = 'www.google.com'
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start: #establish "start" of proxy (connects to localhost)
#       TO-DO: bind, and set to listening mode
        print("Starting proxy server")
        #allow reused addresses, bind, and set to listening mode
        proxy_start.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        proxy_start.bind((HOST,PORT))
        proxy_start.listen(1)

        while True:
            #TO-DO: accept incoming connections from proxy_start, print information about connection
            conn, addr = proxy_start.accept()
            print("Connected by", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end: #establish "end" of proxy (connects to google)
                remote_ip = get_remote_ip(extern_host)
                proxy_end.connect((remote_ip,port))
                #now for the multiprocessing...
                #TO-DO: allow for multiple connections with a Process daemon
                #send data
                #connect proxy_start
                # make sure to set target = handle_request when creating the process.
                p = Process(target=handle_request,args=(conn,proxy_end))
                p.daemon = True
                p.start()
                print("Started process", p)

        conn.close()

if __name__ == "__main__":
    main()       