#!/usr/bin/python

import socket
import time
import fileinput
import os
HOST = '' #locahost 
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

DatFile = open("data.txt", 'r', os.O_NONBLOCK)

while True:
	for line in DatFile:	
		#message = raw_input("Your message: ")
		#currentTime = time.ctime(time.time()) + "\r\n"
		#s.send(currentTime.encode('ascii'))
		s.send(line)
		print ("Client awaiting reply")
		reply = s.recv(1024) #1024 is maximum data that can be received
		print ("Client received ", repr(reply))
		
