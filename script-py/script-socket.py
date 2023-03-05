#!/usr/bin/python

import socket,sys

ip = str(input("Digite o IP: "))
port = int(input("Digite a Porta: "))

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = meusocket.connect_ex((ip,port))

if (res == 0):
    print("Porta Aberta")
else:
    print("Porta Fechada")
