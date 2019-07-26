# import aquareadDAQ

import tkinter as tk
import threading as thr
import dataacq
import numpy as np

global datahold1
global datahold2
global datahold3
global datahold4
datahold1 = []
datahold2 = []
datahold3 = []
datahold4 = []


def fakevoltage(level, noise):
	measured = level +np.random.normal(loc=1,scale= noise)
	return measured,measured,measured,measured

class MyFirstGUI:

	def __init__(self, master):
		
		def updatelabel():
			

			U,Uc,Ubl ,V = dataacq.returnUfromCal()
			# U,Uc,Ubl ,V = fakevoltage(1,0.1)
			
			
			#######################3
			global datahold1			
			global datahold2			
			global datahold3			
			global datahold4	
			
			datahold1.append(U)
			datahold2.append(Uc)
			datahold3.append(Ubl)
			datahold4.append(V)

			if len(datahold1) >= 40:
				del datahold1[0]
				del datahold2[0]
				del datahold3[0]
				del datahold4[0]
			
			U = np.average(datahold1)
			Uc = np.average(datahold2)
			Ubl = np.average(datahold3)
			V = np.average(datahold4)
			#######################3
			
			# self.master.lift()
			try:
				self.labelU["text"] = "Not solid blocking corrected: " + str('{0:.2f}'.format(U)) + "cm/s"
				self.labelUC["text"] = str('{0:.2f}'.format(Uc)) + " cm/s"
				self.labelUCBL["text"] = str('{0:.2f}'.format(Ubl)) + " BL/s"
				self.labelV["text"] = str('{0:.2f}'.format(V)) + " V"
			except:
				pass
			else:
				job_function()

			
		def job_function():
			thr.Timer(.1, updatelabel).start()
		
		self.master = master
		
		
		
		#######
		master.wm_attributes("-topmost", 1)
		master.overrideredirect(1)
		#######
		
		
		
		
		master.wm_title("Flow and voltage from DAQ - AQ3 Swim")
		master.geometry('{}x{}'.format(350, 200))
		# # # # # # # # # # # # # master.configure(bg='darkgrey')
		master.configure(bg='black')
		master.config(highlightbackground="purple")

		# self.label = tk.Label(master, text="U, cm/s",bg='darkgrey')
		# self.label.pack(anchor="w")


		self.labelU = tk.Label(master, text="",bg='black',fg="white")
		self.labelV = tk.Label(master, text="",bg='black',fg="white")
		# self.labelU.pack()

		self.label2 = tk.Label(master, text="Corrected water flow - U ",bg='black',fg="white")
		self.label2.pack(anchor="w")


		self.labelUC = tk.Label(master, text="",bg='black',fg="violet red")
		self.labelUC.pack(anchor = "n")		
		
		# self.label3 = tk.Label(master, text="U corr.",bg='darkgrey')
		# self.label3.pack(anchor="w")


		self.labelUCBL = tk.Label(master, text="",bg='black',fg="green")
		self.labelUCBL.pack(anchor = "n")
		
		
		
		
		self.labelU.config(font=("Helvetica", 10))
		self.labelV.config(font=("Helvetica", 10))
		self.labelUC.config(font=("Helvetica", 20))
		self.labelUCBL.config(font=("Helvetica", 20))
		self.label2.config(font=("Helvetica", 15))


		self.close_button = tk.Button(master, text="Close this window", command=self.doone,bg='azure')
		self.close_button.pack()
		self.labelU.pack()
		self.labelV.pack()
		job_function()
		# updatelabel()
	
	def doone(self):
		print("Greetings! - Goodbye!")
		self.master.destroy()
	
	
		


root = tk.Tk()
my_gui = MyFirstGUI(root)
# updatelabel()
root.mainloop()