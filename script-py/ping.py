#!/usr/bin/python

import subprocess,sys

ipInicial = sys.argv[1]

for ipFinal in range(0,25):
    address = ipInicial + "." + str(ipFinal)
    res = subprocess.call(['ping', '-c', '1', address])
    if res == 0:
        print("ping to", address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")