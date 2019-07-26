import os,sys,shutil,time,datetime

import numpy as np
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
temppath = mainpath + os.sep +"temp" + os.sep



def getflow():
	with open(temppath + "currentflow.txt",'r') as f:
		data = f.readlines()[0].split(";")
	
	U = float(data[0])
	Uc = float(data[1])
	Ubl = float(data[2])
	V = float(data[3])
	
	return U,Uc,Ubl,V

def presentfolderFunc():
	mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
	temppath = mainpath + os.sep +"temp" + os.sep
	with open(mainpath+ os.sep +"temp" + os.sep+"presentfolder.txt",'r') as f:
		pf = f.read()
	slopefolder = pf +os.sep +"All slopes" + os.sep
	expfolder = pf+os.sep +"Experimental information" + os.sep
	return pf, slopefolder, expfolder 

	
	
	
def SetRun(period):
	with open(temppath + "runningexperiment.txt",'w') as f:
		period = f.write(period)

def FORCEMEASUREMENTEND():
	with open(temppath + "ENDPERIOD.txt",'w') as f:
		period = f.write(str(1))
		
def FORCEMEASUREMENTEND_REQ():
	# try:
	
	with open(temppath + "ENDPERIOD.txt",'r') as f:
		period = f.readlines()
	if period[0] == str(1):
		print("Forced end of period")
		# print period[0], type(period[0])
		with open(temppath + "ENDPERIOD.txt",'w') as f:
			period = f.write(str(0))
	
		return True
	
	# except:pass
	return False
		
		
def TjekRun():	
	with open(temppath + "runningexperiment.txt",'r') as f:
		period = f.read()
		
	if period =="0":
		amirunning = False
	else:
		amirunning = True
		
	return amirunning
	
def PrintPeriod(period):
	with open(temppath + "currentperiod.txt",'w') as f:
		period = f.write(period)
	
def TjekPeriod():	
	with open(temppath + "currentperiod.txt",'r') as f:
		period = f.read()
	return period
	
def ox2file(pO2_1,oxtime1):
	# reads oxygen from firesting and prints to lastpo2.txt
	with open(temppath + "lastpo2.txt",'w') as f:
		f.write("%s;%s;"% (pO2_1,oxtime1))
		
		
		
		

def GetLastOxygen():
	# reads oxygen from firesting and prints to lastpo2.txt
	with open(temppath + "lastpo2.txt",'r') as f:
		all = f.read()
		
	# pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = all.split(";")
	
	pO2_1 = all.split(";")[0]
	pO2_2 = all.split(";")[1]
	pO2_3 = all.split(";")[2]
	pO2_4 = all.split(";")[3]
	oxtime1 = all.split(";") [-1]
	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime1
		
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)	

def CopyExperimentalInfo():

################ NEEEDS UPDATE ####################

	#Copies relavant info from temp to experimental folder
	pf, slopefolder, expfolder = presentfolderFunc()
	for i in range(1,5):
		# try:
			shutil.copyfile(temppath + "respirometer_" + str(i) + ".txt", expfolder + "respirometer_" + str(i) + ".txt" )
		# except:
			# print "g"
			
	shutil.copyfile(temppath + "experiment.txt", expfolder + "experiment.txt")
	shutil.copyfile(temppath + "timestampstart.txt", expfolder + "timestampstart.txt")
	shutil.copyfile(temppath + "water.txt", expfolder + "water.txt")
	shutil.copyfile(temppath + "numresp.txt", expfolder + "numresp.txt")

def SetTimeStartExperiment():
	with open(temppath + "timestampstart.txt",'w') as f:
		f.write("UNIX:"+ str(int(time.time())) + ";\n Datetime:10dec1986;")
		
	
def GetTimeStartExperiment():
	
	with open(temppath + "timestampstart.txt",'r') as f:
		UNIXtimestart = int(f.readlines()[0].split(":")[1].split(";")[0])
	unixtimenow = int(time.time())
	in_seconds =  unixtimenow - UNIXtimestart
	in_hours = in_seconds / 3600.0
	in_minutes = in_seconds / 60.0
	in_days = in_seconds / 86400.0
	# print unixtimenow
	return in_hours, in_minutes,in_seconds, in_days

