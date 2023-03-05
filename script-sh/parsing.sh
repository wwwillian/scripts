#!/bin/bash

COLOR="\e[33m"
ENDCOLOR="\e[0m"
FILE="/tmp/parsing";

if [ "$1" == "" ]; then
    echo -e "${COLOR}############################################${ENDCOLOR}";
    echo -e "${COLOR}|->             PARSING HTML             <-|${ENDCOLOR}";
    echo -e "${COLOR}|->    Desec Security - Willian Gomes    <-|${ENDCOLOR}";
    echo -e "${COLOR}|->     ./parsing.sh www.alvo.com.br     <-|${ENDCOLOR}";
    echo -e "${COLOR}############################################${ENDCOLOR}";
else
    echo -e "${COLOR}############################################${ENDCOLOR}";
    echo -e "${COLOR}|->          Buscando Hosts ...          <-|${ENDCOLOR}";
    echo -e "${COLOR}############################################${ENDCOLOR}";

    curl -i --silent $1 | grep "href=\"http" | sed "s/.*:\/\///" | cut -d"\"" -f1 | sed "s/\/.*//" > $FILE;
    
    for URL in $(cat $FILE); do
        sleep 1;
        echo $URL;
    done;

    echo -e "\n";
    echo -e "${COLOR}############################################${ENDCOLOR}";
    echo -e "${COLOR}|->         Resolvendo Hosts ...         <-|${ENDCOLOR}";
    echo -e "${COLOR}############################################${ENDCOLOR}";

    for URL in $(cat $FILE); do
        host $URL | grep "has address";
    done;

    rm -f $URL;
fi;