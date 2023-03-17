#4C Bracco Mattia - TKINTER Somma

import tkinter 
#----------------------------------------------------------------------------------------------------------------------------
class Somma(tkinter.Tk):
	#Costruttore
	def __init__(self,nome):
		super().__init__()
		self.title(nome)
		self.geometry("300x200")
		self.resizable(1,1)
		self.crea_widgets()
	
	#CREA WIDGETS
	def crea_widgets(self):
		mf = tkinter.Frame(self)
		mf.grid()
		
		#Input num1
		self.lblNum1 = tkinter.Label(mf, text="Num 1:")
		self.lblNum1.grid(row=0, column=0)
		self.Num1 = tkinter.IntVar()
		self.txtNum1 = tkinter.Entry(mf, textvariable = self.Num1)
		self.txtNum1.grid(row=0, column=1)
		
		#Input num2
		self.lblNum2 = tkinter.Label(mf, text="Num 2:")
		self.lblNum2.grid(row=1, column=0)
		self.Num2 = tkinter.IntVar()
		self.txtNum2 = tkinter.Entry(mf, textvariable = self.Num2)
		self.txtNum2.grid(row=1, column=1)
		
		#Button calcola
		self.btnCalcola = tkinter.Button(mf, text="Calcola", command = self.calcolaSomma)
		self.btnCalcola.grid(row=2, column=1, columnspan=2)
		
		#Risultato
		self.lblNum3 = tkinter.Label(mf, text="Risultato: ")
		self.lblNum3.grid(row=3, column=0)
		self.ris = tkinter.DoubleVar()
		self.txtris = tkinter.Entry(mf, textvariable = self.ris)
		self.txtris.grid(row=3, column=1)

	#CALCOLA SOMMA
	def calcolaSomma(self):
		x = self.Num1.get()
		y = self.Num2.get()
		r = x + y
		self.ris.set(r)
#----------------------------------------------------------------------------------------------------------------------------
def main():
	f=Somma("Somma")
	f.mainloop()
#----------------------------------------------------------------------------------------------------------------------------
main()
