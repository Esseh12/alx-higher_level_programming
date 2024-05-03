#!/bin/bash
# a bash script that displays all HTTP methods the server will accept
curl -s -i -L "$1" -X OPTIONS 
