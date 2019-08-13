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

FlushDLL.FCWInitObject.restype =  ctypes.c_void_p  ## THIS IS PARAMOUNT TO MAKE THE USB-LUMINUS WORK!!

FlushDLL.FCWOpenCleware.argtypes = [ctypes.c_void_p]
FlushDLL.FCWOpenCleware.restype = ctypes.c_int



FlushDLL.FCWSetSwitch.argtypes = [ctypes.c_void_p, ctypes.c_int,ctypes.c_int,ctypes.c_int]
FlushDLL.FCWSetSwitch.restype = ctypes.c_int

FlushDLL.FCWGetSwitch.argtypes = [ctypes.c_void_p, ctypes.c_int,ctypes.c_int]
FlushDLL.FCWGetSwitch.restype = ctypes.c_int



# FlushDLL = ctypes.WinDLL("flush.dll")
f = FlushDLL.FCWInitObject()
g = FlushDLL.FCWOpenCleware(f)
# hn = FlushDLL.FCWGetHandle(f,0)
# serialnumber = FlushDLL.FCWGetSerialNumber(f,0)
# print hn


#1;on/off
#2;Device number
#3;Channel



interface = f
devno = int(sys.argv[2])
# devno = 0

channel = int(sys.argv[3]) + 16
# print channel,devno,sys.argv[2],sys.argv[3]
# ch1 = 16
# ch2 = 17
# ch3 = 18
# ch4 = 19

# print sys.argv[1], sys.argv[2], sys.argv[3], channel, devno
# flush = FlushDLL.FCWSetSwitch(interface,devno,channel,int(sys.argv[1]))
flush = FlushDLL.FCWSetSwitch(interface,devno,channel,int(sys.argv[1]))
# reportstatus(sys.argv[3])