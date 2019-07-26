from ctypes import WinDLL,c_long,c_int,byref
import os,filehandling
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
temppath = mainpath + "temp" + os.sep

# # # # 	
def DigitalIO(bn,ch,state):
## Controls digital channels
	with open("C:\AQUARESP\Settings\OU_DLL.txt","r") as f:
		getdllstr = f.readlines()
	dllstr = getdllstr[0]
	USB1208dll = WinDLL(dllstr)
	# USB1208dll.cbFlashLED(0)
	USB1208dll.cbDOut(0,10,state) #Writes state to port
	Gadus = "Not relevant"
	return Gadus

def tail( f,window=1):
	#Reads only end of text tile 
	
    BUFSIZ = 1024
    f.seek(0, 2)
    bytes = f.tell()
    size = window
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if (bytes - BUFSIZ > 0):
            # Seek back one whole BUFSIZ
            f.seek(block*BUFSIZ, 2)
            # read BUFFER
            data.append(f.read(BUFSIZ))
        else:
            # file too small, start from begining
            f.seek(0,0)
            # only read what was not read
            data.append(f.read(bytes))
        linesFound = data[-1].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
			
    return '\n'.join(''.join(data).splitlines()[-window:])
	
def ReadFiresting(fn):
	with open(fn,'r') as f:
		ans =  tail(f)
		
	n = 0
	try:
		pO2_1 = ans.split("\t")[4+n]
		pO2_2 = ans.split("\t")[5+n]
		pO2_3 = ans.split("\t")[6+n]
		pO2_4 = ans.split("\t")[7+n]
		# print pO2_1, pO2_2, pO2_3, pO2_4
		oxtime = ans.split("\t")[1]
	except IndexError: 
		print("read error")
		pO2_1 = -4
		pO2_2= -4
		pO2_3= -4
		pO2_4= -4
		oxtime = -4
	# print oxtime
	return float(pO2_1),pO2_2,pO2_3,pO2_4,oxtime
	
def ReadFirestingOld(fn):

	print(fn)
	with open(fn,'r') as f:
		ans =  tail(f)
		
	n = -1
	try:
		pO2_1 = ans.split("\t")[4+n]
		pO2_2 = ans.split("\t")[5+n]
		pO2_3 = ans.split("\t")[6+n]
		pO2_4 = ans.split("\t")[7+n]
	
		oxtime = ans.split("\t")[1+n]
	except IndexError: 
		print("read error")
		pO2_1 = -4
		pO2_2= -4
		pO2_3= -4
		pO2_4= -4
		
	
	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime

def ReadFibox3_1ch(fn):
	with open(fn,'r') as f:
		ans =  tail(f)
	n= -1
	try:
		pO2_1 = ans.split(";")[3].split(" ")[-1]
		oxtime = ans.split(";")[2].split(" ")[-1]
		oxclock = ans.split(";")[1].split(" ")[-1]
		
		# pO2_1 = PO2[0].replace(",",".")
		
		
	except IndexError:
		pO2_1 = -9999
		oxtime = -9999
		oxclock = "00:00:00"
	
	return float(pO2_1), oxtime,oxclock
		
	
def ReadPresens4(fn):
	PO2 = []
	for ch in range(1,5):
		# print ch
		fnr = fn + "-ch" +str(ch)+".txt"
		# print fnr
		
		
		
		with open(fnr,'r') as f:
			ans =  tail(f)
		
		PO2.append(ans.split(";")[3])
			
		# print ans
	# n = 1
	
	
	pO2_1 = PO2[0].replace(",",".")
	pO2_2 = PO2[1].replace(",",".")
	pO2_3 = PO2[2].replace(",",".")
	pO2_4 = PO2[3].replace(",",".")
	oxtime = ans.split(";")[1]
	# print PO2
	# print oxtime
	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime
	

	