def updateLastmo2file(last,mo2,r2):
	if last ==1:
		with open(temppath + "lastmo2.txt","a") as f:
			f.write("\n")
		with open(temppath + "lastr2.txt","a") as f:
			f.write("\n")
	elif last == 2:
		with open(temppath + "lastmo2.txt","w") as f:
			f.write("")		
		with open(temppath + "lastr2.txt","w") as f:
			f.write("")
	else:
		with open(temppath + "lastmo2.txt","a") as f:
			f.write("%s;" % mo2 )		
		with open(temppath + "lastr2.txt","a") as f:
			f.write("%s;" % r2 )
			
	
def SetperiodStart(start,duration):
	with open(temppath + "timer.txt",'w') as f:
		f.write(str(start) + ";" + str(duration) + ";" )

def GetperiodStart():
	with open(temppath + "timer.txt",'r') as f:
		all = f.read().split(";")
	return int(all[0]),int(all[1]),int(time.time())-int(all[0])


def SetOC(status):
	with open(temppath + "OC.txt",'w') as f:
		f.write(str(status))

def GetOC():
	with open(temppath + "OC.txt",'r') as f:
		all = f.read()
	return all
	
	
	
def readrespirometerinfo():
	#As function name says
	with open(temppath + "respirometer.txt","r") as f:
		lines = f.readlines()
		
	# inuse = lines[0].split(":")[1].split(";")[0]
	volume = lines[1].split(";")[0]
	sectionwidth = lines[1].split(";")[1]
	sectionheight = lines[1].split(";")[2]
	
	# animalmass = lines[2].split(":")[1].split(";")[0]
	
	return sectionwidth, volume, sectionheight
	
def GetExperimentInfo():
	#As function name says
	with open(temppath + "experiment.txt","r") as f:
		lines = f.readlines()
		
	# sensor = lines[0].split(":")[1].split(";")[0]
	
	
	ExpName = lines[1].split(";")[0]
	temperature = lines[1].split(";")[1]
	salinity = lines[1].split(";")[2]

	ft = lines[1].split(";")[3]
	wt = lines[1].split(";")[4]
	mt = lines[1].split(";")[5]

	
	with open(temppath + "timestampstart.txt","r") as f:
		lines3 = f.readlines()
	
	UNIXtime = lines3[0].split(":")[1].split(";")[0]
	Dateime = lines3[1].split(":")[1].split(";")[0]
	
	
	# return sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol, UNIXtime, Dateime, IsSlave
	return  ExpName, ft,wt,mt,temperature,salinity, UNIXtime, Dateime

def datafileStop():
	# pf, slopefolder, expfolder = presentfolderFunc()

	myfile = temppath  + "Summary data resp " + str(chan)+".txt"	
	sectionwidth, volume, sectionheight = readrespirometerinfo()

	with open(myfile,"w") as f:
		f.write(" ")
	
	# import AquaPlot
	# AquaPlot.fakeJSdatasource()
	
	
	
	
