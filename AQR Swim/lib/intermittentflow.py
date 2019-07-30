import numpy as np
import sys, os,time,filehandling
from subprocess import Popen
# import filehandling
# Directories
myp = os.path.dirname(sys.argv[0]) + os.sep
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
pump_p = lib + os.sep + "pump control" +os.sep


def Conventional(tf,tw,tm):
#Experimental control for IMF starting with flush period. 
#Having only 1 channel to control the entire setup
	global interface
	devno = 0
	ch1 = 16
	
	exp = True	
	print "Starting experimental cycle"
	while exp:	

		Popen(["python", lib + os.sep + "Pump.py","1","0","0","0"])
		
		print( "Flush started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),tf)	
		exp = filehandling.TjekRun()
		
		if not exp: break
		filehandling.PrintPeriod("F")
		
		time.sleep(float(tf))
		Popen(["python", lib + os.sep +"oxygenserver.py"])
		
		Popen(["python", lib + os.sep + "Pump.py","0","0","0","0"])
		Popen(["python", lib + os.sep + "Pump.py","0","0","0","0"])
		

		print("Waiting period started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),tw)
		filehandling.PrintPeriod("W")
		
		
		exp = filehandling.TjekRun()
		if not exp: break
		
		time.sleep(float(tw))
		Popen(["python", lib + os.sep + "waitendevent.py"])
	
		
		print("Measurement period started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),tm)
		filehandling.PrintPeriod("M")
		
		exp = filehandling.TjekRun()
		if not exp: break
		
		time.sleep(float(tm))
	
		
	Popen(["python", lib + os.sep + "Pump.py","1","0","0","0"])
	Popen(["python", lib + os.sep + "Pump.py","1","0","0","0"])
	
	print("Experiment End")

Conventional(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))