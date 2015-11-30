#!/usr/bin/python
#Moduls
import time
import datetime
import random
import os
#(BSid, lastAlive, alarmState, waterDetection)
i =0
BSid = 0
WaterDetector = 2
#Open a sensors data file
SenseData = open("data.txt", "w")

while i < 20:
	time.sleep(5)
	t = time.strftime("%Y-%m-%d %H:%M:%S")
	BSid+=1 
	AlarmState = random.randint(0, 1)
	if WaterDetector%2 == 0:
		WD = 1
	else:
		WD = 2
	WaterDetector+=1
	print BSid, t, AlarmState, WD
	D = []
	D = (BSid, t, AlarmState, WD)
	
	
	SenseData.write(str(BSid))
	SenseData.write(" ")
	SenseData.write(str(t))
	SenseData.write(" ")
	SenseData.write(str(AlarmState))
	SenseData.write(" ")
	SenseData.write(str(WD))
	SenseData.write("\n")
	SenseData.flush()
	
