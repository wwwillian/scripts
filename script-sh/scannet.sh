#!/bin/bash

if [ "$1" == "" ]; then
    echo "Informe IP: 192.168.0";
else
    for ip in {0..24}; do
        hping3 -S -p 80 -c 1 $1.$ip 2> /dev/null;
    done;
fi;
