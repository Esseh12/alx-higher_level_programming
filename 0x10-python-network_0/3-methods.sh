#!/bin/bash
# a bash script that displays all HTTP methods the server will accept
curl -sL "$1" -X OPTIONS 