def datafileinit():
	#CHANGE THIS AND USE
	pf, slopefolder, expfolder = presentfolderFunc()
	
	#Check this as well
	# sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol,UNIXtime, Dateime, IsSlave = GetExperimentInfo()
	ExpName, ft,wt,mt,temperature,salinity, UNIXtime, Dateime = GetExperimentInfo()
	
	ensure_dir(pf)
	ensure_dir(slopefolder)
	ensure_dir(expfolder)
	
	
	#Check this as well

	myfile = pf + os.sep + "Summary data.txt"	
	sectionwidth, volume, sectionheight = readrespirometerinfo()

	with open(temppath + "fish.txt","r") as fe:
		datatemp = fe.readlines()[1].split(";")
	animalmass = datatemp[0]
	animalwidth = datatemp[1]
	animalheight = datatemp[2]
	animallength = datatemp[3]
	
	
	
	with open(myfile,"w") as f:
		f.write("AQUARESP 3 - Swim version  - Data file \n")
		f.write("--------------------------------------------------------------------------------------------------------------------------------\n")
		
		f.write("Experiment start, UNIX time: "+str(UNIXtime)+"\n")
		# f.write("Experiment Date and time: "+str(Dateime)+"\n")
		f.write("Flush time ,s: "+str(ft)+"\n")
		f.write("Wait time, s: "+str(wt)+"\n")
		f.write("Measurement time, s: "+str(mt)+"\n")
		f.write("Mass of fish, kg: "+str(float(animalmass)*1e-3)+"\n")
		f.write("Fish length - width - heigth, cm: "+str(animallength) +";" +str(animalwidth) +";"+str(animalheight) +";"+"\n")

		f.write("Volume respirometer, L: "+str(volume)+"\n")
		f.write("Real volume (vresp - vfish) (neutrally bouyant), L: "+str(float(volume) - float(animalmass)*1e-3)+"\n")
		# f.write("Athmospheric pressure: "+str(patm)+"\n")
		f.write("Salinity: "+str(salinity)+"\n")
		f.write("Temperature: "+str(temperature)+"\n")	
		f.write("\n Timestamp is beginning of measurement period \n")
		f.write("-.-.-.-.-.-.-.-.------------------------------------------------------\n")
		f.write("Clock TIME;TIME HOURS;TIME UNIX;MO2 mg/h/kg;MO2 mg/h;SLOPE;Intercept;R^2;P;Std Err; Measurement duration seconds;avg po2;median po2; minimum po2; max po2;delta po2;oxygen solubility;ratio vreal fish;total experiment duration hours;minutes;seconds;days;Animal mass;Average swimspeed not corrrected for solidblocking cm/s;Average swimspeed cm/s;Average swimspeed BL/s;Average voltage;Vh2o L/kg/h;\n")
			

				
def MO2Save(timestartmeasurement,in_hours,unixtime, MO2, slope, intercept, r2, p_value, std_err, duration, avgpo2, medianpo2, minpo2,maxpo2, dpo2, beta, rRespFish, in_hours2, in_minutes,in_seconds, in_days,mf,vr,o2content,avgU,avgUC,avgUBL,avgV):

	#mf,vr,o2content,avg U,avg U,avg U,avg V
	# minus rr
	pf, slopefolder, expfolder = presentfolderFunc()
	
	#"TIME;TIME HOURS;TIME UNIX;MO2;R^2;SLOPE;P;duration seconds;avg po2;median po2; minimum po2; max po2;delta po2;\n"
	
	for paath in [pf, temppath]:
		with open(paath + os.sep +"Summary data.txt","a") as stxt1:
			# stxt1.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;" % (timestartmeasurement,in_hours,unixtime,"%.3f" % MO2, "%.6" %slope, "%.6f" % intercept, "%.6f" %rr, "%.6f" %r2, "%.6f" % p_value, "%.6f" % std_err,duration,"%.2f" % avgpo2,"%.2f" % medianpo2,"%.2f" % minpo2,"%.2f" % maxpo2, "%.2f" % dpo2,"%.2f" % beta,"%.2f" % rRespFish,"%.2f" % in_hours, "%.2f" % in_minutes,in_seconds, "%.2f" % in_days))
			#22
			
			stxt1.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;\n" % (timestartmeasurement,
			in_hours,
			unixtime, 
			MO2,
			mf,
			slope, 
			intercept,  
			r2,  
			p_value,
			std_err,
			duration,
			avgpo2, 
			medianpo2,
			minpo2,
			maxpo2,
			dpo2,
			beta,
			rRespFish,
			in_hours,
			in_minutes,
			in_seconds,
			in_days,
			vr,
			mf,
			avgU,
			avgUC,
			avgUBL,
			avgV,
			MO2/float(beta)))
			
		
	# with open('C:\AQUARESP\\temp\datacurrent'+ str(chh)+'.txt',"a") as atxt:
		# atxt.write(str(time)+";"+str(MO2)+";"+str(PO2)+";"+str(RSQ)+";"+str(SLOPE)+";\n")
