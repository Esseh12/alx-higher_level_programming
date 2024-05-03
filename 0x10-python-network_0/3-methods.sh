#!/bin/bash
# a bash script that displays all HTTP methods the server will accept
curl -s -i  "$1" -X OPTIONS | grep -i '^allow:' | cut -d' ' -f2-
