#!/usr/bin/env python
import os
from pyfiglet import Figlet

os.system("clear")
pyf = Figlet(font='puffy')
a = pyf.renderText("Emerson's UDP chat")
os.system("tpuf setaf 3")
print(a)

# importing modules for the chat app

import socket
import time
import threading
import sys

# AF_INET = Network Address Family: IPv4
# SOCK_DGRAM = Datagram socket: UDP

# Function for receiving
def receiver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip_sender, port_sender)) #binding the IP address and port number
    while True:
        msg = s.recvfrom(1024)
        print("\n"+msg[0].decode())
        if "exit" in msg[0].decode() or "bye" in msg[0].decode():
            sys.exit()

# Function for sending
def sender():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = "hello"
    while True:
        if "bye" in text or "exit" in text or "finish" in text:
            exit()
        else:
            text = input(f'{name}:')
            text = name+":"+text
            s.sendto(text.encode(), (ip_receiver, port_receiver))

print("Initializing...")

ip_receiver = input("\nEnter the IP of receiver: ")
port_receiver = int(input("\nEnter the port of the receiver: "))

ip_sender = input("\nEnter your IP: ")
port_sender = int(input("\nEnter your port: "))

name = input("Enter your name: ")

print("Waiting for client...")
time.sleep(1)
print("Connection established...")

# Using multithreading
send = threading.Thread(target=sender)
receive = threading.Thread(target=receiver)

send.start()
receive.start()