def GetsummaryData(ch):
	
	mo2 = []
	po2 = []
	r2 = []
	timesec = []
	num = []
	
	with open(temppath+"Summary data.txt","r") as stxt1:
		all = stxt1.readlines()
	i = 1
	for l in all:
		mo2.append(l.split(";")[3])
		po2.append(l.split(";")[9])
		timesec.append(l.split(";")[1])
		r2.append(l.split(";")[5])
		num.append(i)
		i+=1
		
	return mo2,po2,r2,timesec,num
				
				
def CleanSummaryData():
	for i in range(1,5):
		print("Cleaning up ", i)
		try:
			with open(temppath+"Summary data resp " + str(i)+".txt","w") as stxt1:
				stxt1.write("")
		except: print("not there")
	
	print("Moving files")
	pf, slopefolder, expfolder = presentfolderFunc()
	src = mainpath + "oxygen" + os.sep
	dst = pf + "Oxygen data raw" + os.sep
	
	if not os.path.exists(dst):
		os.makedirs(dst)
		
		
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		shutil.copy(s, d)
	
	import AquaPlot
	AquaPlot.delFAKEJS()
	

	

def getdataswim():
	myp = os.path.dirname(sys.argv[0]) + os.sep
	main = myp.split("lib")[0] +os.sep
	temp = main + "temp" +os.sep
	lib = main + "lib" +os.sep
	result_p = main + "results" +os.sep
	pf,slopefolder,expfolder = presentfolderFunc()
	path_exp = pf.split("results")[1] 	
	mo2_ms_s = []
	mo2s = []
	r2s = []
	po2s = []
	Ubls = []
	Ucs = []
	hours = []
	
	with open(result_p + os.sep + path_exp +os.sep+ "Summary data.txt", 'r') as f:
		for i,l in enumerate(f.readlines()):
			if i >15: 
				# print l
				data = l.split(";")
				hours.append(float(data[1]))
				mo2_ms_s.append(float(data[3]))
				mo2s.append(float(data[4]))
				r2s.append(float(data[7]))
				po2s.append(float(data[11]))
				Ubls.append(float(data[26]))
				Ucs.append(float(data[25]))
				
	mo2_ms_s = np.array(mo2_ms_s)
	mo2s = np.array(mo2s)
	r2s = np.array(r2s)
	po2s = np.array(po2s)
	Ubls = np.array(Ubls)
	hours = np.array(hours)
	Ucs = np.array(Ucs)
	
	return mo2_ms_s,mo2s,r2s,po2s,Ubls,Ucs,hours
	
	
def getslopes():
	myp = os.path.dirname(sys.argv[0]) + os.sep
	main = myp.split("lib")[0] +os.sep
	temp = main + "temp" +os.sep
	lib = main + "lib" +os.sep
	result_p = main + "results" +os.sep
	pf,slopefolder,expfolder = presentfolderFunc()
	path_exp = pf.split("results")[1] 
	
	slopedir = result_p + os.sep + path_exp +os.sep+ "All Slopes"
	numfiles = len(os.listdir(result_p + os.sep + path_exp +os.sep+ "All Slopes" ))
	ExpName, ft,wt,mt,temperature,salinity, UNIXtime, Dateime = GetExperimentInfo()
	
	
	slopes = np.zeros([int(mt)+10,numfiles])
	times = np.zeros([int(mt)+10,numfiles])
	# print slopes.shape
	for i,fn in enumerate(os.listdir(slopedir )):
		with open(slopedir +os.sep+ fn, 'r') as fd:
			for ii,l in enumerate(fd.readlines()):
				if ii > 0: 
					# print i,ii
					data  = l.split(";")
					slopes[ii-1,i] = float(data[3])
					times[ii-1,i] = float(data[1])

	return slopes,times
	

# CleanSummaryData()
# datafileinit()
# CopyExperimentalInfo()
# GetTimeStartExperiment()
# datafileStop()