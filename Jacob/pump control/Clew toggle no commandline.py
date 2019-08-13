# import Flushy




#toggles flush pump


import ctypes
import os,sys
import time
# myp = os.path.dirname(__file__)

myp = os.path.dirname(sys.argv[0]) + os.sep
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
pump_p = lib + os.sep + "pump control" +os.sep


def reportstatus(s):
	with open(temp + "pump.txt", "w") as f:
		f.write(str(s))
		
	


FlushDLL = ctypes.WinDLL(myp + os.sep + "flush.dll")

f = ctypes.c_int()
interface = ctypes.c_int()
# FlushDLL = ctypes.WinDLL("flush.dll")
f = FlushDLL.FCWInitObject()
g = FlushDLL.FCWOpenCleware(f)
# hn = FlushDLL.FCWGetHandle(f,0)
# serialnumber = FlushDLL.FCWGetSerialNumber(f,0)
# print hn


#1;on/off
#2;Device number
#3;Channel

print("Toggling pump")

interface = f
devno = 0

channel = 16
# print channel,devno,sys.argv[2],sys.argv[3]
# ch1 = 16
# ch2 = 17
# ch3 = 18
# ch4 = 19


if FlushDLL.FCWGetSwitch(interface,devno,channel) == 0:
	flush = FlushDLL.FCWSetSwitch(interface,devno,channel,1)
	reportstatus(0)
else:
	flush = FlushDLL.FCWSetSwitch(interface,devno,channel,0)
	reportstatus(1)