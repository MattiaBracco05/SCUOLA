#4C Bracco Mattia - Classe automezzi

import os

MIN = 1
MAX = 5
#------------------------------------------------------------------------------------------------------------------------------------
class Autoveicolo():
	#costruttore
	def __init__(self, targa="", casa="", modello=""):
		self.setTarga(targa)
		self.setCasa(casa)
		self.setModello(modello)
	
	#setter
	def setTarga(self, val):
		self.__targa = val
		
	def setCasa(self, val):
		self.__casa = val
	
	def setModello(self, val):
		self.__modello = val
		
	#getter
	def getTarga(self):
		return self.__targa
	
	def getCasa(self):
		return self.__casa
	
	def getModello(self):
		return self.__modello
		
	#str
	def dettagli(self):
		print('Targa: {0} Casa automobilistica: {1} Modello: {2}'.format(self.getTarga(), self.getCasa(), self.getModello()))
#------------------------------------------------------------------------------------------------------------------------------------
class VeicoloPrivato(Autoveicolo):
	#costruttore
	def __init__(self, targa, casa, modello, numeroPorte="", numeroPosti=""):
		super().__init__(targa, casa, modello)
		self.setNumeroPorte(numeroPorte)
		self.setNumeroPosti(numeroPosti)
	
	#setter
	def setNumeroPorte(self, val):
		self.__numeroPorte = val
	
	def setNumeroPosti(self, val):
		self.__numeroPosti = val
		
	#getter
	def getNumeroPorte(self):
		return self.__numeroPorte
	
	def getNumeroPosti(self):
		return self.__numeroPosti
		
	#str
	def dettagli(self):
		print('VEICOLO PRIVATO: Targa: {0} Casa: {1} Modello: {2} Porte: {3} Posti: {4}'.format(self.getTarga(), self.getCasa(), self.getModello(), self.getNumeroPorte(), self.getNumeroPosti()))
#------------------------------------------------------------------------------------------------------------------------------------
class VeicoloCommerciale(Autoveicolo):
	#costruttore
	def __init__(self, targa, casa, modello, pesoVuoto="", pesoCarico="", articolato=False):
		super().__init__(targa, casa, modello)
		self.setPesoVuoto(pesoVuoto)
		self.setPesoCarico(pesoCarico)
		self.setArticolato(articolato)
	
	#setter
	def setPesoVuoto(self, val):
		self.__pesoVuoto = val
	
	def setPesoCarico(self, val):
		self.__pesoCarico = val
		
	def setArticolato(self, val):
		self.__articolato = val
		
	#getter
	def getPesoVuoto(self):
		return self.__pesoVuoto
	
	def getPesoCarico(self):
		return self.__pesoCarico
		
	def getArticolato(self):
		return self.__articolato
	
	#str
	def dettagli(self):
		print('VEICOLO COMMERCIALE: Targa: {0} Casa: {1} Modello: {2} Peso vuoto: {3} Peso carico: {4} Articolato {5}'.format(self.getTarga(), self.getCasa(), self.getModello(), self.getPesoVuoto(), self.getPesoCarico(), self.getArticolato()))
#------------------------------------------------------------------------------------------------------------------------------------
class Concessionaria():
	#costruttore
	def __init__(self, nome, lista):
		self.setNome(nome)
		self.setLista(lista)
	
	#setter
	def setNome(self, val):
		self.__nome = val

	def setLista(self, lis):
		self.__lista = lis
	
	#getter
	def getNome(self):
		return self.__nome
		
	def getLista(self):
		return self.__lis
	
	#str
	def dettagli(self):
		printf('CONCESSIONARIA: {0}'.format(self.getNome()))
		
#	***** COMPRA VEICOLO *****
	def compraVeicolo(self, targa, listaAutoveicoli, listaVeicoliConcessionaria):
		flag = 0
		#ciclo per il numero di veicoli
		n = len(listaAutoveicoli)
		for i in range(n):
		
			#se la targa corrisponde --> compro il veicolo
			if (targa == listaAutoveicoli[i].getTarga()):
				listaVeicoliConcessionaria.append(listaAutoveicoli[i-1])
				listaAutoveicoli.pop(i-1)
				flag = 1
				print("VEICOLO COMPRATO!")
			
		#restituisco il flag
		return flag
		
