

import os,sys
from subprocess import Popen
myp = os.path.dirname(sys.argv[0]) + os.sep
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
pump_p = lib + os.sep + "pump control" +os.sep

def pumpstatus():
	with open(temp + "pump.txt", "r") as f:
		status = f.read()
	return status
	
	
def testpump(optionalnonsense=1):
	Popen(["python", lib + os.sep + "Pump.py","1","0","0","1"])
	stat = pumpstatus()
	return stat