#!/bin/bash
# send a get request to a url and diaplay the 200 status code
curl -s "$1" | wc
