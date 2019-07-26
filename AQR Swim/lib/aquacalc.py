import numpy as np
import os,sys
import time
import datetime as dtt
from math import exp,log
# from scipy import stats


#Aquaresp Specific
import aquaoxygen as aqox






def normpdf(x, mu=0, sigma=1):
	u= 1.0*(x-mu)/np.abs(sigma)
	y = (1.0/(np.sqrt(2*np.pi)*np.abs(sigma)))*np.exp(-u*u/2.0)
	return y

	
	
def AquaReg(x,y):
	#Linear regression without scipy
	# a,b,r2,se_r,P = AquaReg(x,y)

	A = np.array([x, np.ones(len(x))])

	# Least Squares Regression
	lsr = np.linalg.lstsq(A.T,y)

	a = lsr[0][0]
	b = lsr[0][1] 

	regline = a*x+b

	SSres = np.sum((y - regline)**2)

	SStot = np.sum((y - np.mean(y))**2)

	r2 = 1 - SSres / SStot

	t = float(np.sqrt(r2)*np.sqrt(len(x) -2 ))/np.sqrt(1-r2)

	se_r = np.sqrt(float(1-r2)/(len(x) -2))
	se_intercept = np.sqrt(float((1-r2)*SStot)/(len(x) -2)) 
	# print a,b,r2,se_r,normpdf(t)
	return a,b,r2,se_r,normpdf(t)


#Solid blocking
#Bell & Terhune, 1970

def solidblocking(U,wf,hf,lf,hr,wr):
	#input is uncorrected speed, average width, and length of fish
	#Using an average width, taking the average width and height
	avWidth = (wf+hf)*.5
	
	T = 0.8
	lamb_da = (0.5*lf) / avWidth
	
	#Cross sectional area - assuming fish has an ellipsoid crosssection
	Afish = np.pi * wf*.5 * hf*.5
	
	#Cross sectional area of swim tunnel
	Arespirometer = hr*wr
	
	e = T*lamb_da*(float(Afish)/Arespirometer)**(3.0/2.0)
	
	# Uf: correction using average width e.g. height and width	
	Uf = U*(1 + e)

	return Uf
	

	
#MO2 - Linear Regression
#Svendsen et al, 2015. Steffensen 1989.
	
def sloper(x_time,po2):
##Calculates slope of whatever
	x = x_time
	y = po2
	#Only for positive time in measurement period
	y_samplingcorrected = y[x>0]
	x_samecorr = x[x>0]
	# slope, intercept, r_value, p_value, std_err = stats.linregress(x_samecorr,y_samplingcorrected)
	# rr,pp = stats.pearsonr(x_samecorr,y_samplingcorrected
	
	slope,intercept,r2,std_err,p_value = AquaReg(x_samecorr,y_samplingcorrected)
	
	return slope, intercept, r2, p_value, std_err,np.mean(y_samplingcorrected),np.median(y_samplingcorrected),np.min(y_samplingcorrected),np.max(y_samplingcorrected)

	
	
def mo2maker(slope,temp,salinity,patm,mfish,vresp):
# ##Calculates MO2 on basis of:
# ## slope 
# ## temperature 
# ## salinity
# ## fish size
# ## volume of respirometer
# ## barometric pressue

	pO2max, pO2maxkpa = aqox.partialpressureoxygen(temp, patm, "mmhg")
	oxysolmmhg,oxysolkpa = aqox.oxygensolubility(temp,salinity)
	
	#Get real volume of fish, assuming neutral bouyancy
	vreal = vresp - mfish
	# print vresp, mfish
	#Respirometer to fish ratio (Svendsen et al 2016)
	rRespFish = float(vreal)/mfish
	
	beta = pO2max * oxysolmmhg / 1000.0  # divide by 1000 to get mg O2 / L
	
	#Mass specific oxygen consumption of the fish. 
	MO2 = -1.0*(slope/100.0)*beta*rRespFish*3600
	
	#Whole animal oxygen consumption
	MO2wa = MO2 * mfish
	
	MH2O = MO2 / float(beta)
	MH2Owa = MO2wa / float(beta)
	
	return MO2, beta, rRespFish, MO2wa, MH2O, MH2Owa
	
	
def flowaverager(Uucs,Ucs,Ubls,Vs):
	Uucs = np.array(Uucs)
	
	Ucs = np.array(Ucs)
	Ubls  = np.array(Ubls)
	Vs = np.array(Vs)
	
	
	aUuc = np.average(Uucs)
	aUc = np.average(Ucs)
	aUbl = np.average(Ubls)
	aVS = np.average(Vs)
	
	sdUuc = np.std(Uucs)
	sdUc = np.std(Ucs)
	sdUbl = np.std(Ubls)
	sdVS = np.std(Vs)
	
	return (aUuc,aUc,aUbl,aVS),(sdUuc,sdUc,sdUbl,sdVS)
	
	
	
	
	