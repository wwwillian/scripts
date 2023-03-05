#!/usr/bin/python

import socket,sys

ip = str(input("Digite o IP: "))
port = int(input("Digite a Porta: "))

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect_ex((ip,port))

banner = meusocket.recv(1024)

print(banner)