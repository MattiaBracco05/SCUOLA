#4C Bracco Mattia - TKINTER Widget listbox

import tkinter
from tkinter import ttk
from tkinter import messagebox as mbox

mioFont = ("Arial, 16")

#------------------------------------------------------------------------------------------------------------------------------------
class Finestra(tkinter.Tk):
	#Costruttore
	def __init__(self, nome):
		super().__init__()
		self.title(nome)
		self.geometry("660x1000")
		self.resizable(0, 0)
		self.crea_widgets()
	
	#CREA WIDGETS
	def crea_widgets(self):
		mf = tkinter.Frame(self) #Creo l'oggetto Main Frame (contenitore principale), ci deve sempre essere e contine i widget
		mf.grid() #Definisco il layout del Main Frame (in questo caso "grid")
		
		#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		#LABEL SELECTMODE
		lblSelectmode = tkinter.Label(mf, text="OPZIONI PER SELECTMODE")
		lblSelectmode.grid(row=0, column=0, columnspan=4, sticky=tkinter.EW)
		
		#LISTBOX ACCESSORI (selectmode = browse)
		#Label
		lblBrowse = tkinter.Label(mf, text="BROWSE", bg="blue")
		lblBrowse.grid(row=1, column=0, sticky=tkinter.EW)
		#Listbox
		accessori = ('Pasta', 'Bistecca', 'Carne', 'Pesce', 'Patatine', 'Verdura', 'Contorno', 'Dolce')
		varAccessori = tkinter.Variable(value = accessori)
		listAccessori = tkinter.Listbox(mf, listvariable=varAccessori, height=5, selectmode=tkinter.BROWSE)
		listAccessori.grid(row=2, column=0)
		
		#LISTBOX CIBI (selectmode = extend)
		#Label
		lblBrowse = tkinter.Label(mf, text="EXTENDED", bg="yellow")
		lblBrowse.grid(row=1, column=1, sticky=tkinter.EW)
		#Listbox
		cibi = ('Pasta', 'Bistecca', 'Carne', 'Pesce', 'Patatine', 'Verdura', 'Contorno', 'Dolce')
		varCibi = tkinter.Variable(value = cibi)
		listCibi = tkinter.Listbox(mf, listvariable=varCibi, height=5, selectmode=tkinter.EXTENDED)
		listCibi.grid(row=2, column=1)
		
		#LISTBOX AUTO (selectmode = single)
		#Label
		lblBrowse = tkinter.Label(mf, text="SINGLE", bg="green")
		lblBrowse.grid(row=1, column=2, sticky=tkinter.EW)
		#Listbox
		auto = ('Alfa Romeo', 'Fiat', 'Ford', 'Ferrari', 'Lamborgini', 'Maserati', 'Audi', 'Mercedes', 'BMW', 'Lancia', 'Volvo', 'Seat', 'Kia')
		varAuto = tkinter.Variable(value = auto)
		listAuto = tkinter.Listbox(mf, listvariable=varAuto, height=5, selectmode=tkinter.SINGLE)
		listAuto.grid(row=2, column=2)
		
		#LISTBOX COLORI (selectmode = multiple)
		#Label
		lblBrowse = tkinter.Label(mf, text="MULTIPLE", bg="gray")
		lblBrowse.grid(row=1, column=3, sticky=tkinter.EW)
		#Listbox
		colori = ('Giallo', 'Azzurro', 'Blu', 'Verde', 'Marrone', 'Nero', 'Giallo', 'Mercedes', 'BMW', 'Lancia', 'Volvo', 'Seat', 'Kia')
		varColori = tkinter.Variable(value = colori)
		listColori = tkinter.Listbox(mf, listvariable=varColori, height=5, selectmode=tkinter.MULTIPLE)
		listColori.grid(row=2, column=3)
	
		#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		#LABEL SCROLLBAR
		lblScrollbar = tkinter.Label(mf, text="SCROLLBAR")
		lblScrollbar.grid(row=3, column=0, columnspan=4, sticky=tkinter.EW)

		#Listbox
		linguaggi = ('C#', 'C', 'C++', 'Python', 'Go', 'PHP', 'Swift', 'HTML', 'CSS', 'JSON', 'XML', 'JavaScript', 'Java')
		varLinguaggi = tkinter.Variable(value = linguaggi)
		listLinguaggi = tkinter.Listbox(mf, listvariable=varLinguaggi, height=8, selectmode=tkinter.BROWSE)
		listLinguaggi.grid(row=4, column=0)
		#Scrollbar
		scrollbar = ttk.Scrollbar(mf, orient=tkinter.VERTICAL, command=listLinguaggi.yview)
		listLinguaggi['yscrollcommand'] = scrollbar.set
		scrollbar.grid(row=4, column=1, sticky=tkinter.NS)
		
		#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		#LABEL OPERAZIONI
		lblOperazioni = tkinter.Label(mf, text="OPERAZIONI SULLE LISTE (Vedere codice)")
		lblOperazioni.grid(row=5, column=0, columnspan=4, sticky=tkinter.EW)
		
		#Listbox di partenza
		nomi = ('Alessio', 'Francesco', 'Pietro', 'Paolo', 'Giuseppe', 'Gabriele', 'Edoardo', 'Leonardo', 'Davide')
		varNomi = tkinter.Variable(value = nomi)
		listNomi = tkinter.Listbox(mf, listvariable=varNomi, height=8, selectmode=tkinter.BROWSE)
		listNomi.grid(row=6, column=0)
		#Inserisco un nome in posizione 0 ("Mattia")
		listNomi.insert(0, "Mattia")
		#Elimino il nome nella posizione 2 ("Francesco")
		listNomi.delete(2)
		
		#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		#LABEL SELEZIONE
		lblSelezione = tkinter.Label(mf, text="VALORE SELEZIONATO")
		lblSelezione.grid(row=7, column=0, columnspan=4, sticky=tkinter.EW)

		#Listbox
		sport = ('Calcio', 'Pallavolo', 'Basket', 'Rugby', 'Tennis', 'Nuoto', 'Padel', 'Atletica')
		varSport = tkinter.Variable(value = sport)
		self.listSport = tkinter.Listbox(mf, listvariable=varSport, height=8, selectmode=tkinter.BROWSE)
		self.listSport.grid(row=8, column=0)
		#Button
		btnConferma = tkinter.Button(mf, text='CONFERMA', command=self.stampaSelezione, bg="lightgreen")
		btnConferma.grid(row=8, column=1)
		
		#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		#BUTTON ESCI
		btnEsci = tkinter.Button(mf, text="ESCI", command=self.destroy, bg="red")
		btnEsci.grid(row=9, column=0, columnspan=4, sticky=tkinter.EW)
		
	#STAMPA SELEZIONE
	def stampaSelezione(self):
		for i in self.listSport.curselection():
			print(self.listSport.get(i))
			mbox.showinfo("Selezione", self.listSport.get(i))
			
#------------------------------------------------------------------------------------------------------------------------------------
def main():
	f = Finestra('Widget Listbox')
	f.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------
main()