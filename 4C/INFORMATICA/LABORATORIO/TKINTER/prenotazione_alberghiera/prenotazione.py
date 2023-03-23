#4C Bracco Mattia - TKINTER Prenotazione alberghiera

import tkinter
from tkinter import messagebox as mbox
from functools import partial

costoSingola = 80
costoMatrimoniale = 150
sogliaCosto = 300

#------------------------------------------------------------------------------------------------------------------------------------
class Finestra(tkinter.Tk):
	#Costruttore
	def __init__(self, nome):
		super().__init__()
		self.title(nome)
		self.geometry("700x230")
		self.resizable(0, 0)
		self.crea_widgets()
	
	#CREA WIDGETS
	def crea_widgets(self):
		mf = tkinter.Frame(self) #Creo l'oggetto Main Frame (contenitore principale), ci deve sempre essere e contine i widget
		mf.grid() #Definisco il layout del Main Frame (in questo caso "grid")

		#NOME PRENOTAZIONE
		#Label
		lblNome = tkinter.Label(mf, text="Nome prenotazione: ", fg='black', font=("Arial", 12))	
		lblNome.grid(row = 1, column = 0, sticky = tkinter.W)
		#Entry
		self.nome = tkinter.StringVar()
		self.txtNome = tkinter.Entry(mf, textvariable = self.nome, bg='lightblue')
		self.txtNome.grid(row = 1, column = 1, sticky = tkinter.W)
		#COGNOME PRNEOTAZIONE
		#Label
		lblCognome = tkinter.Label(mf, text="Cognome prenotazione: ", fg='black', font=("Arial", 12))	
		lblCognome.grid(row = 2, column = 0, sticky = tkinter.W)
		#Entry
		self.cognome = tkinter.StringVar()
		self.txtCognome = tkinter.Entry(mf, textvariable = self.cognome, bg='lightblue')
		self.txtCognome.grid(row = 2, column = 1, sticky = tkinter.W)
		
		#NUMERO TOTALE
		#Label
		lblNTotale = tkinter.Label(mf, text="Numero totale persone: ", fg='black', font=("Arial", 12))	
		lblNTotale.grid(row = 3, column = 0, sticky = tkinter.SW)
		#Entry
		self.totale = tkinter.IntVar()
		self.txtTotale = tkinter.Entry(mf, textvariable = self.totale, bg='lightblue')
		self.txtTotale.grid(row = 3, column = 1, sticky = tkinter.W)
		#NUMERO ADULTI
		#Label
		lblNAdulti = tkinter.Label(mf, text="Numero adulti: ", fg='black', font=("Arial", 12))	
		lblNAdulti.grid(row = 3, column = 2, sticky = tkinter.W)
		#Entry
		self.adulti = tkinter.IntVar()
		self.txtAdulti = tkinter.Entry(mf, textvariable = self.adulti, bg='lightblue')
		self.txtAdulti.grid(row = 3, column = 3, sticky = tkinter.W)
		#NUMERO BAMBINI
		#Label
		lblNBambini = tkinter.Label(mf, text="Numero bambini: ", fg='black', font=("Arial", 12))	
		lblNBambini.grid(row = 4, column = 2, sticky = tkinter.W)
		#Entry
		self.bambini = tkinter.IntVar()
		self.txtBambini = tkinter.Entry(mf, textvariable = self.bambini, bg='lightblue')
		self.txtBambini.grid(row = 4, column = 3, sticky = tkinter.W)
		
		#NUMERO NOTTI
		#Label
		lblNotti = tkinter.Label(mf, text="Numero notti: ", fg='black', font=("Arial", 12))
		lblNotti.grid(row = 5, column = 1, sticky = tkinter.W)
		#Entry
		self.notti = tkinter.IntVar()
		self.txtNotti = tkinter.Entry(mf, textvariable = self.notti, bg='lightblue')
		self.txtNotti.grid(row = 5, column = 2, sticky = tkinter.W)
		
		#NUMERO CAMERE SINGOLE
		#Label
		lblSingole = tkinter.Label(mf, text="Numero camere singole: ", fg='black', font=("Arial", 12))
		lblSingole.grid(row = 6, column = 0, sticky = tkinter.W)
		#Entry
		self.singole = tkinter.IntVar()
		self.txtSingole = tkinter.Entry(mf, textvariable = self.singole, bg='lightblue')
		self.txtSingole.grid(row = 6, column = 1, sticky = tkinter.W)
		#NUMERO CAMERE MATRIMONIALI
		#Label
		lblSingole = tkinter.Label(mf, text="Numero camere matrimoniali: ", fg='black', font=("Arial", 12))
		lblSingole.grid(row = 6, column = 2, sticky = tkinter.W)
		#Entry
		self.matrimoniali = tkinter.IntVar()
		self.txtMatrimoniali = tkinter.Entry(mf, textvariable = self.matrimoniali, bg='lightblue')
		self.txtMatrimoniali.grid(row = 6, column = 3, sticky = tkinter.W)
		
		#BUTTON CALCOLA
		btnCalcolo = tkinter.Button(mf, text="CALCOLA", bg='lightgreen', command=self.calcola)
		btnCalcolo.grid(row=7, column=1)
		#BUTTON ANNULLA
		btnAnnulla = tkinter.Button(mf, text="ANNULLA", bg='red', command=self.annulla)
		btnAnnulla.grid(row=7, column=2)
		
		#SOMMA DA VERSARE
		#Label
		lblSomma = tkinter.Label(mf, text="Somma da versare: ", fg='black', font=("Arial", 12))
		lblSomma.grid(row = 8, column = 1, sticky = tkinter.W)
		#Entry
		self.somma = tkinter.IntVar()
		self.txtSomma = tkinter.Entry(mf, textvariable = self.somma, bg='lightblue')
		self.txtSomma.grid(row = 8, column = 2, sticky = tkinter.W)
		self.txtSomma.config(state = "readonly") #Disabilito l'input sulla entry che mostra la somma
		#BUTTON ESCI
		btnEsci = tkinter.Button(mf, text="ESCI", bg='lightgreen', command=self.destroy)
		btnEsci.grid(row=9, column=3)

	#AZIONE BUTTON CALCOLA
	def calcola(self):
		#RICAVO I VALORI
		nome = self.txtNome.get()
		cognome = self.txtCognome.get()
		nTOT = self.txtTotale.get()
		nADU = self.txtAdulti.get()
		nBAM = self.txtBambini.get()
		nNOT = self.txtNotti.get()
		sing = self.txtSingole.get()
		matr = self.txtMatrimoniali.get()
		
		#IMPOSTO IL FLAG INIZIALE A "0"
		flag = 0
		
		#CONTROLLO I VALORI INSERITI
		#Nome
		if (nome.isalnum() and not nome.isalpha()) or nome.isnumeric() or nome.isspace() or nome == "":
			print("Errore nel campo nome!")
			mbox.showwarning("Errore", "Errore campo nome")
			self.txtNome.configure(bg='red')
			flag = 1
		else:
			self.txtNome.configure(bg='lightblue')
		#Cognome
		if (cognome.isalnum() and not cognome.isalpha()) or cognome.isnumeric() or cognome.isspace() or cognome == "":
			print("Errore nel campo cognome!")
			mbox.showwarning("Errore", "Errore campo cognome")
			self.txtCognome.configure(bg='red')
			flag = 1
		else:
			self.txtCognome.configure(bg='lightblue')
		#Numero persone totali
		if not nTOT.isnumeric() or int(nTOT) < 1:
			print("Errore nel campo numero totale!")
			mbox.showwarning("Errore", "Errore campo numero totale persone")
			self.txtTotale.configure(bg='red')
			flag = 1
		else:
			self.txtTotale.configure(bg='lightblue')
		#Numero notti
		if not nNOT.isnumeric() or int(nNOT) < 1:
			print("Errore nel campo notti!")
			mbox.showwarning("Errore", "Errore campo numero notti")
			self.txtNotti.configure(bg='red')
			flag = 1
		else:
			self.txtNotti.configure(bg='lightblue')
		#Numero adulti
		if not nADU.isnumeric():
			print("Errore nel campo adulti!")
			mbox.showwarning("Errore", "Errore campo numero adulti")
			self.txtAdulti.configure(bg='red')
			flag = 1
		else:
			self.txtAdulti.configure(bg='lightblue')
		#Numero bambini
		if not nBAM.isnumeric():
			print("Errore nel campo bambini!")
			mbox.showwarning("Errore", "Errore campo numero bambini")
			self.txtBambini.configure(bg='red')
			flag = 1
		else:
			self.txtBambini.configure(bg='lightblue')
		#Numero camere singole
		if not sing.isnumeric():
			print("Errore nel campo camere singole!")
			mbox.showwarning("Errore", "Errore campo numero camere singole")
			self.txtSingole.configure(bg='red')
			flag = 1
		else:
			self.txtSingole.configure(bg='lightblue')
		#numero camere matrimoniali
		if not matr.isnumeric():
			print("Errore nel campo camere matrimoniali!")
			mbox.showwarning("Errore", "Errore campo numero camere matrimoniali")
			self.txtMatrimoniali.configure(bg='red')
			flag = 1
		else:
			self.txtMatrimoniali.configure(bg='lightblue')
		
		#persone totali
		if (int(nBAM) + int(nADU)) != int(nTOT):
			print("Il numero delle persone non corrisponde con le persone totali")
			mbox.showwarning("Errore", "Il numero delle persone non corrisponde con le persone totali")
			self.txtTotale.configure(bg='red')
			self.txtAdulti.configure(bg='red')
			self.txtBambini.configure(bg='red')
			flag = 1
		else:
			self.txtTotale.configure(bg='lightblue')
			self.txtAdulti.configure(bg='lightblue')
			self.txtBambini.configure(bg='lightblue')
		#camere totali
		if (int(sing) + int(matr)) == 0:
			print("Il numero totale delle camere è pari a 0")
			mbox.showwarning("Errore", "Il numero totale delle camere è pari a 0")
			flag = 1
			self.txtSingole.configure(bg='red')
			self.txtMatrimoniali.configure(bg='red')
		else:
			self.txtSingole.configure(bg='lightblue')
			self.txtMatrimoniali.configure(bg='lightblue')
		
		#Se flag = 0 (non ci sono errori --> calcolo il totale)
		if flag == 0:
			costo = ((int(sing) * costoSingola) + (int(matr) * costoMatrimoniale)) * int(nNOT)
			self.somma.set(costo)
			if costo > sogliaCosto:
				self.txtSomma.configure(bg='red')
			else:
				self.txtSomma.configure(bg='lightgreen')
			
		#MESSAGGIO ALL'UTENTE
		if flag == 1:
			print("ERRORE NELLA COMPLIAZIONE DEI DATI")
		else:
			print("DATI PRENOTAZIONE\nNome: " + nome + " Cognome: " + cognome + "\nTotale: " + nTOT + " Numero adulti: " + nADU + " Numero bambini: " + nBAM + "\nNumero notti: " + nNOT + "\nCamere singole: " + sing + " Camere matrimoniali: " + matr + "\nCosto: " + str(costo) + "€")
	
	#AZIONE BUTTON ANNULLA
	def annulla(self):
		self.nome.set("")
		self.cognome.set("")
		self.totale.set(0)
		self.adulti.set(0)
		self.bambini.set(0)
		self.notti.set(0)
		self.singole.set(0)
		self.matrimoniali.set(0)
		self.somma.set(0)

#------------------------------------------------------------------------------------------------------------------------------------
def main():
	f = Finestra('Prenotazione alberghiera')
	f.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------
main()
