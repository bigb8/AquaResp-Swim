
from subprocess import Popen
import tkinter as tk
import os,sys
import numpy as np

myp = os.path.dirname(sys.argv[0]) + os.sep
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
pump_p = lib + os.sep + "pump control" +os.sep



def saveRelay():
	# from scipy import stats
	
	global listbox
	
	# listbox.curselection()
	
	
	with open(temp + "Relay.txt", "w") as f:
		f.write(str(listbox.curselection()[0]))
		f.write(";")
		f.write(listbox.get(listbox.curselection()))
		
		
	print("Data saved: ", listbox.get(listbox.curselection()))
	
def testRelay():
	
	
	Popen(["python", lib + os.sep + "Pump.py","1","0","1"])
	


root = tk.Tk()
top_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)
mid_frame = tk.Frame(root)


top_frame.pack(side="top", fill="x")
mid_frame.pack(side="top", fill="x")
bottom_frame.pack(side="top", fill="x")

# top_frame.pack(side="top", fill="x",expand=False)


B3 = tk.Button(mid_frame, text ="Test relay", command = testRelay,bg="SteelBlue3",height =2, width = 30)
B3.pack()





B1 = tk.Button(bottom_frame, text ="Save", command = saveRelay,bg="PaleGreen3",height =3, width = 30)
B2 = tk.Button(bottom_frame, text ="Close window", command = root.destroy,bg="tomato2")



B2.pack(side="bottom",anchor="n")
B1.pack(anchor="n",side="bottom")



root.wm_title("Flush pump relay configuration - AQ3 Swim")
root.geometry('{}x{}'.format(600, 300))

label1 = tk.Label(top_frame,text="Choose relay")
label1.pack(side="left")
L3 = tk.Label(top_frame, text ="Off", bg="red3")
# L3.pack(anchor="e")
L3.pack(side="left")


global listbox
listbox = tk.Listbox(top_frame)
listbox.pack(side="bottom",fill="x")


label2 = tk.Label(mid_frame,text="O2: ")
label2.pack(side="left")

for item in ["Flush box 1 channel", "Flush box 4 ch #1", "Flush box 4 ch #2", "Flush box 4 ch #3", "Flush box 4 ch #4", "Loligo LOL-DAQ","MMC USB/PMD 1208LS #ch1"]:
    listbox.insert(tk.END, item)


