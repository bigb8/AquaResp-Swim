import Flushy
import ctypes
import os
import time
from subprocess import Popen

myp = os.path.dirname(__file__)
# print os.path.dirname(sys.argv[0])
FlushDLL = ctypes.WinDLL(myp + os.sep + "flush.dll")
f = FlushDLL.FCWInitObject()
g = FlushDLL.FCWOpenCleware(f)
# hn = FlushDLL.FCWGetHandle(f,0)
# serialnumber = FlushDLL.FCWGetSerialNumber(f,0)
# print hn

interface = f
devno = 1
ch1 = 16
ch2 = 17
ch3 = 18
ch4 = 19
# status = FlushDLL.FCWGetSeqSwitch(f,devno,ch1,0)

Flushy.FlipOn(interface,devno,ch1)
# print  myp +os.sep +"aupload.py"
# Popen(["python",  myp +os.sep +"aupload.py"])