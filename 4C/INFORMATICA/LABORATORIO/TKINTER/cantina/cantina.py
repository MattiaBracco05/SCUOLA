#5C Bracco Mattia

#IMPORT
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import pickle

#-----------------------------------------------------------------------------------------------------------------------------------
class Vino:
	#Costruttore
	def __init__(self, nome, anno):
		self.nome = nome
		self.anno = anno
#-----------------------------------------------------------------------------------------------------------------------------------
class Bottiglia:
	#Costruttore
	def __init__(self, nome, anno, vino):
		self.nome = nome
		self.anno = anno
		self.vino = vino
		self.spostamenti = []

	#Aggiugni spostamento
	def aggiungiSpostamento(self, scaffaleDestinazione):
		spostamento = Spostamento(self, scaffaleDestinazione)
		self.spostamenti.append(spostamento)
#-----------------------------------------------------------------------------------------------------------------------------------
class Spostamento:
	#Costruttore
	def __init__(self, bottiglia, scaffaleDestinazione):
		self.bottiglia = bottiglia
		self.scaffaleDestinazione = scaffaleDestinazione
#-----------------------------------------------------------------------------------------------------------------------------------
class Scaffale:
	#Costruttore
	def __init__(self, nome):
		self.nome = nome
		self.bottiglie = []

	#Aggiungi bottiglia
	def aggiungiBottiglia(self, bottiglia):
		self.bottiglie.append(bottiglia)

	#Rimuovi bottiglia
	def eliminaBottiglia(self, bottiglia):
		#Controllo che la bottiglia sia presente
		if bottiglia in self.bottiglie:
			self.bottiglie.remove(bottiglia)
#-----------------------------------------------------------------------------------------------------------------------------------
class Cantina:
	#Costruttore
	def __init__(self):
		self.stanze = {}

	#Aggiungi stanza
	def aggiungiStanza(self, nomeStanza):
		self.stanze[nomeStanza] = []

	#Aggiungi scaffale
	def aggiungiScaffale(self, nomeStanza, nomeScaffale):
		scaffale = Scaffale(nomeScaffale)
		self.stanze[nomeStanza].append(scaffale)

	#Elimina scaffale
	def eliminaScaffale(self, nomeStanza, nomeScaffale):
		scaffale = next((s for s in self.stanze[nomeStanza] if s.nome == nomeScaffale), None)
		# Controllo che lo scaffale esista nella stanza
		if scaffale:
			#Controllo che lo scaffale sia vuoto
			if len(scaffale.bottiglie) == 0:
				#Rimuovo lo scaffale
				self.stanze[nomeStanza].remove(scaffale)
			
			#Altrimenti --> messaggii di errore
			else:
				messagebox.showerror("Errore", "Lo scaffale deve essere vuoto per poter essere eliminato!")
		else:
			messagebox.showerror("Errore", "Lo scaffale non esiste!")
