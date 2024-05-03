#!/bin/bash
# a bash script that displays all HTTP methods the server will accept
curl -s "$1" --request -L OPTIONS
