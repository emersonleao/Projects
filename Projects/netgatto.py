#!/usr/bin/env python

# Netgatto meow 
# My own implementation of netcat. Emerson 28.09.2021

import sys

# collect the arguments
hostname = sys.argv[1]
port     = int(sys.argv[2])

def netgatto(hn, p):
    #initalize the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hn, p))

    sock.sendall(content)
    time.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    print("Connection closed.")
    sock.close()


content = "GET / HTTP/1.1\nHost: google.com\n\n"

while 1:
    buf = ""
    shouldClose = False

    #collect the request
    inp = input("")
    while input != "":
        # stop processing if we want connection to close
        if (inp == "Connection: close"):
            shouldClose = True
        buf += inp + "\n"
        inp = input("")

    buf += "\n"

    #send the request to the server
    netgatto(hostname, port, buf.encode())

    if (shouldClose):
        break


