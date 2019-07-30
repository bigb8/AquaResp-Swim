#Aquaresp pys
import aquarespdevice as aqdev
import filehandling
import aquacalc, dataacq
# import AquaPlot
from subprocess import Popen
# Other
import os, time, datetime
import numpy as np


# import matplotlib.pyplot as plt
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
oxygenpath = mainpath + os.sep +"oxygen" + os.sep
temppath = mainpath + os.sep +"temp" + os.sep

# fn = oxygenpath + "firesting.txt"

lib_p = mainpath  + os.sep + "lib" + os.sep



	
def MeasurementPeriod(mainpath):
	# fn = oxygenpath + "firesting.txt"
	# presentfolder 
	pf,slopefolder,expfolder = filehandling.presentfolderFunc()
	

	#Datacollection when it is measuring time
	measurementperiod1 = []
	Uucs = []
	Ucs = []
	Ubls = []
	Vs = []

	timesec = []
	timeabs = []
	timeunix = []

	pO2_1,pO2_2,pO2_3,pO2_4,oxtime = ["","","","",""]
	# print pO2_1,pO2_2,pO2_3,pO2_4,oxtime

	oxtimeold = datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
	unixtime = int(time.time())
	unixtime2 = int(time.time())
	
	timestartmeasurement = datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
	timestartmeasurement2 = datetime.datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")


	print("Start Data Acquisition - MO2")
	
	while 1:
		# try:
		pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = aqdev.uniformoxygen()
		# print pO2_1.replace(",",".")
		# except:	
			# pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = [0,0,0,0,datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")]
		
		#Read swim speed
		# try:
		
		U,Uc,Ubl,V = dataacq.getflow()
	

		unixtime = int(time.time())
		# Standard sampling rate for Aquaresp is .25 second
		time.sleep(.5) 

		
		try:
			oxtime = datetime.datetime.strptime(oxtime1, "%H:%M:%S")
			oxtimeold = datetime.datetime.strptime(oxtimeold, "%H:%M:%S")
		except TypeError:
			pass
		except:
			print("Missed a time reading.")
		
		# print oxtime1,oxtimeold,oxtime
		try:
			dtime = oxtime - oxtimeold
		except TypeError:
			print( "Type error in delta time. Line 84")
		
		try:
			stime = oxtime - timestartmeasurement
		except:
			print( "Error in line 89")
		
		
		if not dtime.total_seconds() == 0:
			# samplingrate in aquaresp is to high compared to the oxygenmeter. So if there is no time difference
			# between the samples, they are not logged.

			try:
				measurementperiod1.append(float(pO2_1))
			except ValueError:
				measurementperiod1.append(float(9999))
			except:
				measurementperiod1.append(float(9998))
				
			Uucs.append(float(U))
			Ucs.append(float(Uc))
			Ubls.append(float(Ubl))
			Vs.append(float(V))
			
			timesec.append(float(stime.total_seconds()))
			timeabs.append(oxtime1)
			timeunix.append(unixtime)
			
			#Denne skal aendres
			# filehandling.ox2file(pO2_1,pO2_2,pO2_3,pO2_4,oxtime1)
			filehandling.ox2file(pO2_1,oxtime1)
			

		oxtimeold = oxtime1
		#When measurement period ends
		if filehandling.TjekPeriod() !="M":	break
		# 
		# exp = filehandling.TjekRun()
		# if not exp: break
	
	#Get measurement period duration
	duration = int(time.time()) - unixtime2
	
	#Handle save data, and MO2 Calculation etc
	numfiles = len([name for name in os.listdir(slopefolder) if os.path.isfile(os.path.join(slopefolder, name))])
	
	# print 'slopes: ', slopefolder
	with open( slopefolder + "Cycle_" + str(numfiles + 1) + ".txt",'w')	as f:
		f.write("Time;Seconds from start for linreg;Unix Time;ch1 po2;Uc;Ubl;Vc;\n")
		for ii,l in enumerate(timesec):
			f.write("%s;%s;%s;%s;%s;%s;%s;\n"% (timeabs[ii],l,timeunix[ii],measurementperiod1[ii],Ucs[ii],Ubls[ii],Vs[ii]))
	
	measurementperiod1 = np.array(measurementperiod1)
	timesec = np.array(timesec)
	
	# sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol, UNIXtime, Dateime, IsSlave = filehandling.GetExperimentInfo()
	ExpName, ft,wt,mt,temperature,salinity, UNIXtime, Dateime = filehandling.GetExperimentInfo()
	
	
	filehandling.updateLastmo2file(2,"-","-")
	
	# inuse, volume, animalmass = filehandling.readrespirometerinfo(1)	
	sectionwidth, volume, sectionheight = filehandling.readrespirometerinfo()	
	slope, intercept, rr, p_value, std_err,avgpo2,medianpo2,minpo2,maxpo2 = aquacalc.sloper(timesec,measurementperiod1)
	
	
	(aUuc,aUc,aUbl,aVS),(sdUuc,sdUc,sdUbl,sdVS) = aquacalc.flowaverager(Uucs[Uucs<999],Ucs[Uucs<999],Ubls[Uucs<999],Vs[Uucs<999])
	in_hours, in_minutes,in_seconds, in_days = filehandling.GetTimeStartExperiment()
	
	with open(temppath + "fish.txt","r") as fe:
		datatemp = fe.readlines()[1].split(";")
	animalmass = float(datatemp[0])*1e-3 #kg
	animalwidth = datatemp[1] # cm
	animalheight = datatemp[2]
	animallength = datatemp[3]
	
	
	
	avgU = aUuc
	avgUC = aUc
	avgUBL = aUbl
	avgV = aVS
	
	# MO2, beta, rRespFish = aquacalc.mo2maker(slope,float(temperature),float(salinity),760,float(animalmass),float(volume))
	MO2, beta, rRespFish, MO2wa, MH2O, MH2Owa= aquacalc.mo2maker(slope,float(temperature),float(salinity),760,float(animalmass),float(volume))
	print( '------------\n\n')
	print ( "MO2: ", str(MO2), " r-squared: ",str(rr), "Slope: ", slope,'\n')
	print('------------\n\n')
	
	filehandling.updateLastmo2file(0,MO2,rr)
	filehandling.MO2Save(timestartmeasurement2,in_hours,unixtime, MO2, slope, intercept, rr, p_value, std_err,duration,avgpo2,medianpo2,minpo2,maxpo2, maxpo2-minpo2,beta,rRespFish,in_hours, in_minutes,in_seconds, in_days,MO2wa,animalmass,beta,avgU,avgUC,avgUBL,avgV)
		
		#Create JS for data viewer
		# try:	
			# AquaPlot.fakeJSdatasource()
		
		#Create copy data for  data viewer
			# Popen(["python",  mainpath +os.sep +"lib" + os.sep +"copytoGD.py"])
		# print "Finished data handling", duration
		# except: pass
	filehandling.updateLastmo2file(1,"-","-")
	
	
	# Popen(["python", lib_p + os.sep + "Pump.py","1","0","1"])
	
	
	
def run():			

	# Firesting, Presens4, Fibox3, FNFiresting, FNFibox	= SensorMess()

	while 1:
		time.sleep(.25)
		if filehandling.TjekPeriod() =="M":
		#Initiate measurement period datacollection
			MeasurementPeriod(mainpath)
			break
run()
# Popen(["python", mainpath +os.sep +"lib" + os.sep +"copytoGD.py "])

