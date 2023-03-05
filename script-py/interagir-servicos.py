#!/usr/bin/python

import socket,sys

print("FTP Service")
ip = str(input("Digite o IP: "))
port = 21

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect_ex((ip,port))
banner = meusocket.recv(1024)
print(banner,"\n")

print("Enviando o USER")
st="USER ricardo\r\n"
byt=st.encode()
meusocket.send(byt)
banner = meusocket.recv(1024)
print(banner,"\n")

print("Enviando o PASS")
st="PASS ricardo\r\n"
byt=st.encode()
meusocket.send(byt)
banner = meusocket.recv(1024)
print(banner)
