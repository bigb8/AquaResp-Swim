import os,sys
import numpy as np
import aquarespdevice
import aquacalc

myp = os.path.dirname(sys.argv[0]) + os.sep
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
pump_p = lib + os.sep + "pump control" +os.sep




def getO2():
	#Check sensor
	with open(temp + "O2 sensor.txt","r") as f:
		r = f.readline()
		
	r = r.split(";")
		
	
	sensor = r[1]
	sensorn = int(r[0])
	# print sensor, sensorn
	if sensorn < 4:
		#Firesting sting type sensor
		sensorlog = "firesting.txt"
		
		#Acquire O2
		pO2_1,pO2_2,pO2_3,pO2_4,oxtime = aquarespdevice.ReadFiresting(main + "O2 log" + os.sep + sensorlog)
		
		
	elif sensorn == 5:	
		#Presen Fibox type sensor
		#Fibox 3:
		sensorlog = "fibox3.txt"
		
		#Acquire O2
		pO2_1, oxtime,oxclock = aquarespdevice.ReadFibox3_1ch(main + "O2 log" + os.sep + sensorlog)
		pO2_2 = pO2_3 = pO2_4 = 99999
	
	
	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime
	
# getO2()















import os,time
from ctypes import WinDLL,c_long,c_int,byref

myp = os.path.realpath(__file__).split("aquaread.")[0]
temp = myp.split("lib")[0] + os.sep + "temp" + os.sep


def returnvoltage():
	#Get present DAQ
	
	#Read voltage
	
	bit,V = MMC1208Read(0,0,0)
	
	#return
	return V

def getcalflow():
	with open(temp + "flowcal.txt","r") as f:
		data = f.readlines()[1]
	
	data = data.split(";")
	
	slope = data[0]
	intercept = data[1]
	return slope,intercept
	
def returnUfromCal():
	V = returnvoltage()
		
	slope, intercept = getcalflow()
	U = float(slope)*float(V) + float(intercept)
	
	
	if os.path.isfile(temp + "fish.txt"): 
		with open(temp + "fish.txt","r") as fe:
			datatemp = fe.readlines()[1].split(";")
	
	mf = float(datatemp[0])		
	wf = float(datatemp[1])		
	hf = float(datatemp[2])		
	lf = float(datatemp[3])		
	
	
	if os.path.isfile(temp + "respirometer.txt"): 
		with open(temp + "respirometer.txt","r") as fe:
			datatemp = fe.readlines()[1].split(";")
	
	wr = float(datatemp[1])	
	hr = float(datatemp[2])	
			
	Uc = aquacalc.solidblocking(U,wf,hf,lf,hr,wr)
	
	Ubl = Uc / lf
	
	with open(temp + "currentflow.txt",'w') as f:
		f.write("%s;%s;%s;%s;" %	(U,Uc,Ubl,V))
	
	return U,Uc,Ubl,V
	
	
def getflow():
	with open(temp + "currentflow.txt",'r') as f:
		data = f.readlines()
	
	try:
		U,Uc,Ubl,V,nnnn = data[0].split(";")
	except IndexError:
		U,Uc,Ubl,V,nnnn = (9999,9999,9999,9999,9999)
	except ValueError:
		U,Uc,Ubl,V,nnnn = (9999,9999,9999,9999,9999)
	# print U,Uc,Ubl,V
	return U,Uc,Ubl,V
	
	
def MMC1208Read(bn,ch,ran):
	## AnalogRead - reads one value from a MCC board and returns bit value (Va) and voltage (vread)
	
	## bn - board number - integer
	## ch - channel - integer
	## res - board resolution - integer
	res = 12
	## MAD - max AD range
	MADs = {4:1,
			14:2,
			16:3,
			0:5,
			10:10,
			105:1,
			103:2,
			102:2.5,
			101:5,
			100:10
	}
	## ran  - AD range - integer or string
	## polar - polarity of AD range
	polarities = {	4:2,
			14:2,
			16:2,
			0:2,
			10:2,
			105:1,
			103:1,
			102:1,
			101:1,
			100:1}
	
	
	# with open("C:\AQUARESP\Settings\OU_DLL.txt","r") as f:
		# getdllstr = f.readlines()
	# dllstr = myp + "CBW32.dll"
	# dllstr = "C:\Program Files (x86)\Measurement Computing\DAQ\cbw32.dll"
	dllstr = lib + "cbw64.dll"
	# print dllstr
	USB1208dll = WinDLL(dllstr)
	# USB1208dll.cbFlashLED(0)

	resbit = 2 ** res

	Vch = c_long()
	VC2 = c_int()
	# USB1208 reads from board 0, ch 0, range 1=+/-10V, and placed the result in c_long Vch
	VC2 =USB1208dll.cbAIn(bn,ch,ran,byref(Vch))
	Va=Vch.value   # Va is the read ADC code in Vch location

	reshalf = float(resbit)/polarities[ran] # Bipolar ranges

	fraction = float(Va - reshalf) / reshalf 
	vread = fraction * MADs[ran]
	
	# print vread,Va,10*(Va/4096.0)
	return Va,vread	
	
	

	
	
	
# for i in range(0,150):
	# time.sleep(.01)
	# returnUfromCal()
	
	
	