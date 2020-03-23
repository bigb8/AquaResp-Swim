
#
import tkinter as tk
import time 
import os,sys,subprocess
import ctypes
import shutil

##
myp = os.path.dirname(sys.argv[0]) + os.sep


###


root = tk.Tk()
root.title("AquaInstall")
w1 = tk.Label(root, text="Flush installation control",font='Helvetica 10 bold')

#Variables for label updating
v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()

#Titles, left justification
i1 = tk.Label(root, text="...",textvariable=v1)

#Buttons
global clewbit, mccbit
clewbit = "64"
mccbit = "64"

def bitter32():
	global clewbit
	clewbit = "32"
	b12.config(bg="pink")
	b11.config(bg="lightgreen")

		
def bitter64():
	global clewbit
	clewbit = "64"
		
	b11.config(bg="pink")
	b12.config(bg="lightgreen")
	
	
def bittermcc32():
	global mccbit
	mccbit = "32"
	b22.config(bg="pink")
	b21.config(bg="lightgreen")

		
def bittermcc64():
	global mccbit
	mccbit = "64"
		
	b21.config(bg="pink")
	b22.config(bg="lightgreen")



b11 = tk.Button(root, text="32-bit", width=8,command=bitter32)
b12 = tk.Button(root, text="64-bit", width=8, command=bitter64)

w1.grid(row=0,column=0,sticky="w")
i1.grid(row=1,columnspan=3,sticky="we")

b12.grid(row = 2,column=0,sticky="w")
b11.grid(row = 2,column=2,sticky="e")

w2 = tk.Label(root, text="ADC Installation control",font='Helvetica 10 bold')
i2 = tk.Label(root, text="...",textvariable=v2)

b21 = tk.Button(root, text="32-bit", width=8,command=bittermcc32)
b22 = tk.Button(root, text="64-bit", width=8, command=bittermcc64)

w2.grid(row=3,column=0,sticky="w")

b22.grid(row = 5,column=0,sticky="w")
b21.grid(row = 5,column=2,sticky="e")


i2.grid(row=4,columnspan=3,sticky="we")

#Libraries
def numpyy():
	subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade","pip"])
	try:
		import numpy as np
		b31.config(bg="lightgreen")	
		b31.config(text ="OK")	
		
	except ImportError:
		subprocess.call([sys.executable, "-m", "pip", "install", "numpy"])

def bokehh():
	subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade","pip"])
	try:
		import bokeh
		b32.config(bg="lightgreen")
		b32.config(text ="OK")	
	except ImportError:
		subprocess.call([sys.executable, "-m", "pip", "install", "bokeh"])

		
def mcculww():
	subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade","pip"])
	try:
		import mcculw
		b33.config(bg="lightgreen")
		b33.config(text ="OK")	
	except ImportError:
		subprocess.call([sys.executable, "-m", "pip", "install", "mcculw"])			

def scipyy():
	subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade","pip"])
	try:
		import scipy
		b34.config(bg="lightgreen")
		b34.config(text ="OK")	
	except ImportError:
		subprocess.call([sys.executable, "-m", "pip", "install", "scipy"])		
		
		
b31 = tk.Button(root, text="Numpy", width=8,command=numpyy)
b32 = tk.Button(root, text="Bokeh", width=8,command=bokehh)
b33 = tk.Button(root, text="mcculw", width=8,command=mcculww)
b34 = tk.Button(root, text="Scipy", width=8,command=scipyy)
w3 = tk.Label(root, text="Libraries",font='Helvetica 10 bold')
w3.grid(row=6,column=0,sticky="w")

b31.grid(row = 7,columnspan=4,sticky="we")
b32.grid(row = 8,columnspan=4,sticky="we")
b33.grid(row = 9,columnspan=4,sticky="we")
b34.grid(row = 10,columnspan=4,sticky="we")

# FlushDLL = ctypes.WinDLL(myp + os.sep + "dlls" + os.sep + "cbw32.dll")

mccbitold = "0"
clewbitold = "0"

def dllcheck():
	global clewbit,mccbit,clewbitold,mccbitold,testpass1,testpass2
	#Tests	
	
	if not clewbit == clewbitold:
		clewbitold = clewbit
		try:
			if clewbit == "32":
				FlushDLL = ctypes.WinDLL(myp + os.sep + "dlls" + os.sep + "USBaccess32.dll")
				shutil.copyfile(myp + os.sep + "dlls" + os.sep + "USBaccess32.dll",myp.split("AQR")[0] +os.sep +"AQR Swim"+ os.sep + "lib" + os.sep+"pump control"+os.sep + "flush.dll")
					
				
			elif clewbit == "64":
				FlushDLL = ctypes.WinDLL(myp + os.sep + "dlls" + os.sep + "USBaccess64.dll")
				shutil.copyfile(myp + os.sep + "dlls" + os.sep + "USBaccess64.dll",myp.split("AQR")[0] +os.sep +"AQR Swim"+ os.sep + "lib" + os.sep+"pump control"+os.sep + "flush.dll")
			testpass1 = True
		except OSError:
			testpass1 = False
		
	
	
	if not mccbit == mccbitold:	
		mccbitold = mccbit
		try:
			if mccbit == "32":
				FlushDLL = ctypes.WinDLL(myp + os.sep + "dlls" + os.sep + "cbw32.dll")
				shutil.copyfile(myp + os.sep + "dlls" + os.sep + "cbw32.dll",myp.split("AQR")[0] +os.sep +"AQR Swim"+ os.sep + "lib" + os.sep + "1208.dll")
				# print("d")
			elif mccbit == "64":
				FlushDLL = ctypes.WinDLL(myp + os.sep + "dlls" + os.sep + "cbw64.dll")
				shutil.copyfile(myp + os.sep + "dlls" + os.sep + "cbw64.dll",myp.split("AQR")[0] +os.sep +"AQR Swim"+ os.sep + "lib" + os.sep + "1208.dll")
			
			testpass2 = True
		except OSError:
			testpass2 = False
		
	
	
	
	
	
	
	
	if testpass1:
		v1.set("OK!")
		i1.config(bg="lightgreen")
	else:
		v1.set("Failed")
		i1.config(bg="pink")
		

	if testpass2:
		v2.set("OK!")
		i2.config(bg="lightgreen")
	else:
		v2.set("Failed")
		i2.config(bg="pink")	
	
	root.after(100, dllcheck)
	


dllcheck()


root.mainloop()