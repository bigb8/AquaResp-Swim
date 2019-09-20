# Graphing
import matplotlib.pyplot as plt
import threading as thr
from subprocess import Popen
# import matplotlib
# matplotlib.rc('axes',edgecolor='green')
# style="red.Horizontal.TProgressbar",

# import ttk
import os, sys,time
import matplotlib
# matplotlib.use('TkAgg')

import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

if sys.version_info[0] < 3:
    # import Tkinter as Tk
	import Tkinter as Tk
	# from Tkinter import *
else:
	import tkinter as Tk
	from tkinter import ttk



myp = os.path.dirname(sys.argv[0]) + os.sep
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
result_p = main + "results" +os.sep

#Get experimental folder
import filehandling
pf,slopefolder,expfolder = filehandling.presentfolderFunc()


# Looping information
# Get flush wait measure status
period = filehandling.TjekPeriod()

#Duration of experiment
in_hours, in_minutes,in_seconds, in_days =	filehandling.GetTimeStartExperiment()



#Buttons: End experiment. Note
class ExperimentRunning:
	def __init__(self, master):
	
		self.plot1 = 0
		self.plot2 = 0
		self.endexperiment = False
		
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		
		def updatelabel():
			# V = dataacq.returnvoltage()
			try:
				print(1)
				# self.labelV["text"] = str('{0:.2f}'.format(V))
			except:
				pass
			else:
				print(2)
				# job_function()


		self.master = master

		master.wm_title("Experiment in progress - AquaResp Swim")
	# root.geometry('{}x{}'.format(1000, 600))

		myframe = Tk.Frame(master)
		
		lab2 = Tk.Label(master, text = "Hello, you can find the plots in the plots.html file in the Aquaresp folder")
		myframe1 = Tk.Frame(myframe)
		myframe2 = Tk.Frame(myframe)
		lab2.pack(anchor="nw")

		status = Tk.Frame(master)
		controls = Tk.Frame(master)


		# myframe.pack(side="top", fill="x")
		myframe.pack(side="top",fill="x")
		
		myframe1.pack(side="left")
		myframe2.pack(side="right")

		status.pack(side="right", fill="both")
		controls.pack(side="left", fill="y")


		s = ttk.Style()
		s.theme_use('clam')
		s.configure("red.Horizontal.TProgressbar", foreground='black', background='red')
		s.configure("blue.Horizontal.TProgressbar", foreground='black', background='blue')
		s.configure("green.Horizontal.TProgressbar", foreground='black', background='green')


		self.lab = Tk.Label(status,text = "Period status, Flush - Wait - Measure: ")
		self.pfl = ttk.Progressbar(status,style="red.Horizontal.TProgressbar", orient=Tk.HORIZONTAL, length=150, mode='determinate',max = 1000)
		self.pwa = ttk.Progressbar(status,style="blue.Horizontal.TProgressbar", orient=Tk.HORIZONTAL, length=100, mode='determinate',max = 1000)
		self.pme = ttk.Progressbar(status,style="green.Horizontal.TProgressbar", orient=Tk.HORIZONTAL, length=150, mode='determinate',max = 1000)

		self.lab.pack(side = "left")
		self.pme.pack(side="right")# statusbar = ttk.StatusBar(status)
		self.pwa.pack(side="right")# statusbar = ttk.StatusBar(status)
		self.pfl.pack(side="right")# statusbar = ttk.StatusBar(status)



		
			
		def update():
			if self.endexperiment == 1: return
			
			#Present period timing
			starttime, durationperiod, timeleft = filehandling.GetperiodStart()
			period = filehandling.TjekPeriod()
			# print period
			
			
		
			if period == "F":
				sw = 0
				sm = 0
				sf = float(timeleft)/float(durationperiod)
				# print sf
			elif period == "W":
				sw = float(timeleft)/float(durationperiod)
				sm = 0
				sf = 1
			elif period == "M":
				sw = 1
				sm = float(timeleft)/float(durationperiod)
				sf = 1
				
			# Show progress bar + status bar
			
			statusstring = "Period status, Flush "+ str("%.1f" % (sf*100)) + "% - Wait: "+str("%.1f" % (sw*100))+"% - Measure: " +str("%.1f" % (sm*100)) +"%"
			
			self.pfl['value']= sf*1000
			self.pwa['value']= sw*1000
			self.pme['value']= sm*1000
			self.lab['text'] = statusstring
							
			job_function()


		def job_function():
			self.ccc = thr.Timer(1, update).start()
			
			
	
		
		def startevent():
			Popen(["python", lib + "eventexperiment.py"])
		
		def quit():
			print( "--------------------------")
			self.endexperiment = True
			print( "Stopping Experiment Safely")
			print( "--------------------------")
			time.sleep(1)
			print( "Turning on flush pump\n\n\n")
			# Flush on
			Popen(["python", lib + os.sep + "Pump.py","1","0","0","0"])
			
			time.sleep(1)
			print("copying files\n\n\n")
			# copy temp files
			
			time.sleep(3)
			print( "Thank you for using AquaResp - and good bye\n\n\n")
			# self.ccc.stop()
			# end
			root.quit()     # stops mainloop
			root.destroy()  # this is necessary on Windows to prevent
							# Fatal Python Error: PyEval_RestoreThread: NULL tstate

		# button = Tk.Button(master=root, text='Quit', command=_quit)
		button1 = Tk.Button(master=controls, text='Stop Experiment', command=quit,bg="red")
		button2 = Tk.Button(master=controls, text='Programmable event', command=startevent,bg="cornflower blue")
		button2.pack(side=Tk.LEFT)
		button1.pack(side=Tk.LEFT)
		# button.pack(side=Tk.BOTTOM)
		root.resizable(0,0)
		job_function()






root = Tk.Tk()
my_gui = ExperimentRunning(root)
root.mainloop()