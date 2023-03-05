#!/usr/bin/python

#Paramentros
#
import sys
#
print("Varrendo host:",sys.argv[1],"no porta",sys.argv[2],"\n");

#Comandos do sytema operacional
#
import os
#
print("Verificando portas abertas: ");
os.system("netstat -nltp");
