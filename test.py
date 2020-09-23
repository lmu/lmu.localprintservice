#!./bin/python

import requests


url = "http://localhost:6543/api/v1/print"

with open("doc.pdf", "rb") as input:
    data = input.read()
    r = requests.request("PUT", url, data=data, headers={"Content-Type": "application/pdf"})
    print(r)