#	***** VENDI VEICOLO *****
	def vendiVeicolo(self, targa, listaVeicoliConcessionaria):
		flag = 0
		#ciclo per il numero di veicoli
		n = len(listaVeicoliConcessionaria)
		for i in range(n):
		
			#se la targa corrisponde --> vendo il veicolo
			if (targa == listaVeicoliConcessionaria[i].getTarga()):
				listaVeicoliConcessionaria.pop(i-1)
				flag = 1
				print("VEICOLO VENDUTO!")
			
		#restituisco il flag
		return flag
		
# ***** STAMPA VEICOLI *****
	def stampaVeicoli(self, listaVeicoliConcessionaria, listaAutoveicoli):
		print(" ____________________________ ")
		print("|                            |")
		print("|   VEICOLI CONCESSIONARIA   |")
		print("|____________________________|")
		n = len(listaVeicoliConcessionaria)
		for i in range(n):
			print(listaVeicoliConcessionaria[i].dettagli())
		
		print(" ____________________________ ")
		print("|                            |")
		print("|       VEICOLI NUOVI        |")
		print("|____________________________|")
		n = len(listaAutoveicoli)
		for i in range(n):
			print(listaAutoveicoli[i].dettagli())	
#------------------------------------------------------------------------------------------------------------------------------------
def insNVeicoli():
	#chiedo quanti veicoli registrare e controllo il valore
	val = input("Quanti veicoli di questo tipo si vogliono registrare? (" + str(MIN) + "-" + str(MAX) + "): ")
	while (not val.isnumeric() or int(val) < MIN or int(val) > MAX):
		val = input("ERRORE! Quanti veicoli di questo si volgiono registrare? (" + str(MIN) + "-" + str(MAX) + "):")
	
	#restituisco il valore (intero)
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------
def insTarga():
	#chiedo in input la targa e controllo il formato
	targa = input("Inserire la targa: ")
	while (len(targa) != 7 or targa[0].isnumeric() or targa[1].isnumeric() or targa[2].isalpha() or targa[3].isalpha() or targa[4].isalpha() or targa[5].isnumeric() or targa[6].isnumeric()):
			targa = input("ERRORE! (formato targa non valido, es. formato valido AA001AA)\nInserire la targa del veicolo: ")
	
	#restituisco il valore (stringa)
	return targa
