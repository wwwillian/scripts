#!/usr/bin/python

print("Hello World!!!\n");
ip = "192.168.0.1";
porta = 80;
ver = 1.1;

print("Scan version: ",ver);
print("Varrendo Host: ",ip,"na Porta: ",porta,"\n");


print("Scan version: %.1f" %ver);
print("Varrendo Host: %s na Porta: %d" %(ip,porta),"\n");

print("Tipos - version ",type(ver)," | Host ",type(ip)," | Porta ",type(porta),"\n");

#Modo interativo

ip = input("Digite o IP: "); #string
porta = int(input("Digite a porta: ")); #int

print("Varrendo Host: %s na Porta: %d" %(ip,porta),"\n");

