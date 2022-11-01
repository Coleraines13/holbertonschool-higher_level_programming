#!/usr/bin/python3
"""this will display the x-request-id varible of a given url"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r= requests.get(url)
    print(r.headers.get("X-Request-Id"))