#------------------------------------------------------------------------------------------------------------------------------------
def insCasa():
	#chiedo e controlllo il nome della casa automobilistica
	val = input("Inserire il nome della casa automobilistica: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il nome della casa automobilistica: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------
def insModello():
	#chiedo e controlllo il nome del modelli
	val = input("Inserire il modello dell'autoveicolo: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il modello dell'autoveicolo: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------
def insPeso():
	#chiedo e controllo il peso
	val = input("Inserire il peso: ")
	while (not val.isnumeric() or int(val) < 1000 or int(val) > 10000):
		val = input("ERRORE! Inserire il peso: ")
	
	#restituisco il valore (intero)
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------
def insArticolato():
	#chiedo e controllo se il veicolo è articolato
	val = input("Il veicolo è articolato? (S/N): ")
	while (val != 'S' and val != 's' and val != 'n' and val != 'N'):
		val = input("ERRORE! Il veicolo è articolato?? (S/N): ")
	#se si --> True
	if (val == 's' or val == 'S'):
		res = True
	#se no --> False
	if (val == 'n' or val == 'N'):
		res = False
	
	#restituisco il valore (boolean)
	return res
#------------------------------------------------------------------------------------------------------------------------------------
def insNPorte():
	#chiedo e controllo il numero di porte
	val = input("Inserire il numero di porte: ")
	while (not val.isnumeric() or int(val) < 3 or int(val) > 5):
		val = input("ERRORE! Inserire il numero di porte: ")
	
	#restituisco il valore (intero)
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------
def insNPosti():
	#chiedo e controllo il numero di porte
	val = input("Inserire il numero di posti: ")
	while (not val.isnumeric() or int(val) < 2 or int(val) > 9):
		val = input("ERRORE! Inserire il numero di posti: ")
	
	#restituisco il valore (intero)
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------
def insNome():
	#chiedo e controlllo il nome della concessionaria
	val = input("Inserire il nome della concessionaria: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il nome della concessionaria: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------	
os.system("clear")
listaAutoveicoli = []
listaVeicoliConcessionaria = []

#chiedo quanti veicoli registrare
print("veicoli commerciali")
N_VEICOLI_COMMERCIALI = insNVeicoli()
print("veicoli privati")
N_VEICOLI_PRIVATI = insNVeicoli()
os.system("clear")

#registro i VEICOLI COMMERCIALI
for i in range(N_VEICOLI_COMMERCIALI):
	print(" ____________________________ ")
	print("|                            |")
	print("|    VEICOLO COMMERCIALE     |")
	print("|____________________________|")
	targa = insTarga()
	casa = insCasa()
	modello = insModello()
	print("peso veicolo vuoto")
	pesoVuoto = insPeso()
	print("peso veicolo carico")
	pesoCarico = insPeso()
	articolato = insArticolato()
	
	#creo il veicolo
	nuovoVeicolo = VeicoloCommerciale (targa, casa, modello, pesoVuoto, pesoCarico, articolato)
	
	#lo aggiungo alla lista
	listaAutoveicoli.append(nuovoVeicolo)
	
	#pulisco lo schermo
	os.system("clear")
	
#registro i VEICOLI PRIVATI
for i in range(N_VEICOLI_PRIVATI):
	print(" ____________________________ ")
	print("|                            |")
	print("|      VEICOLO PRIVATO       |")
	print("|____________________________|")
	targa = insTarga()
	casa = insCasa()
	modello = insModello()
	porte = insNPorte()
	posti = insNPosti()
	
	#creo il veicolo
	nuovoVeicolo = VeicoloPrivato (targa, casa, modello, porte, posti)
	
	#lo aggiungo alla lista
	listaAutoveicoli.append(nuovoVeicolo)
	
	#pulisco lo schermo
	os.system("clear")

#CONCESSIONARIA
nome = insNome()
miaConcessionaria = Concessionaria (nome, listaVeicoliConcessionaria)

#ciclo finchè l'utente non decide di uscire
uscita = 0
while uscita == 0:
	print(" ____________________________ ")
	print("|                            |")
	print("|     MENÙ DELLE OPZIONI     |")
	print("|____________________________|")
	print("|                            |")
	print("|1- COMPRA VEICOLO           |")
	print("|2- VENDI VEICOLO            |")
	print("|3- STAMPA VEICOLI           |")
	print("|4- EXIT                     |")
	print("|____________________________|")	
	opzione = input("\nScegliere una delle opzioni: ")
	
	#CONTROLLO OPZIONE INSERITA
	while not opzione.isnumeric() or opzione.isspace() or int(opzione) < 1 or int(opzione) > 4:
		opzione = input("ERRORE! Scegliere una delle opzioni: ")
	opzione = int(opzione) #casting effettuato dopo il while in modo da evitare errori
	os.system("clear")
	
	#OPZIONE 1 --> COMPRA UN VEICOLO
	if opzione == 1:
		#chiedo la targa di un veicolo
		targaIns = insTarga()
		
		#richiamo il metodo per comprare il veicolo
		flag = miaConcessionaria.compraVeicolo(targa, listaAutoveicoli, listaVeicoliConcessionaria)
	
		#se flag rimane a 0 --> veicolo non trovato
		if flag == 0:
			print("Veicolo non trovato!")
	
		#PULIZIA DELLO SCHERMO
		input("Premi INVIO per continuare...")
		os.system("clear")
	
	#OPZIONE 2 --> VENDO UN VEICOLO
	if opzione == 2:
		#chiedo la targa di un veicolo
		targaIns = insTarga()
		
		#richiamo il metodo per vendere il veicolo
		flag = miaConcessionaria.vendiVeicolo(targa, listaVeicoliConcessionaria)
	
		#se flag rimane a 0 --> veicolo non trovato
		if flag == 0:
			print("Veicolo non trovato!")
	
		#PULIZIA DELLO SCHERMO
		input("Premi INVIO per continuare...")
		os.system("clear")
	
	#OPZIONE 3 --> STAMPA
	if opzione == 3:
		miaConcessionaria.stampaVeicoli(listaVeicoliConcessionaria, listaAutoveicoli)
		
		#PULIZIA DELLO SCHERMO
		input("Premi INVIO per continuare...")
		os.system("clear")
	
	#OPZIONE 4 --> ESCO	
	if opzione == 4:
		print("ESCO DAL PROGRAMMA!")
		uscita = 1
