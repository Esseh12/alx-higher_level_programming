#!/usr/bin/python3
""" a Python script that takes in a URL
- sends a request to the URL
- displays the body of the response (decoded in utf-8)"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print(f"Error code: {er.code}")
