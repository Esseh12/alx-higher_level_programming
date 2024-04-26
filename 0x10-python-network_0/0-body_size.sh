#!/bin/bash
# send a request to a url and display response size

curl -s "$1" | wc -c
