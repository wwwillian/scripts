#!/usr/bin/python

import urllib.request,sys

site = urllib.request.urlopen(sys.argv[1])
server = site.info()

print("O servidor web esta rodando")
print(server['Server'])