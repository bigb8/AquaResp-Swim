# import Flushy




#toggles flush pump


import ctypes
import os,sys
import time
#myp = os.path.dirname(__file__)

myp = os.path.dirname(sys.argv[0]) + os.sep
print(myp)
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
pump_p = lib + os.sep + "pump control" +os.sep


def reportstatus(s):
	with open(temp + "pump.txt", "w") as f:
		f.write(str(s))
		
	


FlushDLL = ctypes.WinDLL(myp + os.sep + "flush.dll")


FlushDLL.FCWInitObject.restype =  ctypes.c_void_p  ## THIS IS PARAMOUNT TO MAKE THE USB-LUMINUS WORK!!

FlushDLL.FCWOpenCleware.argtypes = [ctypes.c_void_p]
FlushDLL.FCWOpenCleware.restype = ctypes.c_int



FlushDLL.FCWSetSwitch.argtypes = [ctypes.c_void_p, ctypes.c_int,ctypes.c_int,ctypes.c_int]
FlushDLL.FCWSetSwitch.restype = ctypes.c_int

FlushDLL.FCWGetSwitch.argtypes = [ctypes.c_void_p, ctypes.c_int,ctypes.c_int]
FlushDLL.FCWGetSwitch.restype = ctypes.c_int


f = FlushDLL.FCWInitObject()

# f = ctypes.c_long(f)
print(f)
# serialnumber = FlushDLL.FCWGetSerialNumber(f,0)
# print(f,serialnumber)
# g = FlushDLL.FCWOpenCleware(ctypes.byref(f))
g = FlushDLL.FCWOpenCleware(f)

# 66463
# hn = FlushDLL.FCWGetHandle(f,0)

# print hn


#1;on/off
#2;Device number
#3;Channel

print( "Toggling pump")

interface = f
devno = int(sys.argv[2])

channel = int(sys.argv[3]) + 16
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