def SensorMess():
	#Keeps track of what sensor is used
	# sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol, UNIXtime, Dateime, IsSlave  = filehandling.GetExperimentInfo()
	ExpName, ft,wt,mt,temperature,salinity, UNIXtime, Dateime = filehandling.GetExperimentInfo()
	# print sensor
	sensor = "0"
	Firesting = False
	Presens4 = False
	Fibox3 = False
	Fibox4ch = False
	
	
	FNFiresting = "--"
	FNFibox = "--"
	
	
	if sensor =="4":
		Firesting = False
		Presens4 = False
		Fibox3 = True
		FNFibox =  mainpath + "O2 log" + os.sep + "fibox3.txt"
		
	elif sensor =="0":
		Firesting = True
		Presens4 = False
		Fibox3 = False
		FNFiresting = mainpath + "O2 log" + os.sep + "firesting.txt"
		
		
	fnslave = "O2 slave.txt"
	return Firesting, Presens4, Fibox3, FNFiresting, FNFibox, fnslave			

def uniformoxygen():
	Firesting, Presens4, Fibox3, FNFiresting, FNFibox, fnslave = SensorMess()
	# print Firesting, Presens4, Fibox3, FNFiresting, FNFibox
	# print Firesting
	
	Firesting = True
	Fibox = False
	
	if Firesting:
		pO2_1,pO2_2,pO2_3,pO2_4,oxtime = ReadFiresting(FNFiresting)

				
	if Fibox3:
		pO2_1,oxclock,oxtime = ReadFibox3_1ch(FNFibox)
		pO2_2,pO2_3,pO2_4 = ["-","-","-"]
		pO2_1 = pO2_1.replace(",",".")
	
	
	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime	
	
	
	
# fn = "C:\\AQUARESP\\temp\\oxygen\\presens"
# fn = mainpath + "oxygen\\fibox3.txt"
# ReadPresens4(fn)
	
# ReadFibox3_1ch(fn)
# print uniformoxygen()
	
	
	
	
	
	
	
# print "ON"	
# DigitalIO(0,10,1)
# time.sleep(6)
# print "OFF"
# DigitalIO(0,10,1)




#Legacy
# # # # def AnalogRead(bn,ch,ran):

	# # # # ## AnalogRead - reads one value from a MCC board and returns bit value (Va) and voltage (vread)
	
	# # # # ## bn - board number - integer
	# # # # ## ch - channel - integer
	# # # # ## res - board resolution - integer
	# # # # res = 12
	# # # # ## MAD - max AD range
	# # # # MADs = {4:1,
			# # # # 14:2,
			# # # # 16:3,
			# # # # 0:5,
			# # # # 10:10,
			# # # # 105:1,
			# # # # 103:2,
			# # # # 102:2.5,
			# # # # 101:5,
			# # # # 100:10
	# # # # }
	# # # # ## ran  - AD range - integer or string
	# # # # ## polar - polarity of AD range
	# # # # polarities = {	4:2,
			# # # # 14:2,
			# # # # 16:2,
			# # # # 0:2,
			# # # # 10:2,
			# # # # 105:1,
			# # # # 103:1,
			# # # # 102:1,
			# # # # 101:1,
			# # # # 100:1}
	
	
	

			

	
	# # # # with open("C:\AQUARESP\Settings\OU_DLL.txt","r") as f:
		# # # # getdllstr = f.readlines()

	# # # # dllstr = getdllstr[0]
	# # # # USB1208dll = WinDLL(dllstr)

	# # # # resbit = 2 ** res

	# # # # Vch = c_long()
	# # # # VC2 = c_int()
	# # # # # USB1208 reads from board 0, ch 0, range 1=+/-10V, and placed the result in c_long Vch
	# # # # VC2 =USB1208dll.cbAIn(bn,ch,ran,byref(Vch))
	# # # # Va=Vch.value   # Va is the read ADC code in Vch location

	# # # # reshalf = float(resbit)/polarities[ran] # Bipolar ranges

	# # # # fraction = float(Va - reshalf) / reshalf 
	# # # # vread = fraction * MADs[ran]
	# # # # return Va,vread	
	
	



