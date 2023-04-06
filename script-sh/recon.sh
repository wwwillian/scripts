#!/bin/bash
FILE="/usr/share/dirb/wordlists/big.txt"

for STRING in $(cat $FILE); do
 
    RESULT=$(curl -s -H "User-Agent: DesecTool" -o /dev/null -w "%{http_code}%" $1/$STRING/);
   
    if [[ "$RESULT" == *"200"* ]]; then
        echo "Diretório encontrado: $1/$STRING/";
    fi;
done;
