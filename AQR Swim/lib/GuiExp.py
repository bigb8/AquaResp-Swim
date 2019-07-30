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
		
		lab2 = Tk.Label(master, text = "Right click to change plots. Left click to move cross")
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



		self.f = Figure(figsize=(5, 4), dpi=100,frameon=False)
		self.a = self.f.add_subplot(111)
		self.a1 = self.a.twinx()
		
		t = np.arange(0.0, 3.0, 0.01)
		s = np.sin(2*np.pi*t)
		
		self.line1, = self.a.plot(t,s,'b.')
		self.line2, = self.a1.plot(t,s,'r.')
		
		# self.clicklim = clicklim
		self.horizontal_line = self.a1.axhline(y=0, color='y', alpha=0.5)
		self.v_line = self.a1.axvline(x=1, color='y', alpha=0.5)
		

		self.f2 = Figure(figsize=(5, 4), dpi=100,frameon=False)
		self.a2 = self.f2.add_subplot(111)
		
		
		self.line3, = self.a2.plot(t,s,'b.')
		self.horizontal_line2 = self.a2.axhline(y=0, color='g', alpha=0.5)
		
		self.v_line2 = self.a2.axvline(x=1, color='g', alpha=0.5)
		# a tk.DrawingArea
		self.canvas = FigureCanvasTkAgg(self.f, master=myframe1)
		self.canvas2 = FigureCanvasTkAgg(self.f2, master=myframe2)
		self.canvas.draw()
		# self.canvas.show()
		# self.canvas2.show()
		self.canvas2.draw()

		self.canvas.get_tk_widget().pack(side=Tk.LEFT)
		self.canvas2.get_tk_widget().pack()

		# toolbar = NavigationToolbar2TkAgg(canvas, root)
		# toolbar.update()
		# canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
		# frame.pack()


		
		def changeplot1(toggle):
			mo2_ms_s,mo2s,r2s,po2s,Ubls,Ucs,hours=filehandling.getdataswim()
			
			if toggle: self.plot1 += 1
			
			if self.plot1 == 4: self.plot1 = 1
			
			if self.plot1 == 1:
				# self.a1.cla()
				self.a1.plot(hours,r2s,'r.')
	
				self.line1.set_data(hours,mo2_ms_s)
				self.line2.set_data(hours,r2s)
				
				
				ax = self.canvas.figure.axes[0]
				ax1 = self.canvas.figure.axes[1]
				self.canvas.figure.axes[1].set_yticks([0,.5,.8,.9,1])
				
				ax.set_xlim(0, hours.max()*1.2)
				
				ax.set_xlabel("Hours from start")
				ax.set_ylabel("Mass specific MO2 (mg/h/kg)")
				
				ax.set_ylim(mo2_ms_s.min() - 50, mo2_ms_s.max()+50) 
				ax1.set_ylim(0,1.01) 
				
				ax1.set_ylabel('R2', color='r')
				self.f.tight_layout()
				
				
			elif self.plot1 == 2:
				
				self.line1.set_data(po2s,mo2_ms_s)
				
				ax = self.canvas.figure.axes[0]
				ax.set_xlim(0, 105)
				ax.set_xlabel("Air sat. %")
				ax.set_ylabel("Mass specific MO2 (mg/h/kg)")
				ax.set_ylim(0, mo2_ms_s.max()*1.2) 
				self.f.tight_layout()	
				
				self.a1.cla()
				self.canvas.figure.axes[1].set_yticks([])
				self.canvas.figure.axes[1].set_ylabel("",color="w")
				self.horizontal_line = self.a1.axhline(y=self.y1, color='y', alpha=0.5)
				self.v_line = self.a1.axvline(x=self.x1, color='y', alpha=0.5)

			elif self.plot1 == 3:
				self.line1.set_data(mo2_ms_s,r2s)
				self.line2.set_data(hours,r2s)
				ax = self.canvas.figure.axes[0]
				ax.set_xlim(mo2_ms_s.min()*.8, mo2_ms_s.max()*1.2)
				ax.set_ylabel("R2")
				ax.set_xlabel("Mass specific MO2 (mg/h/kg)")
				ax.set_ylim(0, 1.01) 
				self.f.tight_layout()
				
			self.canvas.draw()
				
				
		def changeplot2(toggle):
			mo2_ms_s,mo2s,r2s,po2s,Ubls,Ucs,hours=filehandling.getdataswim()
			slopes,times= filehandling.getslopes()
			
			if toggle: self.plot2 += 1
			
			if self.plot2 == 2: self.plot2 = 1
			
			if self.plot2 == 1:
				# self.line3, =self.a2.plot(Ubls,mo2_ms_s,'k.',alpha=1)
				
				self.line3.set_data(Ubls,mo2_ms_s)
				ax = self.canvas2.figure.axes[0]
				ax.set_xlim(0, Ubls.max()*1.2)
				ax.set_xlabel("Body lengths per second")
				ax.set_ylabel("Mass specific MO2 (mg/h/kg)")
				ax.set_ylim(mo2_ms_s.min() - 50, mo2_ms_s.max() + 50) 
				self.f2.tight_layout()
				

				
			# elif self.plot2 == 2:
				# try:
					# for ik, sl in enumerate(slopes[0,:]):
						# self.a2.plot(times[:,ik],slopes[:,ik],'k')

					# ax = self.canvas2.figure.axes[0]
					# ax.set_ylim( np.min(slopes[:,ik])*.9,np.max(slopes[:,ik])*1.1) 
					# ax.set_xlim(0, np.max(times[ik]))
					# ax.set_xlabel("Air sat")
					# ax.set_ylabel("Time in measurement period")
				
				# except UnboundLocalError:
					# return
			self.canvas2.draw()
					
		def on_click(event):
			# print event.inaxes
			# print event.inaxes
			x = event.xdata
			y = event.ydata
			
			self.x1 = x
			self.y1 = y
			if event.inaxes is not None:
			
				# print event.xdata, event.ydata
				if event.button == 3: 
					try:
						changeplot1(True)
					except ValueError:
						print(" Wait for first measurement")
				if event.button == 1: 
					xlim0, xlim1 = self.a1.get_xlim()
					ylim0, ylim1 = self.a1.get_ylim()
					# print self.a1.get_ylim(), self.a.get_ylim(),self.a.xmin()
					if x <= xlim0+(xlim1-xlim0):
						self.horizontal_line.set_ydata(y)
						self.v_line.set_xdata(x)

						self.canvas.draw()
					
					# self.a.plot()
				
			else:
				print( 'Click in the window')

		def on_click2(event):
			# print event.button, "canvas 2"
			# print event.inaxes
			x = event.xdata
			y = event.ydata
			
			self.x2 = x
			self.y2 = y
			if event.inaxes is not None:
				# print event.xdata, event.ydata
				if event.button == 3: 
					try:
						changeplot2(True)
					except ValueError:
						print (" Wait for first measurement")
				
				
				if event.button == 1: 
					xlim0, xlim1 = self.a2.get_xlim()
					ylim0, ylim1 = self.a2.get_ylim()
					# print self.a1.get_ylim(), self.a.get_ylim(),self.a.xmin()
					if x <= xlim0+(xlim1-xlim0):
						self.horizontal_line2.set_ydata(y)
						self.v_line2.set_xdata(x)

						self.canvas2.draw()
			else:
				print('Clicked ouside axes bounds but inside plot window')


		def on_key_event(event):
			print('you pressed %s' % event.key)
			# key_press_handler(event, canvas, toolbar)
			
		def update():
			if self.endexperiment == 1: return
			if self.plot1 == 0: self.plot1 = 1
			if self.plot2 == 0: self.plot2 = 1
			
			try:
				changeplot2(False)
				changeplot1(False)
			except ValueError:
				pass
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
			
			# if self.endexperiment:

				# print "HERE!?"
				# exit(0)
				
			job_function()


		def job_function():
			self.ccc = thr.Timer(1, update).start()
			
			
		self.canvas.mpl_connect('key_press_event', on_key_event)
		self.canvas2.mpl_connect('key_press_event', on_key_event)
		self.canvas.callbacks.connect('button_press_event', on_click)
		self.canvas2.callbacks.connect('button_press_event', on_click2)
		
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
		# Tk.mainloop()
		# If you put root.destroy() here, it will cause an error if
		# the window is closed with the window manager.






root = Tk.Tk()
my_gui = ExperimentRunning(root)
root.mainloop()