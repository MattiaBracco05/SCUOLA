#4C Bracco Mattia - TKINTER Hotel bellavista

import tkinter
import locale
from tkinter import messagebox as mbox

mioFont = ("Arial, 16")

#------------------------------------------------------------------------------------------------------------------------------------
class Finestra(tkinter.Tk):
	#Costruttore
	def __init__(self, nome):
		super().__init__()
		self.title(nome)
		self.geometry("460x500")
		self.resizable(0, 0)
		self.crea_widgets()
	
	#CREA WIDGETS
	def crea_widgets(self):
		mf = tkinter.Frame(self) #Creo l'oggetto Main Frame (contenitore principale), ci deve sempre essere e contine i widget
		mf.grid() #Definisco il layout del Main Frame (in questo caso "grid")
		
		#NOME HOTEL
		lblTitolo = tkinter.Label(mf, text="Hotel Bellavista", fg="blue", font=("Arial, 20"))
		lblTitolo.grid(row = 0, column = 0, columnspan = 4)
		
		#COGNOME PRNEOTAZIONE
		#Label
		lblCognome = tkinter.Label(mf, text="Cognome", fg='black', font=mioFont)	
		lblCognome.grid(row = 1, column = 0, sticky = tkinter.W)
		#Entry
		self.cognome = tkinter.StringVar()
		self.txtCognome = tkinter.Entry(mf, textvariable = self.cognome, bg='lightblue')
		self.txtCognome.grid(row = 1, column = 1, sticky = tkinter.W)
		
		#NOME PRENOTAZIONE
		#Label
		lblNome = tkinter.Label(mf, text="Nome", fg='black', font=mioFont)	
		lblNome.grid(row = 2, column = 0, sticky = tkinter.W)
		#Entry
		self.nome = tkinter.StringVar()
		self.txtNome = tkinter.Entry(mf, textvariable = self.nome, bg='lightblue')
		self.txtNome.grid(row = 2, column = 1, sticky = tkinter.W)
		
		#TIPO DI STANZA
		#Label
		lblStanza = tkinter.Label(mf, text="Tipo di stanza", fg='black', font=mioFont)
		lblStanza.grid(row = 3, column = 0, columnspan = 2)
		#Radio
		self.sceltaStanza = tkinter.StringVar()
		self.radio1 = tkinter.Radiobutton(mf, text="Singola", font=mioFont, variable = self.sceltaStanza, value = "singola")
		self.radio1.grid(row = 4, column = 0)	
		self.radio2 = tkinter.Radiobutton(mf, text="Matrimoniale", font=mioFont, variable = self.sceltaStanza, value = "matrimoniale")
		self.radio2.grid(row = 4, column = 1)
		
		#NUMERO NOTTI
		#Label
		lblNotti = tkinter.Label(mf, text="Numero notti", fg='black', font=mioFont)
		lblNotti.grid(row = 5, column = 0, sticky = tkinter.W)
		#Entry
		self.notti = tkinter.IntVar()
		self.txtNotti = tkinter.Entry(mf, textvariable = self.notti, bg='lightblue')
		self.txtNotti.grid(row = 5, column = 1, sticky = tkinter.W)
		
		#EXTRA
		#Label
		lblExtra = tkinter.Label(mf, text="Servizi extra", fg='black', font=mioFont)
		lblExtra.grid(row = 6, column = 0, columnspan = 3)
		#Check
		self.sceltaExtra1 = tkinter.StringVar()
		self.check1 = tkinter.Checkbutton(mf, text="Piscina", font=mioFont, variable=self.sceltaExtra1, onvalue="piscina", offvalue="")
		self.check1.grid(row = 7, column = 0)
		self.sceltaExtra2 = tkinter.StringVar()
		self.check2 = tkinter.Checkbutton(mf, text="Parcheggio", font=mioFont, variable=self.sceltaExtra2, onvalue="parcheggio", offvalue="")
		self.check2.grid(row = 7, column = 1)
		self.sceltaExtra3 = tkinter.StringVar()
		self.check3 = tkinter.Checkbutton(mf, text="WI-FI", font=mioFont, variable=self.sceltaExtra3, onvalue="WI-FI", offvalue="")
		self.check3.grid(row = 7, column = 2)
		
		#BUTTON PRENOTA
		btnPrenota = tkinter.Button(mf, text="PRENOTA", bg='lightgreen', font=mioFont, command=self.mostraRiepilogo)
		btnPrenota.grid(row=8, column=1)
		
		#BUTTON ESCI
		btnEsci = tkinter.Button(mf, text="ESCI", bg='lightblue', font=mioFont, command=self.destroy)
		btnEsci.grid(row=9, column=1)
		
	#FINESTRA RIEPILOGO
	def mostraRiepilogo(self):
		
		#RICAVO I VALORI
		nome = self.txtNome.get()
		cognome = self.txtCognome.get()
		stanza = self.sceltaStanza.get()
		notti = self.txtNotti.get()
		
		#IMPOSTO IL FLAG INIZIALE A "0"
		flag = 0
		
		#CONTROLLO CHE I DATI INSERITI SIANO CORRETTI
		#Cognome
		if (cognome.isalnum() and not cognome.isalpha()) or cognome.isnumeric() or cognome.isspace() or cognome == "":
			print("Errore nel campo cognome!")
			mbox.showwarning("Errore", "Errore campo cognome")
			self.txtCognome.configure(bg='red')
			flag = 1
		else:
			self.txtCognome.configure(bg='lightblue')
		#Nome
		if (nome.isalnum() and not nome.isalpha()) or nome.isnumeric() or nome.isspace() or nome == "":
			print("Errore nel campo nome!")
			mbox.showwarning("Errore", "Errore campo nome")
			self.txtNome.configure(bg='red')
			flag = 1
		else:
			self.txtNome.configure(bg='lightblue')
		#Stanza
		if stanza == "":
			print("Errore nel campo camera!")
			mbox.showwarning("Errore", "Errore campo camera (non selezionato)")
			flag = 1
		#Notti
		if not notti.isnumeric() or int(notti) < 1:
			print("Errore nel campo notti!")
			mbox.showwarning("Errore", "Errore campo numero notti")
			self.txtNotti.configure(bg='red')
			flag = 1
		else:
			self.txtNotti.configure(bg='lightblue')
		
		#SE I DATI SONO TUTTI CORRETTI --> messaggio riepilogo
		if flag == 0:
			serviziExtra = self.sceltaExtra1.get() + " " + self.sceltaExtra2.get() + " " + self.sceltaExtra3.get()
			mbox.showinfo(title="Riepilogo prenotazione", message='Riepilogo \nIl sig. {0} {1}\nHa prenotato una stanza {2} per n. {3} notti\ncon i seguenti servizi extra: {4}'.format(cognome, nome, stanza, notti, serviziExtra))
#------------------------------------------------------------------------------------------------------------------------------------
def main():
	f = Finestra('Hotel Bellavista')
	f.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------
main()
