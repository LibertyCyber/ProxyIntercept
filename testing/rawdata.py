#!/usr/bin/env python3

import requests
import re

rdata = b'POST http://docker.hackthebox.eu:32453/ HTTP/1.1\r\nHost: docker.hackthebox.eu:32453\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://docker.hackthebox.eu:32453/\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 13\r\nOrigin: http://docker.hackthebox.eu:32453\r\nConnection: keep-alive\r\nCookie: _ga=GA1.2.625538749.1581830366; _gid=GA1.2.910099240.1582343166\r\nUpgrade-Insecure-Requests: 1\r\n\r\npassword=fdsf'
clean = rdata.decode('utf-8')


lol = re.findall(r'POST .+? HTTP/', clean)
host = lol[0][5:-6]
print(host)

x = requests.post(host, data = rdata)

print(x.content)