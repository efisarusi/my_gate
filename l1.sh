#!/bin/bash
while true
do
    echo "wait"
    socat tcp-l:22290,reuseaddr EXEC:'echo -e "HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: *\r\nContent-Length: 13\r\n\r\nHEllo, World!"'
    date >> log1.txt
    echo "start"
    python3 l1.py
done