#-----------------------------------------------------------------------------------------------------------------------------------
class App:
	#Costruttore
	def __init__(self, root):
		self.cantina = Cantina()
		self.caricaDati()

		self.root = root
		self.root.title("Gestione Cantina")

		#Creo uno stile personalizzato per le combobox
		stileCombobox = ttk.Style()
		stileCombobox.theme_create('mioStileCombobox', parent='alt', settings={
			'TCombobox': {
				'configure': {
					'padding': 5,  #Padding interno
					'background': 'blue',  #Colore di sfondo (dove c'è la freccia)
					'fieldbackground': 'lightblue',  #Colore dell'input
					'bordercolor': 'black',  #Colore del bordo
					'arrowsize': 20, #Dimensione della freccia
					'arrowcolor': 'black',  #Colore della freccia
				}
			}
		})
		stileCombobox.theme_use('mioStileCombobox')

		#Selezione della stanza
		self.stanzaLabel = tk.Label(root, text="Seleziona stanza:")
		self.stanzaLabel.grid(row=0, column=0, columnspan=2)
		self.stanzaVar = tk.StringVar()
		self.stanzaMenu = ttk.Combobox(root, textvariable=self.stanzaVar, values=list(self.cantina.stanze.keys()))
		self.stanzaMenu.bind("<<ComboboxSelected>>", self.visualizzaScaffali)
		self.stanzaMenu.grid(row=1, column=0, columnspan=2)

		#Selezione dello scaffale
		self.scaffaleLabel = tk.Label(root, text="Seleziona scaffale:")
		self.scaffaleLabel.grid(row=3, column=0, columnspan=2)
		self.scaffaleVar = tk.StringVar()
		self.scaffaleMenu = ttk.Combobox(root, textvariable=self.scaffaleVar)
		self.scaffaleMenu.grid(row=4, column=0, columnspan=2)

		#--------------------------------------
		#--------------- BUTTON ---------------
		#--------------------------------------
		
		#STANZA
		#Aggiungi
		self.btnAggiungiStanza = tk.Button(root, text="Aggiungi Stanza", command=self.aggiungiStanza, bg='lightgreen')
		self.btnAggiungiStanza.grid(row=2, column=0, sticky = tk.EW)
		#Elimina
		self.btnEliminaStanza = tk.Button(root, text="Elimina Stanza", command=self.eliminaStanza, bg='red')
		self.btnEliminaStanza.grid(row=2, column=1, sticky = tk.EW)

		#SCAFFALE
		#Aggiungi
		self.btnAggiungiScaffale = tk.Button(root, text="Aggiungi Scaffale", command=self.aggiungiScaffale, bg='lightgreen')
		self.btnAggiungiScaffale.grid(row=5, column=0, sticky = tk.EW)
		#Elimina
		self.btnEliminaScaffale = tk.Button(root, text="Elimina Scaffale", command=self.eliminaScaffale, bg='red')
		self.btnEliminaScaffale.grid(row=5, column=1, sticky = tk.EW)

		#BOTTIGLIA
		#Aggiungi
		self.btnAggiungiBottiglia = tk.Button(root, text="Aggiungi Bottiglia", command=self.aggiungiBottiglia, bg='lightgreen')
		self.btnAggiungiBottiglia.grid(row=7, column=0, sticky = tk.EW)
		#Elimina
		self.btnEliminaBottiglia = tk.Button(root, text="Rimuovi Bottiglia", command=self.eliminaBottiglia, bg='red')
		self.btnEliminaBottiglia.grid(row=7, column=1, sticky = tk.EW)
		#Sposta
		self.btnSpostaBottiglia = tk.Button(root, text="Sposta Bottiglia", command=self.spostaBottiglia, bg='lightblue')
		self.btnSpostaBottiglia.grid(row=8, column=0, sticky = tk.EW)
		#Visualizza
		self.btnVisualizzaBottiglie = tk.Button(root, text="Visualizza Bottiglie", command=self.visualizzaBottiglie, bg='lightblue')
		self.btnVisualizzaBottiglie.grid(row=8, column=1, sticky = tk.EW)
		
		#Riquadro elenco bottiglie
		self.lista_bottiglie = tk.Listbox(root)
		self.lista_bottiglie.grid(row=6, column=0, columnspan=2)
				
	#--------------------------------------
	#--------------- STANZA ---------------
	#--------------------------------------
	
	#AGGIUNGI
	#Questo metodo permette di aggiungere una stanza, i dati richiesti sono il nome della stanza da creare
	def aggiungiStanza(self):
		#Chiedo il nome della stanza da creare
		nomeStanza = simpledialog.askstring("Aggiungi Stanza", "Inserire il nome della stanza: ")
		#Creo la stanza e salvo i dati
		if nomeStanza:
			self.cantina.aggiungiStanza(nomeStanza)
			self.stanzaMenu['values'] = list(self.cantina.stanze.keys())
			self.salvaDati()

	#ELIMINA
	#Questo metodo permette di eliminare la stanza selezionata (a condizione che non ci siano scaffali presenti in essa)
	def eliminaStanza(self):
		#Ricavo la stanza selezionata
		stanzaSelezionata = self.stanzaVar.get()
		#Chiedo conferma di eliminare la stanza
		if stanzaSelezionata:
			scaffaliStanza = self.cantina.stanze.get(stanzaSelezionata, [])
			
			#Controllo che non ci siano scaffali nella stanza da eliminare
			if scaffaliStanza:
				messagebox.showerror("Errore", "Devi prima eliminare tutti gli scaffali presenti nella stanza!")
			else:
				conferma = messagebox.askyesno("Elimina Stanza", f"Sei sicuro di voler eliminare la stanza '{stanzaSelezionata}'? ")
				#Se sì -->
				if conferma:
					#Elimino la stanza e salvo i dati
					del self.cantina.stanze[stanzaSelezionata]
					self.stanzaMenu['values'] = list(self.cantina.stanze.keys())
					self.stanzaVar.set("")
					self.scaffaleVar.set("")
					self.salvaDati()

	#--------------------------------------
	#-------------- SCAFFALE --------------
	#--------------------------------------

	#AGGIUNGI
	#Questo metodo permette di aggiungere uno scaffale all'interno della stanza selezionata
	def aggiungiScaffale(self):
		stanzaSelezionata = self.stanzaVar.get()
		if stanzaSelezionata:
			nomeScaffale = simpledialog.askstring("Aggiungi Scaffale", "Inserire il nome dello scaffale: ")
			if nomeScaffale:
				self.cantina.aggiungiScaffale(stanzaSelezionata, nomeScaffale)
				self.visualizzaScaffali()
				self.salvaDati()
				
	#ELIMINA
	#Questo metodo permette di eliminare uno scaffale all'interno della stanza selezionata a condizione che lo scaffale sia vuoto
	def eliminaScaffale(self):
		stanzaSelezionata = self.stanzaVar.get()
		scaffaleSelezionato = self.scaffaleVar.get()
		if stanzaSelezionata and scaffaleSelezionato:
			conferma = messagebox.askyesno("Elimina Scaffale", f"Sei sicuro di voler eliminare lo scaffale '{scaffaleSelezionato}'? ")
			if conferma:
				self.cantina.eliminaScaffale(stanzaSelezionata, scaffaleSelezionato)
				self.visualizzaScaffali()
				self.scaffaleVar.set("")
				self.salvaDati()

	#VISUALIZZA
	#Questo metodo permette di visualizzare le bottiglie presenti in un detemrinato scaffale (nella rispettiva stanza)
	def visualizzaScaffali(self, event=None):
		stanzaSelezionata = self.stanzaVar.get()
		scaffaliStanza = self.cantina.stanze.get(stanzaSelezionata, [])
		self.scaffaleMenu['values'] = [scaffale.nome for scaffale in scaffaliStanza]
		self.scaffaleVar.set("")


	#--------------------------------------
	#------------- BOTTIGLIA --------------
	#--------------------------------------

	#AGGIUNGI
	#Questo metodo permette di aggiungere una bottiglia di vino allo scaffale (nella rispettiva stanza) selezionato, i dati richiesti sono: nome della bottiglia, anno della bottiglia, nome del vino e anno del vino
	def aggiungiBottiglia(self):
		#Ricavo la stanza e lo scaffale selezionati
		stanzaSelezionata = self.stanzaVar.get()
		scaffaleSelezionato = self.scaffaleVar.get()
		#Controllo che entrambi siano selezionati --> chiedo i dati
		if stanzaSelezionata and scaffaleSelezionato:
			
			#Chiedo il nome della bottiglia
			nomeBottiglia = simpledialog.askstring("Aggiungi Bottiglia", "Inserire il nome della bottiglia: ")
			if nomeBottiglia:
				#Chiedo l'anno della bottiglia
				annoBottiglia = simpledialog.askinteger("Aggiungi Bottiglia", "Inserire l'anno della bottiglia: ")
				if annoBottiglia:
					#Chiedo il nome e l'anno del vino
					nomeVino = simpledialog.askstring("Aggiungi Bottiglia", "Inserire il nome del vino: ")
					annoVino = simpledialog.askinteger("Aggiungi Bottiglia", "Inserire l'anno del vino: ")
					#Creo l'istanza di Vino e di Bottiglia
					vino = Vino(nomeVino, annoVino)
					bottiglia = Bottiglia(nomeBottiglia, annoBottiglia, vino)
					
					#Inserisco la bottiglia nello scaffale e salvo i dati
					scaffale = next((s for s in self.cantina.stanze[stanzaSelezionata] if s.nome == scaffaleSelezionato), None)
					if scaffale:
						scaffale.aggiungiBottiglia(bottiglia)
						self.salvaDati()
						
	#ELIMINA
	#Questo metodo permette di eliminare una bottiglia di vino dallo scaffale (nella rispettiva stanza) selezionato inserendo il nome della bottiglia
	def eliminaBottiglia(self):
		#Ricavo la stanza e lo scaffale selezionati
		stanzaSelezionata = self.stanzaVar.get()
		scaffaleSelezionato = self.scaffaleVar.get()
		#Controllo che entrambi siano selezionati --> scaffale
		if stanzaSelezionata and scaffaleSelezionato:
			scaffale = next((s for s in self.cantina.stanze[stanzaSelezionata] if s.nome == scaffaleSelezionato), None)
			
			#Se sì -->
			if scaffale:
				bottiglieNelloScaffale = scaffale.bottiglie
				#Controllo se ci sono bottigle nello scaffale
				if bottiglieNelloScaffale:
					
					#Chiedo il nome della bottiglia da eliminare
					bottigliaSelezionata = simpledialog.askstring("Rimuovi Bottiglia", "Inserire il nome della bottiglia da rimuovere: ")
					#Controllo che la bottiglia selezionata esista
					if bottigliaSelezionata:
						bottiglia = next((b for b in bottiglieNelloScaffale if b.nome == bottigliaSelezionata), None)
						
						#Elimino la bottiglia e salvo i dati
						if bottiglia:
							scaffale.eliminaBottiglia(bottiglia)
							self.salvaDati()

	#SPOSTA
	#Questo metodo permette di spostare una bottiglia di vino da uno scaffale (nella rispettiva stanza) ad un altro scaffale presente nella stessa stanza oppure in un'altra, i dati richiesti sono il nome della bottiglia da spostare, il nome della stanza di destinazione e il nome dello scaffale di destinazione
	def spostaBottiglia(self):
		#Ricavo la stanza e lo scaffale selezionati
		stanzaSelezionata = self.stanzaVar.get()
		scaffaleSelezionato = self.scaffaleVar.get()
		
		#Controllo che entrambi siano selezionati --> scaffale
		if stanzaSelezionata and scaffaleSelezionato:
			scaffale = next((s for s in self.cantina.stanze[stanzaSelezionata] if s.nome == scaffaleSelezionato), None)
			
			#Controllo che nello scaffale ci siano delle bottiglie
			if scaffale:
				bottiglieNelloScaffale = scaffale.bottiglie
				#Se sì -->
				if bottiglieNelloScaffale:
					
					#Chiedo il nome della bottiglia da spostare
					bottigliaSelezionata = simpledialog.askstring("Sposta Bottiglia", "Inserire il nome della bottiglia da spostare: ")
					#Controllo che la bottiglia selezionata esista
					if bottigliaSelezionata:
						bottiglia = next((b for b in bottiglieNelloScaffale if b.nome == bottigliaSelezionata), None)
						
						#Se sì -->
						if bottiglia:
						#Chiedo la stanza di destinazione (inserita)
							stanzaIns = simpledialog.askstring("Sposta Bottiglia", "Inserire il nome della stanza di destinazione: ")
							#Controllo che la stanza inserita esista
							if stanzaIns and stanzaIns in self.cantina.stanze:
								#Chiedo lo scaffale di destinazione (inserito)
								scaffaleIns = simpledialog.askstring("Sposta Bottiglia", "Inserire il nome dello scaffale di destinazione: ")
								#Controllo che lo scaffale di destinazione esista
								if scaffaleIns:
									#Vado a settare lo "scaffale di destinazione"
									scaffaleDestinazione = next((s for s in self.cantina.stanze[stanzaIns] if s.nome == scaffaleIns), None)
									
									#Sposto la bottiglia e aggiorno i dati salvati
									if scaffaleDestinazione:
										bottiglia.spostamenti.append(Spostamento(bottiglia, scaffaleDestinazione))
										scaffale.eliminaBottiglia(bottiglia)
										scaffaleDestinazione.aggiungiBottiglia(bottiglia)
										self.salvaDati()
										messagebox.showinfo("Spostamento", "Bottiglia spostata con successo!")
										
								#Messaggi di errore
									else:
										messagebox.showerror("Errore", "La scaffale indicato non esiste!")
							else:
								messagebox.showerror("Errore", "La stanza indicata non esiste!")
						else:
							messagebox.showerror("Errore", "La bottiglia indicata non esiste!")
	#VISUALIZZA
	#Questo metodo permette di visualizzare tutte le bottiglie presenti sullo scaffale selezionato (nella rispettiva stanza)
	def visualizzaBottiglie(self):
		#Ricavo la stanza e lo scaffale selezionati
		stanzaSelezionata = self.stanzaVar.get()
		scaffaleSelezionato = self.scaffaleVar.get()
		
		#Controllo che entrambi siano selezionati	
		if stanzaSelezionata and scaffaleSelezionato:
			scaffale = next((s for s in self.cantina.stanze[stanzaSelezionata] if s.nome == scaffaleSelezionato), None)
			
			#Controllo che ci siano delle bottiglie nello scaffale
			if scaffale:
				self.lista_bottiglie.delete(0, tk.END)
				
				#Stampo le bottiglie presenti nello scaffale (ciclo for)
				for bottiglia in scaffale.bottiglie:
					self.lista_bottiglie.insert(tk.END, f"{bottiglia.nome} - {bottiglia.anno}")

	#--------------------------------------
	#---------------- DATI ----------------
	#--------------------------------------

	#Carica
	def caricaDati(self):
		try:
			with open("cantina_data.pkl", "rb") as file:
				self.cantina = pickle.load(file)
		except FileNotFoundError:
			pass

	#Salva
	def salvaDati(self):
		with open("cantina_data.pkl", "wb") as file:
			pickle.dump(self.cantina, file)

	#Chiusura
	def salvaDatiChiusura(self):
		self.salvaDati()
		self.root.destroy()
#-----------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	root.protocol("WM_DELETE_WINDOW", app.salvaDatiChiusura)
	root.mainloop()
