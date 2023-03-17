#4C Bracco Mattia - TKINTER Calcolatrice

import tkinter


#------------------------------------------------------------------------------------------------------------------------------------
class Finestra(tkinter.Tk):
	#Costruttore
	def __init__(self, nome):
		super().__init__()
		self.espressione = ''
		self.title(nome)
		self.geometry("385x185")
		self.resizable(0, 0)
		self.crea_widgets()
	
	#CREA WIDGETS
	def crea_widgets(self):
		mf = tkinter.Frame(self) #Creo l'oggetto Main Frame (contenitore principale), ci deve sempre essere e contine i widget
		mf.grid() #Definisco il layout del Main Frame (in questo caso "grid")

		#Entry
		self.equation = tkinter.StringVar()
		expressionField = tkinter.Entry(mf, textvariable=self.equation)
		expressionField.grid(columnspan=4, ipadx=100)

		#1
		btn1 = tkinter.Button(mf, text='1', fg='black', bg='lightblue', command=lambda: self.press(1), height=1, width=7)
		btn1.grid(row=1, column=0)
		#2
		btn2 = tkinter.Button(mf, text='2', fg='black', bg='lightblue', command=lambda: self.press(2), height=1, width=7)
		btn2.grid(row=1, column=1)
		#3
		btn3 = tkinter.Button(mf, text='3', fg='black', bg='lightblue', command=lambda: self.press(3), height=1, width=7)
		btn3.grid(row=1, column=2)
		#4
		btn4 = tkinter.Button(mf, text='4', fg='black', bg='lightblue', command=lambda: self.press(4), height=1, width=7)
		btn4.grid(row=2, column=0)
		#5
		btn5 = tkinter.Button(mf, text='5', fg='black', bg='lightblue', command=lambda: self.press(5), height=1, width=7)
		btn5.grid(row=2, column=1)
		#6
		btn6 = tkinter.Button(mf, text='6', fg='black', bg='lightblue', command=lambda: self.press(6), height=1, width=7)
		btn6.grid(row=2, column=2)
		#7
		btn7 = tkinter.Button(mf, text='7', fg='black', bg='lightblue', command=lambda: self.press(7), height=1, width=7)
		btn7.grid(row=3, column=0)
		#8
		btn8 = tkinter.Button(mf, text='8', fg='black', bg='lightblue', command=lambda: self.press(8), height=1, width=7)
		btn8.grid(row=3, column=1)
		#9
		btn9 = tkinter.Button(mf, text='9', fg='black', bg='lightblue', command=lambda: self.press(9), height=1, width=7)
		btn9.grid(row=3, column=2)
		#0
		btn0 = tkinter.Button(mf, text='0', fg='black', bg='lightblue', command=lambda: self.press(0), height=1, width=7)
		btn0.grid(row=4, column=1)
		
		#.
		btnPunto = tkinter.Button(mf, text='.', fg='black', bg='lightgreen', command=lambda: self.press('.'), height=1, width=7)
		btnPunto.grid(row=4, column=0)
		#=
		btnUguale = tkinter.Button(mf, text='=', fg='black', bg='lightgreen', command=self.calcolaRisultato, height=1, width=7)
		btnUguale.grid(row=4, column=2)
		
		#+
		btnSomma = tkinter.Button(mf, text='+', fg='black', bg='blue', command=lambda: self.press('+'), height=1, width=7)
		btnSomma.grid(row=1, column=3)
		#-
		btnSottrazione = tkinter.Button(mf, text='-', fg='black', bg='blue', command=lambda: self.press('-'), height=1, width=7)
		btnSottrazione.grid(row=2, column=3)
		#X
		btnMoltiplicazione = tkinter.Button(mf, text='X', fg='black', bg='blue', command=lambda: self.press('*'), height=1, width=7)
		btnMoltiplicazione.grid(row=3, column=3)
		#:
		btnDivisione = tkinter.Button(mf, text=':', fg='black', bg='blue', command=lambda: self.press('/'), height=1, width=7)
		btnDivisione.grid(row=4, column=3)
		
		#clear
		btnClear = tkinter.Button(mf, text='CLEAR', fg='black', bg='lightgreen', command=self.clear, height=1, width=7)
		btnClear.grid(row=5, column=0, columnspan = 4)
	
	#PRESS
	def press(self, val):
		self.espressione = self.espressione + str(val)
		self.equation.set(self.espressione)
	
	#CALCOLA RISULTATO
	def calcolaRisultato(self):
		try:
			risultato = str(eval(self.espressione))
			self.equation.set(risultato)
		except:
			self.equation.set("Errore!")
			self.espressione = "" 
	
	#CLEAR
	def clear(self):
		self.espressione = ""
		self.equation.set("")
#------------------------------------------------------------------------------------------------------------------------------------
def main():
	f = Finestra('Calcolatrice')
	f.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------
main()
