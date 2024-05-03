#!/bin/bash
# a bash script that takes in a url, and sends a request to it
curl -s "$1" | wc -c
