#!/usr/bin/python
import sys

if len(sys.argv) <= 2:
	print("Passar dois parametros: ex. 10.10.1.0 80\n");
else :
	print("Varrendo host:",sys.argv[1],"no porta",sys.argv[2],"\n");


for ip in range(1,10):
	print("Varrendo IP: 192.168.0.%s" %ip);
