#!/usr/bin/python

import socket
import time
import MySQLdb
# from socket import *
# from import socket, bind, listen, recv, send

HOST = '' #locahost 
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) # how many connections it can receive at one time

conn, addr = s.accept() #accept the connection
print ("Connected by" , addr) #print the address of a person connected

con = MySQLdb.connect(host="localhost", user="root", passwd="a5089012")#connect to MySQl data base
con.query('DROP DATABASE testdb')
con.query('CREATE DATABASE testdb')
con.query("GRANT ALL ON testdb.* to ''@'localhost'")
con.commit()
con=MySQLdb.connect(db='testdb')
cur = con.cursor()
cur.execute('CREATE TABLE `testdata` \
(`bsID` int(11) NOT NULL AUTO_INCREMENT,\
`lastAlive` datetime NOT NULL,\
`alarmState` int(1) NOT NULL,\
`waterDetection` int(1) NOT NULL,\
PRIMARY KEY (`bsID`)) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;')

Logfile = open("LogFile.dat", "w")#creating a new logfile which collects alarmed states

while True:
	data = conn.recv(1024) #user will receive 1024 bytes and store it in data. Server is listening
	print "Server received: ", repr(data) #print received data
	
	t = data.split()
	t1 = t[0]#BSid
	t2 = t[1]#lastAlive date
	t3 = t[2]#lastAlive time
	t4 = t[3]#alarmState
	t5 = t[4]#waterDetector
	datetime = [t2, t3]
	dt = ' '.join(datetime)
	
	#------------MySQL updating segment------------------
	
	cur.execute("INSERT INTO `testdata` (BSid, lastAlive, alarmState, waterDetection) \
				VALUES (%s, %s, %s, %s)", (t1, dt, t4, t5))
	con.commit()
	#----------------------------------------------------
	#Updating log file in case alarm ocurred
	if t4 == '1':
		Logfile.write("Alarm occured: ")
		Logfile.write("BsID: ")
		Logfile.write(t1)
		Logfile.write(" DateTime: ")
		Logfile.write(dt)
		Logfile.write(" Water Detector: ")
		Logfile.write(t5)
		Logfile.write("\n")
		
	#-----------------------------------------------------
	time.sleep(5)
	
	reply = "From server- Update me..."
	conn.sendall(reply)
	

conn.close()	
