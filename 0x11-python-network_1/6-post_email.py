#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)

    print(req.text)
