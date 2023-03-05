#!/usr/bin/python

import requests,sys

site = requests.get(sys.argv[1])
status = site.status_code

if (status == 200):
    print("Site Existe")
else:
    print("Site Inexistente")