

import datetime
import threading as thr
import tkinter as tk
from time import ctime, strftime
import os,sys
import numpy as np
from subprocess import Popen

#AquaResp Swim related packs
# import aquaread
import externalhandling,filehandling
import dataacq
import aquacalc


# myp = os.path.realpath(__file__).split("main.")[0]
# temp = myp.split("lib")[0] + os.sep + "temp" + os.sep

myp = os.path.dirname(sys.argv[0]) + os.sep
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
pump_p = lib + os.sep + "pump control" +os.sep
results = main  + "results" +os.sep

with open(temp + "experimentstarted.txt", 'w') as f: f.write("0")

# print(Fore.WHITE + Back.RED  + 'some red text')


class Swimmy(tk.Frame):
	
	def __init__(self, parent, *args, **kwargs):
		
		
		
		def DAQgui():
			def startguivol():
				thread = thr.Thread(target = exec(compile(open(myp+"guivoltage.py").read(), myp+"guivoltage.py", 'exec')) ).start()
			def saveDAQ():
				# from scipy import stats
				
				global listbox			
				with open(temp + "DAQ.txt", "w") as f:
					f.write(str(listbox.curselection()[0]))
					f.write(";")
					f.write(listbox.get(listbox.curselection()))
					
					
				print( "Data saved: ", listbox.get(listbox.curselection()))
				
			# def statusrelay():
				


			global L3
			root = tk.Tk()
			top_frame = tk.Frame(root)
			bottom_frame = tk.Frame(root)
			mid_frame = tk.Frame(root)


			top_frame.pack(side="top", fill="x")
			mid_frame.pack(side="top", fill="x")
			bottom_frame.pack(side="top", fill="x")

			# top_frame.pack(side="top", fill="x",expand=False)


			B3 = tk.Button(mid_frame, text ="Test DAQ", command = startguivol,bg="SteelBlue3",fg="Black",height =2, width = 30)
			B3.pack()


			B1 = tk.Button(bottom_frame, text ="Save", command = saveDAQ,bg="PaleGreen3",height =3, width = 30)
			B2 = tk.Button(bottom_frame, text ="Close window", command = root.destroy,bg="tomato2")

			B2.pack(side="bottom",anchor="n")
			B1.pack(anchor="n",side="bottom")


			root.wm_title("DAQ for Motor readout configuration - AQ3 Swim")
			root.geometry('{}x{}'.format(300, 300))

			label1 = tk.Label(top_frame,text="Choose DAQ")
			label1.pack(side="left")

			global listbox
			listbox = tk.Listbox(top_frame)
			listbox.pack(side="bottom",fill="x")


			label2 = tk.Label(mid_frame,text="O2: ")
			label2.pack(side="left")

			for item in ["Easy input ch1", "Easy input ch2", "MMC USB/PMD 1208LS CH1", "Loligo LOL-DAQ"]:
				listbox.insert(tk.END, item)

			
			
			with open(temp + "DAQ.txt", "r") as f:	
				id = f.readlines()[0].split(";")[0]
				listbox.select_set(int(id))

		
		def relaygui():
	
			def saveRelay():
				# from scipy import stats
				
				global listbox			
				with open(temp + "Relay.txt", "w") as f:
					f.write(str(listbox.curselection()[0]))
					f.write(";")
					f.write(listbox.get(listbox.curselection()))
					
					
				print("Data saved: ", listbox.get(listbox.curselection()))
				
			# def statusrelay():
			def testRelay():
				global L3
				# Popen(["python", lib + os.sep + "Pump.py","1","0","1"])
				# stat = externalhandling.pumpstatus()
				stat = externalhandling.testpump()
				try:
					if stat == "1":
						L3.configure(bg="green")
						L3.configure(text="On")
					elif stat =="0":
						L3.configure(bg="red")
						L3.configure(text="Off")
				except:
					pass
					
				# print stat
				


			global L3
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

			with open(temp + "Relay.txt", "r") as f:	
				id = f.readlines()[0].split(";")[0]
				listbox.select_set(int(id))
				
		def O2GUI():
			def saveO2sens():		
				global listbox
				
				# listbox.curselection()
				try:
					with open(temp + "O2 sensor.txt", "w") as f:
						f.write(str(listbox.curselection()[0]))
						f.write(";")
						f.write(listbox.get(listbox.curselection()))
				except IndexError:
					print(Fore.WHITE + Back.RED +"Error: Choose sensor on above list")
					print(Fore.RESET + 	Back.RESET)
					return
					
				# print "Data saved: ", listbox.get(listbox.curselection())
				print("Data saved: " + listbox.get(listbox.curselection()))
				


			root = tk.Tk()
			top_frame = tk.Frame(root)
			bottom_frame = tk.Frame(root)
			mid_frame = tk.Frame(root)


			top_frame.pack(side="top", fill="x")
			mid_frame.pack(side="top", fill="x")
			bottom_frame.pack(side="top", fill="x")
			B1 = tk.Button(bottom_frame, text ="Save and Check sensor", command = saveO2sens,bg="PaleGreen3",height =3, width = 30)
			B2 = tk.Button(bottom_frame, text ="Close window", command = root.destroy,bg="tomato2")

			B2.pack(side="bottom",anchor="n")
			B1.pack(anchor="n",side="bottom")


			root.wm_title("Oxygen sensor setup - AQ3 Swim")
			root.geometry('{}x{}'.format(300, 250))

			label1 = tk.Label(top_frame,text="Choose sensor")
			label1.pack(side="left")

			global listbox
			listbox = tk.Listbox(top_frame)
			listbox.pack(side="bottom")


			label2 = tk.Label(mid_frame,text="O2: ")
			label2.pack(side="left")

			for item in ["Firesting - Channel 1", "Firesting - Channel 2", "Firesting - Channel 3", "Firesting - Channel 4", "Firesting - Small thing", "Presens Fibox 3"]:
				listbox.insert(tk.END, item)
			
			with open(temp + "O2 sensor.txt", "r") as f:	
				id = f.readlines()[0].split(";")[0]
				listbox.select_set(int(id))
		
		
		
		def FlowCalGUI():
			
			def startguivol():
				thread = thr.Thread(target = exec(compile(open(myp+"guivoltage.py").read(), myp+"guivoltage.py", 'exec')) ).start()
			
			def saveflow():
				global T,T2
				Voltage = T2.get("0.0",tk.END)
				Flow = T.get("0.0",tk.END)
				Vs = []
				Us = []
								
				try:
					with open(temp + "FlowVolRaw.txt","w") as f:
						f.write("Voltage;Flow;\n")
						for i,n in enumerate(Voltage.split(";")):
							
							#checking if emptystring
							try:
								float(n)
								v = Voltage.split(";")[i]
								u = Flow.split(";")[i]
								Vs.append(float(v))
								Us.append(float(u))
								
								print(v,u)
							except:
								print("End of cal data.\n\n\n\n")
								break
						
							f.write("%s;%s;\n" % (Voltage.split(";")[i],Flow.split(";")[i]))
							
						#Converting to numpy arrays
						Vs = np.array(Vs)
						Us = np.array(Us)
						
						
						
						#Calibration curve
						# slope, intercept, r_value, p_value, std_err = aquacalc.aq(Vs,Us)
						
						slope,intercept,r2,std_err,p_value = aquacalc.AquaReg(Vs,Us)
						
						
						print("Voltages: ", Vs,"\nFlows : ", Us,"\n")
						
						
					print("Flow calibration: Slope: ", slope, " Intercept: ", intercept, "Rsq: ", r2, "S.E.: ", std_err)
					
					# print Fore.RESET + 	Back.RESET
					
					with open(temp + "flowcal.txt","w") as f:
						f.write("Slope;Intecept;P value of slope;standard error;R squared;\n")
						f.write("%s;%s;%s;%s;%s;" % (slope, intercept, p_value, std_err,r2))
						
					
					print("Data saved: ", temp + "flowcal.txt")
				
				except ValueError:
					print("Error: Check that you have equal number of voltages and flow measurements")
					
				except RuntimeWarning:
					print("Error: Non number detected")
					


			root = tk.Tk()
			global T,T2

						
			B1 = tk.Button(root, text ="Save information", command = saveflow,bg="PaleGreen3",height =3, width = 30)

			B2 = tk.Button(root, text ="Close window", command = root.destroy,bg="tomato2")
			B22 = tk.Button(root, text ="Voltage readings", command = startguivol )
			B2.pack(side="bottom",anchor="n")
			B22.pack(anchor="n")
			B1.pack(anchor="n",side="bottom")

			root.wm_title("Flow calibration measurements - AQ3 Swim")
			root.geometry('{}x{}'.format(800, 300))

			top_frame = tk.Frame(root)
			bottom_frame = tk.Frame(root, background="yellow")


			top_frame.pack(side="top", fill="x",expand=False)
			bottom_frame.pack(side="bottom", fill="both", expand=True)
			
			S = tk.Scrollbar(bottom_frame)
			T = tk.Text(bottom_frame, height=4, width=50)

			S2 = tk.Scrollbar(bottom_frame)
			T2 = tk.Text(bottom_frame, height=4, width=50)
			
			label1 = tk.Label(top_frame,text="Voltage, V. Use semicolon separation e.g. 1;2;3;4;5;")
			label2 = tk.Label(top_frame,text="Flow, cm/s. Use semicolon separation e.g. 0.1;0.2;0.3;0.4;0.5;")

			label1.pack(side="left")
			label2.pack(side="right")

			S.pack(side="right", fill="y")
			T.pack(side="right", fill="y")


			S2.pack(side="right", fill="y")
			T2.pack(side="left", fill="y")

			S.config(command=T.yview)
			T.config(yscrollcommand=S.set)

			S2.config(command=T2.yview)
			T2.config(yscrollcommand=S2.set)
			
						
			vol = ""
			val = ""
			if os.path.isfile(temp + "FlowVolRaw.txt"):
				with open(temp + "FlowVolRaw.txt","r") as f:
					for i,l in enumerate(f.readlines()):
						if i >0:
							vol = vol + l.split(";")[0] + ";"
							val = val + l.split(";")[1] + ";"
								
			
			
			T2.insert(tk.END,vol)
			T.insert(tk.END,val)

			
		
		def job_function():
			# global checking
			ccc = thr.Timer(.5, checkbeforestart)
			# ccc.daemon = True
			ccc.start()
			
			
			
		def checkbeforestart():
			self.td.set(ctime())
				
				
			with open(temp + "experimentstarted.txt", 'r') as f:
				if f.readline() =='1':
					return
				# LoadLoad()		
				#Bottom part with buttons
				# O2 check
				
			if os.path.isfile(temp + "O2 sensor.txt"):
						
				self.O2stat["text"]= "O2: "
				self.B3["fg"] = "green4"
				
				
				#Get current O2
				pO2_1,pO2_2,pO2_3,pO2_4,oxtime = dataacq.getO2()
				
				
				self.O2stat["text"]= "Sensor Chosen. O2: " + str(pO2_1) + " % air sat."
				
				o2_tjek = 1
			else:
				self.O2stat["text"]= "No sensor registered"
				self.B3["fg"] = "red1"
				
				o2_tjek = 0
				
			#Checking whether flow calibration is completed
			if os.path.isfile(temp + "flowcal.txt"):
				with open(temp + "flowcal.txt","r") as fc:
					reads = fc.readlines()[1].split(";")
							
				self.Ustat["text"] = "Flow calibrated: Slope: " + str('{0:.2f}'.format(float(reads[0]))) + " Intercept: "+ str('{0:.2f}'.format(float(reads[1]))) + " rsq: " + str('{0:.2f}'.format(float(reads[-2])))
				self.B4["fg"] = "green4"
				fc_tjek = 1
			else:
				self.Ustat["text"] = "Flow not calibrated"
				self.B4["fg"] = "red1"
				fc_tjek = 0

			
			def tjekker(li):
				for ii in li:
					if ii.get() =="": 
						ii["bg"] = "light pink"
					else:
						ii["bg"] = "snow"

						
			if os.path.isfile(temp + "Relay.txt"):			
				stat = externalhandling.pumpstatus()
				if stat =="0":
					stat = "On"
				else:
					stat = "Off"
				self.Relaystat["text"] = "Relay OK. Right click to test. Status: Flushing " + stat
				self.B5["fg"] = "green4"
				r_tjek = 1
			else:
				self.Relaystat["text"] = "Flow not calibrated"
				self.B5["fg"] = "red1"
				r_tjek = 0
			
			
			def tjekker(li):
				for ii in li:
					if ii.get() =="": 
						ii["bg"] = "light pink"
					else:
						ii["bg"] = "snow"
						
			if os.path.isfile(temp + "DAQ.txt"):			
				# stat = externalhandling.pumpstatus()		
				self.B6["fg"] = "green4"			
				# V = dataacq.returnvoltage()
				# self.MotorReadstat["text"] = "Motor input registered. V: " + str('{0:.2f}'.format(V))
				self.MotorReadstat["text"] = "Motor input saved."
								
				r_tjek = 1
			else:
				self.MotorReadstat["text"] = "Motor input not registered"
				self.B6["fg"] = "red1"
				r_tjek = 0
			
			
			def tjekker(li):
				for ii in li:
					if ii.get() =="": 
						ii["bg"] = "light pink"
					else:
						ii["bg"] = "snow"
				
			expbox = [self.expname,self.temperature,self.salinity,self.flush,self.wait,self.measure]
			respbox = [self.respvol,self.swinsecW,self.swinsecH]
			fishbox = [self.fishmass,self.fishW,self.fishH,self.fishL]
			
			tjekker(expbox)
			tjekker(respbox)
			tjekker(fishbox)
						
			
			job_function()
			

		def StartExperiment():
			print("Initiating experiment")
			filehandling.SetRun(str(1))
			# global checking
			# checking.kill()
			with open(temp + "experimentstarted.txt", 'w') as f: f.write("1")
			
			
			# Save data
			SaveSave()
			
			# Initiate experiment
			
			#Create folder
			en =  self.expname.get()
			ep = results + en +"_"  + str(datetime.datetime.now().strftime("%d %B %Y %H%M"))
			
			if not os.path.exists(ep):
				os.makedirs(ep)
			
			with open(temp + "presentfolder.txt", "w") as f:
				f.write(ep)
			
			mf = self.fishmass.get()
			lf = self.fishL.get()
			hf = self.fishH.get()
			wf = self.fishW.get()
						
			vr = self.respvol.get()
			vw = self.swinsecW.get()
			vh = self.swinsecH.get()
			
			tf = self.flush.get()
			tw = self.wait.get()
			tm = self.measure.get()
			
			# Experiment GUI
			Popen(["python", lib + os.sep +"GuiExp.py"])
			
			Popen(["python", lib + os.sep +"guiU.py"])
			
			filehandling.SetTimeStartExperiment()
			filehandling.datafileinit()
			
			
			Popen(["python", lib + os.sep +"intermittentflow.py ", str(tf),str(tw),str(tm)])
			root.destroy()
			
			


			
		def SaveSave():
			#Experiment box saving
			with open(temp + "experiment.txt","w") as fe:
				fe.write(("%s;%s;%s;%s;%s;%s;\n") % ("Experiment name","Temperature","Salinity","Flushing time", "Wait time", "Measurement time"))
				fe.write(("%s;%s;%s;%s;%s;%s;") % (self.expname.get(),self.temperature.get(),self.salinity.get(),self.flush.get(),self.wait.get(),self.measure.get()))
	
			#Respirometer box saving
			with open(temp + "respirometer.txt","w") as fe:
				fe.write(("%s;%s;%s;\n") % ("Volume","Section Width", "Section Height"))
				fe.write(("%s;%s;%s;") % (self.respvol.get(),self.swinsecW.get(),self.swinsecH.get()))

			#Fish box saving
			with open(temp + "fish.txt","w") as fe:
				fe.write(("%s;%s;%s;%s;\n") % ("Mass","Fish Width", "Fish Height", "Fish length"))
				fe.write(("%s;%s;%s;%s;") % (self.fishmass.get(),self.fishW.get(),self.fishH.get(),self.fishL.get()))

			print("Data saved")

			
		

		def LoadLoadLoad(event):
			# LoadLoadLoad: Loads everything if double click
			fishbox = [self.fishmass,self.fishW,self.fishH,self.fishL]
			
			if os.path.isfile(temp + "fish.txt"): 
				with open(temp + "fish.txt","r") as fe:
					datatemp = fe.readlines()[1]
					
				for ii,entry in enumerate(datatemp.split(";")):
					
					if ii == len(fishbox):break
									
					if fishbox[ii].get() =="": # if empty, and not active, fill with saved data
						if  fishbox[ii].focus_get() != fishbox[ii]: 
							fishbox[ii].insert(tk.END,entry)
					
				datatemp = None			
		
			print("Fish data loaded")
			
			
		def LoadLoad():
			#Experiment box laoding
			expbox = [self.expname,self.temperature,self.salinity,self.flush,self.wait,self.measure]
			respbox = [self.respvol,self.swinsecW,self.swinsecH]
			fishbox = [self.fishmass,self.fishW,self.fishH,self.fishL]
			

			if os.path.isfile(temp + "experiment.txt"): 
				with open(temp + "experiment.txt","r") as fe:
					datatemp = fe.readlines()[1]
					
				for ii,entry in enumerate(datatemp.split(";")):
					
					if ii == 0: continue
					if ii == len(expbox):break
									
					if expbox[ii].get() =="": # if empty, and not active, fill with saved data
						if  expbox[ii].focus_get() != expbox[ii]: 
							expbox[ii].insert(tk.END,entry)
					
				datatemp = None			

			#Respirometer box load
			if os.path.isfile(temp + "respirometer.txt"): 
				with open(temp + "respirometer.txt","r") as fe:
					datatemp = fe.readlines()[1]
					
				for ii,entry in enumerate(datatemp.split(";")):
					if ii == len(respbox):break
									
					if respbox[ii].get() =="": # if empty, and not active, fill with saved data
						if  respbox[ii].focus_get() != respbox[ii]: 
							respbox[ii].insert(tk.END,entry)
					
				datatemp = None			
			else:
				
				for ii in respbox:
					if ii.get() =="": 
						ii["bg"] = "light coral"
					else:
						ii["bg"] = "snow"
			
			print("Respirometer and experiment data loaded")
			return			
		
	
		
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.parent.wm_title("AquaResp 3 - Swim")
		self.parent.geometry('{}x{}'.format(800,600))
		self.parent.resizable(width=False, height=False)
		# self.parent.pack(side="top", fill="both", expand=True)
	
	
	
		self.main_container  = tk.Frame(self.parent)
		self.main_container.pack(side="top", fill="both",expand=True)

		self.top_frame = tk.Frame(self.main_container)
		self.bottom_frame = tk.Frame(self.main_container, background="yellow")
		
		
		self.top_frame.pack(side="top", fill="x", expand=False)
		self.bottom_frame.pack(side="bottom", fill="x", expand=True)
		
		
		self.top_left = tk.LabelFrame(self.top_frame, text="Experiment",bg="thistle3")
		
		self.top_left.pack(side="left",ipadx=75,fill="both")
		
		self.bot_left = tk.LabelFrame(self.bottom_frame, text="Equipment",bg="AntiqueWhite1")
		self.bot_rigth = tk.LabelFrame(self.bottom_frame, text="Control")
		
		
		self.bot_left.pack(side="left", fill="x", expand=True)
		self.bot_rigth.pack(side="right", fill="both", expand=True)
		
		
		self.frameresp  = tk.LabelFrame(self.top_frame, text="Respirometer",bg="LightSteelBlue1",fg="darkblue")
		self.framefish= tk.LabelFrame(self.top_frame,text="Fish",bg="DarkSeaGreen1",fg="darkgreen")

		
		self.frameresp.pack( fill="x")
		self.framefish.pack( fill="x")
		

		#Experiment contents
		self.td = tk.StringVar()
		self.label = tk.Label( self.top_left, textvariable=self.td,bg="thistle3",fg="darkblue" )
		self.td.set(ctime())
		self.label.pack(anchor="w")
		self.expnamelab = tk.Label( self.top_left, text = "Experiment name: " ,bg="thistle3")
		self.expname = tk.Entry( self.top_left )
		self.temperaturelab = tk.Label( self.top_left, text = "Temperature, Celsius: " ,bg="thistle3")
		self.temperature = tk.Entry( self.top_left )

		self.salinitylab = tk.Label( self.top_left, text = "Salinity, PSU: ",bg="thistle3" )
		self.salinity = tk.Entry( self.top_left )
		
		self.flushlab = tk.Label( self.top_left, text = "Flush time, seconds: ",bg="thistle3" )
		self.flush = tk.Entry( self.top_left )
		self.waitlab = tk.Label( self.top_left, text = "Wait time, seconds: ",bg="thistle3" )
		self.wait= tk.Entry( self.top_left )
		self.measurelab = tk.Label( self.top_left, text = "Measurement time, seconds: " ,bg="thistle3")
		self.measure = tk.Entry( self.top_left )
		
		self.expnamelab.pack(anchor="w")
		self.expname.pack(fill="x")
		
		self.temperaturelab.pack(anchor="w")
		self.temperature.pack(fill="x")		
		
		self.salinitylab.pack(anchor="w")
		self.salinity.pack(fill="x")
		
		self.flushlab.pack(anchor="w")
		self.flush.pack(fill="x")
		
		self.waitlab.pack(anchor="w")
		self.wait.pack(fill="x")
		
		self.measurelab.pack(anchor="w")
		self.measure.pack(fill="x")
	

	
		#Right side - respirometer
		self.respvollab = tk.Label( self.frameresp, text = "Respirometer volume, L: " ,bg="LightSteelBlue1")
		self.respvol = tk.Entry( self.frameresp)
		
		self.swinsecWlab = tk.Label( self.frameresp, text = "Swim section width, cm: " ,bg="LightSteelBlue1")
		self.swinsecW = tk.Entry( self.frameresp)
		
		self.swinsecHlab = tk.Label( self.frameresp, text = "Swim section height, cm: " ,bg="LightSteelBlue1")
		self.swinsecH = tk.Entry( self.frameresp)
		
		self.respvollab.pack(anchor="w")
		self.respvol.pack(fill="x")

		self.swinsecWlab.pack(anchor="w")
		self.swinsecW.pack(fill="x")

		self.swinsecHlab.pack(anchor="w")
		self.swinsecH.pack(fill="x")
	
		#Right side - fish
		self.fishLlab = tk.Label( self.framefish, text = "Fish length, cm: ",bg="DarkSeaGreen1" )
		self.fishL = tk.Entry( self.framefish)
		self.fishWlab = tk.Label( self.framefish, text = "Fish width widest, cm: ",bg="DarkSeaGreen1" )
		self.fishW = tk.Entry( self.framefish)
		self.fishHlab = tk.Label( self.framefish, text = "Fish width highest, cm: ",bg="DarkSeaGreen1" )
		self.fishH = tk.Entry( self.framefish)
		self.fishmasslab = tk.Label( self.framefish, text = "Fish mass, g: " ,bg="DarkSeaGreen1")
		self.fishmass = tk.Entry( self.framefish)
		
		self.fishLlab.pack(anchor="w")
		self.fishL.pack(fill="x")

		self.fishWlab.pack(anchor="w")
		self.fishW.pack(fill="x")

		self.fishHlab.pack(anchor="w")
		self.fishH.pack(fill="x")
		
		
		self.fishmasslab.pack(anchor="w")
		self.fishmass.pack(fill="x")
	
		
		self.O2stat = tk.Label(self.bot_left, text ="No sensor reg.",bg="AntiqueWhite1")
		self.B3 = tk.Button(self.bot_left, text ="Configure Oxygen sensor", command = O2GUI)
		
		self.Ustat = tk.Label(self.bot_left, text ="Flow not calibrated",bg="AntiqueWhite1")
		self.B4 = tk.Button(self.bot_left, text ="Calibrate flow", command = FlowCalGUI,fg="red1")

		self.Relaystat = tk.Label(self.bot_left, text ="Relay not configured",bg="AntiqueWhite1")
		self.B5 = tk.Button(self.bot_left, text ="Configure relay", command = relaygui,fg="red1")	

		self.MotorReadstat = tk.Label(self.bot_left, text ="DAQ for motor input not set",bg="AntiqueWhite1")
		self.B6 = tk.Button(self.bot_left, text ="Configure DAQ", command = DAQgui,fg="red1")
		
		# hmm
		job_function()

		
		self.B3.pack(anchor="w",fill="x")
		self.O2stat.pack(fill="x",expand=True)
		
		self.B6.pack(anchor="w",fill="x")
		self.MotorReadstat.pack(fill="x",expand=True)

		self.B4.pack(anchor="w",fill="x")
		self.Ustat.pack(fill="x",expand=True)

		self.B5.pack(anchor="w",fill="x")
		self.Relaystat.pack(fill="x",expand=True)

		#Bottom part with buttons
		B1 = tk.Button(self.bot_rigth, text ="Load information \n Left click for Resp and Exp \n Right click for fish", command = LoadLoad,fg="maroon")
		B11 = tk.Button(self.bot_rigth, text ="Save information", command = SaveSave,fg="sea green")
		
		B1.bind('<Button-3>', LoadLoadLoad)
		self.Relaystat.bind('<Button-3>',externalhandling.testpump)

		
		self.B2 = tk.Button(self.bot_rigth, text ="Start Experiment", command = StartExperiment,fg="blue",bg="PeachPuff1")	
		B1.pack(side="left",fill="both",expand=True)
		B11.pack(side="left",fill="both",expand=True)
		self.B2.pack(side="left",fill="both",expand=True)
		


if __name__ == "__main__":
	root = tk.Tk()
	Swimmy(root).pack(side="top")
	# try:
	root.mainloop()
	# except TclError:
		# "Closing main GUI"