#!./bin/python

import base64
import requests


url = "http://localhost:6543/api/v1/printpdf"

with open("doc.pdf", "rb") as input:
    data = input.read()
    #data = base64.b64encode(data)
    r = requests.request("PUT", url, data=data, headers={"Content-Type": "application/pdf"})
    print(r)
