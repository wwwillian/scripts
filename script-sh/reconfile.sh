#!/bin/bash
lynx -dump "https://google.com/search?num=100&q=site:"$1"+ext:"$2"" | cut -d "=" -f2 | grep ".$2" | egrep -v "site|google" | sed s'/...$//'g

# dirb http://rh.businesscorp.com.br /usr/share/dirb/wordlists/small.txt -a "User-Agent: DesecTool"
# exiftool key.png
# curl -i --silent businesscorp.com.br | grep "href=\"http" | sed "s/.*:\/\///" | cut -d"\"" -f1 | sed "s/\/.*//" > /tmp/parsing └─$ curl -i --silent businesscorp.com.br | grep "href=\"http" | sed "s/.*:\/\///" | cut -d"\"" -f1 | sed "s/\/.*//" > /tmp/parsing
# curl -I -H "User-Agent: DesecTool" http://172.16.1.60/index.aspx