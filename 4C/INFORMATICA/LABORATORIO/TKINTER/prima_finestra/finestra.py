#4C Bracco Mattia - Prima finestra TKINTER

import tkinter
#----------------------------------------------------------------------------------------------------------------------------
class Finestra(tkinter.Tk):
	#Costruttore
	def __init__(self, nome):
		super().__init__()
		self.title("Finestra grafica " + nome)
		self.geometry("300x200")
		self.resizable(0, 0)
		self.crea_widgets()
	
	#CREA WIDGETS
	def crea_widgets(self):
		mf = tkinter.Frame(self) #Creo l'oggetto Main Frame (contenitore principale), ci deve sempre essere e contine i widget
		mf.grid() #Definisco il layout del Main Frame (in questo caso "grid")
		#Label
		lbl1 = tkinter.Label(mf, text="Premi il pulsante -->") #Creo la label
		lbl1.grid(row=0, column=0) #Posiziono la label
		#Button
		btn1 = tkinter.Button(mf, text="Click here") #Creo il button
		btn1.grid(row=0, column=1) #Posiziono il button
#----------------------------------------------------------------------------------------------------------------------------
def main():
	f = Finestra('Main')
	f.mainloop()
#----------------------------------------------------------------------------------------------------------------------------
main()
