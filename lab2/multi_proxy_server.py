#!/usr/bin/env python3
import socket, time, sys
from multiprocessing import Process

# TO-DO: get_remote_ip() method

# TO-DO: handle_request() method

def main():

# TO-DO: establish localhost, extern_host (google), port, buffer size

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start: #establish "start" of proxy (connects to localhost)
#       TO-DO: bind, and set to listening mode

        while True:
            #TO-DO: accept incoming connections from proxy_start, print information about connection

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end: #establish "end" of proxy (connects to google)
                #TO-DO: get remote IP of google, connect proxy_end to it

                #now for the multiprocessing...

                #TO-DO: allow for multiple connections with a Process daemon
                # make sure to set target = handle_request when creating the process.

            #TO-DO: close the connection!