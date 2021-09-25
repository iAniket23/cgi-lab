#!/usr/bin/env python3
import secret, templates 
from http import cookies
import json
import os

# Q1
print('Content-Type: application/json\r\n\r\n')
print(json.dumps(dict(os.environ), indent = 4))

# Q2
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
message = "\nQuery string:{}".format(os.environ.get('QUERY_STRING'))
print(message)
print("<br>")
message = "\nBrowser:{}".format(os.environ.get("HTTP_USER_AGENT"))
print(message)
print("<br>")
print(templates.login_page()) # Q4