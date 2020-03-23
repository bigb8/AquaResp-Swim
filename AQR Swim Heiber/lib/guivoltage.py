import dataacq

import tkinter as tk
import threading as thr
import numpy as np

global VList
VList = []


class MyFirstGUI:

	def __init__(self, master):
		
		def updatelabel():
			V = dataacq.returnvoltage()
			# Add a smoother to the voltage signal
			global VList
			VList.append(V)
			if len(VList) > 20:
				del VList[0]
			
			V = np.median(VList)
			
			try:
				self.labelV["text"] = str('{0:.2f}'.format(V))
			except:
				pass
			else:
				job_function()

			
		def job_function():
			thr.Timer(.1, updatelabel).start()
		
		self.master = master


		master.wm_title("Voltage from DAQ - AQ3 Swim")
		master.geometry('{}x{}'.format(400, 150))
		master.configure(bg='darkgrey')

		self.label = tk.Label(master, text="Voltage read:",bg='darkgrey')
		self.label.pack()


		self.labelV = tk.Label(master, text="",bg='darkgrey',fg="blue")
		self.labelV.pack()
		self.labelV.config(font=("Courier", 44))


		self.close_button = tk.Button(master, text="Close", command=self.doone,bg='red4')
		self.close_button.pack()
		
		job_function()
		# updatelabel()
	
	def doone(self):
		print("Greetings! - Goodbye!")
		self.master.destroy()
	
	
		


root = tk.Tk()
my_gui = MyFirstGUI(root)
# updatelabel()
root.mainloop()