#4C Bracco Mattia - Classe vigile

import os

class Vigile():
	#costruttore
	def __init__(self, nome, matricola, listaVeicoli=[], listaMulte=[]):
		self.setNome(nome)
		self.setMatricola(matricola)
		self.setListaVeicoli(listaVeicoli)
		self.setListaMulte(listaMulte)
		
	#setter
	def setNome(self, val):
		self.__nome = val
		
	def setMatricola(self, val):
		self.__matricola = val
		
	def setListaVeicoli(self, obj):
		self.__listaVeicoli = obj
		
	def setListaMulte(self, obj):
		self.__listaMulte = obj
		
	#getter
	def getNome(self):
		return self.__nome
	
	def getMatricola(self):
		return self.__matricola
		
	def getListaVeicoli(self):
		return self.__listaVeicoli
		
	def getListaMulte(self):
		return self.__listaMulte
		
	#str
	def presentati(self):
		print('VIGILE nome: {0} Matricola: {1}'.format(self.getNome(), self.getMatricola()))
		
		
# ***** EFFETTUA MULTA *****
	def effettuaMulta(self, nuovo):
	
		#estrapolo la lista dele multe
		lista = self.getListaMulte()
		#aggiungo il nuovo veicolo alla lista
		lista.append(nuovo) 
		#imposto la lista
		self.setListaMulte(lista)
	
# ***** ELIMINA MULTA *****
	def eliminaMulta(self, numVerbale):
		lista = self.getListaMulte()
		N = len(lista)
		flag = 0
		
		#se lunghezza = 0 --> nessun veicolo --> messaggio di errore
		if N == 0:
			print("Nessuna multa registrata!")
		
		#ciclo per il numero di multe presenti nella lista
		for i in range(N):
			if numVerbale == lista[i].getNumero():
				flag = 1
				pos = i
		
		#se verbale non trovato (flag vale 0) --> messaggio di errore
		if flag == 0:
			print("Verbale non trovato!")
		#se verbale trovato --> lo elimino
		else:
			print("Procedo a rimuovere la multa...")
			#elimino la multa
			lista.pop[i]
			#imposto la lista
			self.setListaMulte(lista)
		
# ***** LISTA MULTE *****
	def stampaListaMulte(self):
 		lista = self.getListaMulte()
 		N = len(lista)
 		
 		#se lunghezza = 0 --> nessun veicolo --> messaggio di errore
 		if N == 0:
 			print("Nessuna multa registrata!")
 			
 		#stampo le multe
 		for i in range (N):
 			print(lista[i].dettagli())
		
# ***** LISTA VEICOLI *****
	def stampaListaVeicoli(self):
 		lista = self.getListaVeicoli()
 		N = len(lista)
 		
 		#se lunghezza = 0 --> nessun veicolo --> messaggio di errore
 		if N == 0:
 			print("Nessun veicolo registrato!")
 			
 		#stampo i veicoli
 		for i in range (N):
 			print(lista[i].dettagli())
 			
# ***** TROVA VEICOLO *****
	def trovaVeicolo(self, targaIns):
		
		#determino il numero di veicoli presenti nella lista
		flag = 0
		lista = self.getListaVeicoli()
		N = len(lista)
		
		#ciclo per il numero di veicoli
		for i in range(N):
			if targaIns == lista[i].getTarga():
				flag = 1
				print(lista[i].dettagli())
				return lista[i]		
				
		#se veicolo non trovato (flag vale 0) --> messaggio di errore
		if flag == 0:
			print("Il veicolo cercato non è presente nel nostro archivio!")
			return 0
		
# ***** AGGIUNGI VEICOLO *****
	def aggiungiVeicolo(self, nuovo):
			
		#estrapolo la lista dei veicoli
		lista = self.getListaVeicoli()
		#aggiungo il nuovo veicolo alla lista
		lista.append(nuovo) 
		#imposto la lista
		self.setListaVeicoli(lista)
		
# ***** CONTROLLO MULTE *****
	def controlloMulte(self, targaIns):
		lista = self.getListaMulte()
		N = len(lista)
		flag = 0
		
		#ciclo per il numero di multe nella lista
		for i in range(N):
			#se la targa inserita corrisponde a quella della multa incremento il flag
			if targaIns == lista[i].getVeicolo().getTarga():
				flag += 1
				
		#restituisco il valore booleano della ricerca
		if flag > 1:
			return True
		else:
			return False
			
# ***** CONTROLLO TARGA UNIVOCA *****
	def controlloTargaUnivoca(self, targaIns):
		lista = self.getListaVeicoli()
		N = len(lista)
		flag = 0
		
		#ciclo per il numero di veicoli nella lista
		for i in range(N):
			#se la targa corrisponde (già presente) --> flag = 1
			if targaIns == lista[i].getTarga():
				flag = 1
				print("ERRORE! Targa già registrata")	
		return flag		
#-------------------------------------------------------------------------------------------------------------------------------------
class Veicolo():
	#costruttore
	def __init__(self, targa, potenza):
		self.setTarga(targa)
		self.setPotenza(potenza)
		
	#setter
	def setTarga(self, val):
		self.__targa = val
		
	def setPotenza(self, val):
		self.__potenza = val
	
	#getter
	def getTarga(self):
		return self.__targa
	
	def getPotenza(self):
		return self.__potenza
		
	#str
	def dettagli(self):
		print('VEICOLO: Targa: {0} Potenza: {1} CV'.format(self.getTarga(), self.getPotenza()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Auto(Veicolo):
	#costruttore
	def __init__(self, targa, potenza, tipo, marca, modello):
		super().__init__(targa, potenza)
		self.setMarca(marca)
		self.setModello(modello)
		self.setTipo(tipo)
		
	#setter
	def setMarca(self, val):
		self.__marca = val
		
	def setModello(self, val):
		self.__modello = val
		
	def setTipo(self, val):
		self.__tipo = val
	
	#getter
	def getMarca(self):
		return self.__marca
		
	def getModello(self):
		return self.__modello
		
	def getTipo(self):
		return self.__tipo
		
	#str
	def dettagli(self):
		print("Tipo: {:4s} Targa: {:7s} Potenza: {:3d} CV Marca: {:7s} Modello: {:7s}".format(self.getTipo(), self.getTarga(), self.getPotenza(), self.getMarca(), self.getModello()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Moto(Veicolo):
	#costruttore
	def __init__(self, targa, potenza, tipo, marca, modello):
		super().__init__(targa, potenza)
		self.setMarca(marca)
		self.setModello(modello)
		self.setTipo(tipo)
		
	#setter
	def setMarca(self, val):
		self.__marca = val
		
	def setModello(self, val):
		self.__modello = val

	def setTipo(self, val):
		self.__tipo = val
	
	#getter
	def getMarca(self):
		return self.__marca
		
	def getModello(self):
		return self.__modello

	def getTipo(self):
		return self.__tipo

	#str
	def dettagli(self):
		print("Tipo: {:4s} Targa: {:7s} Potenza: {:3d} CV Marca: {:7s} Modello: {:7s}".format(self.getTipo(), self.getTarga(), self.getPotenza(), self.getMarca(), self.getModello()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Multa():
	#costruttore
	def __init__(self, numero, luogo, veicolo):
		self.setNumero(numero)
		self.setLuogo(luogo)
		self.setVeicolo(veicolo)

	#setter
	def setNumero(self, val):
		self.__numero = val
		
	def setLuogo(self, val):
		self.__luogo = val

	def setVeicolo(self, obj):
		self.__veicolo = obj
	
	#getter
	def getNumero(self):
		return self.__numero
		
	def getLuogo(self):
		return self.__luogo

	def getVeicolo(self):
		return self.__veicolo
		
	#str
	def dettagli(self):
		print('Numero verbale: {0} Luogo: {1} Targa: {2}'.format(self.getNumero(), self.getLuogo(), self.getVeicolo().getTarga()))
#-------------------------------------------------------------------------------------------------------------------------------------
def insNome():
	#chiedo e controlllo il nome del vigile
	val = input("Inserire il nome del vigile: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il nome del vigile: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------
def insMatricola():
	#chiedo e controlllo la matricola
	val = input("Inserire matricola del vigile: ")
	while val.isspace():
		val = input("ERRORE! Inserire la matricola del vigile: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------	
def insTarga():
	#chiedo in input la targa e controllo il formato
	targa = input("Inserire la targa: ")
	while (len(targa) != 7 or targa[0].isnumeric() or targa[1].isnumeric() or targa[2].isalpha() or targa[3].isalpha() or targa[4].isalpha() or targa[5].isnumeric() or targa[6].isnumeric()):
			targa = input("ERRORE! (formato targa non valido, es. formato valido AA001AA)\nInserire la targa del veicolo: ")
	
	#restituisco il valore (stringa)
	return targa
#------------------------------------------------------------------------------------------------------------------------------------
def insPotenza():
	#chiedo e controllo la potenza
	val = input("Inserire la potenza del veicolo (CV): ")
	while (not val.isnumeric() or int(val) < 10 or int(val) > 900):
		val = input("ERRORE! Inserire la potenza del veicolo (CV): ")
	
	#restituisco il valore (intero)
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------	
def insTipo():
	#chiedo e controllo il tipo di veicolo
	val = input("Inserire il tipo di veicolo (A = AUTO / M = MOTO): ")
	while (val != 'A' and val != 'a' and val != 'M' and val != 'm'):
		val = input("ERRORE! Inserire il tipo di veicolo (A = AUTO / M = MOTO): ")
	#a / A --> Auto
	if (val == 'a' or val == 'A'):
		res = "Auto"
	#m / M --> Moto
	if (val == 'm' or val == 'M'):
		res = "Moto"
	
	#restituisco il valore (boolean)
	return res
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
def insLuogo():
	#chiedo e controlllo il luogo
	val = input("Inserire il luogo: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il luogo: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------
def insNum():
	#chiedo e controlllo il numero
	val = input("Inserire il numero di verbale: ")
	while (not val.isnumeric() or int(val) < 0 or int(val) > 100):
		val = input("ERRORE! Inserire il numero di verbale: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------
os.system("clear")
numero = 1

#CREO UN VIGILE
nome = insNome()
matricola = insMatricola()
mioVigile = Vigile (nome, matricola)

uscita = 0;
while uscita == 0:
	print(" ____________________________ ")
	print("|                            |")
	print("|     MENÙ DELLE OPZIONI     |")
	print("|____________________________|")
	print("|                            |")
	print("|1- EFFETTUA MULTA           |")
	print("|2- ELIMINA MULTA            |")
	print("|3- LISTA MULTE              |")
	print("|4- LISTA VEICOLI REGISTRATI |")
	print("|5- TROVA VEICOLO            |")
	print("|6- AGGIUNGI VEICOLO         |")
	print("|7- MULTE VEICOLO > 1?       |")
	print("|8- EXIT                     |")
	print("|____________________________|")	
	opzione = input("\nScegliere una delle opzioni: ")
	
	#CONTROLLO OPZIONE INSERITA
	while not opzione.isnumeric() or opzione.isspace() or int(opzione) < 1 or int(opzione) > 8:
		opzione = input("ERRORE! Scegliere una delle opzioni: ")
	opzione = int(opzione) #casting effettuato dopo il while in modo da evitare errori
	os.system("clear")
	
	#OPZIONE 1 --> EFFETTUA MULTA
	if opzione == 1:
		print(" ____________________________ ")
		print("|                            |")
		print("|       EFFETTUA MULTA       |")
		print("|____________________________|")
		#chiedo i dati
		print("Numero verbale: " + str(numero))
		luogo = insLuogo()
		targaIns = insTarga()
		veicolo = mioVigile.trovaVeicolo(targaIns)
		
		#se il veicolo è stato trovato --> multa
		if veicolo != 0:
			#creo una multa e l'aggiungo alla lista
			nuovaMulta = Multa (numero, luogo, veicolo)
			mioVigile.effettuaMulta(nuovaMulta)
			numero += 1 #aumento il numero progressivo dei verbali
	
	#OPZIONE 2 --> ELIMINA MULTA
	if opzione == 2:
		print(" ____________________________ ")
		print("|                            |")
		print("|       ELIMINA MULTA        |")
		print("|____________________________|")
		#chiedo il numero di verbale da eliminare ed elimino la multa
		numVerbale = insNum()
		mioVigile.eliminaMulta(numVerbale)
		
	#OPZIONE 3 --> LISTA MULTE
	if opzione == 3:
		print(" ____________________________ ")
		print("|                            |")
		print("|        LISTA MULTE         |")
		print("|____________________________|")
		#stampo la lista delle multe
		mioVigile.stampaListaMulte()
		
	#OPZIONE 4 --> LISTA VEICOLI REGISTRATI
	if opzione == 4:
		print(" ____________________________ ")
		print("|                            |")
		print("|       LISTA VEICOLI        |")
		print("|____________________________|")
		#stampo la lista dei veicoli
		mioVigile.stampaListaVeicoli()
		
	#OPZIONE 5 --> CERCA VEICOLO
	if opzione == 5:
		print(" ____________________________ ")
		print("|                            |")
		print("|       TROVA VEICOLO        |")
		print("|____________________________|")
		#chiedo una targa
		targaIns = insTarga()
		
		#cerco il veicolo
		mioVigile.trovaVeicolo(targaIns)
		
	#OPZIONE 6 --> AGGIUNGI VEICOLO
	if opzione == 6:
		print(" ____________________________ ")
		print("|                            |")
		print("|      AGGIUNGI VEICOLO      |")
		print("|____________________________|")
		#chiedo i dati del veicolo
		targa = insTarga()
		#ciclo finchè la targa non è univoca (non ancora registrata)
		while mioVigile.controlloTargaUnivoca(targa) != 0:
				targa = insTarga()
		potenza = insPotenza()
		tipo = insTipo()
		marca = insCasa()
		modello = insModello()
		
		#se tipo = moto --> creo una moto
		if tipo == "Moto":
			nuovoVeicolo = Moto(targa, potenza, tipo, marca, modello)
		#se tipo = auto --> creo un auto
		if tipo == "Auto":
			nuovoVeicolo = Auto(targa, potenza, tipo, marca, modello)
		
		#aggiungo il nuovo veicolo
		mioVigile.aggiungiVeicolo(nuovoVeicolo)
		
	#OPZIONE 7 --> CONTROLLO BOOLEAN MULTE > 1
	if opzione == 7:
		print(" ____________________________ ")
		print("|                            |")
		print("|    CONTROLLO MULTE > 1?    |")
		print("|____________________________|")
		#chiedo i dati del veicolo e controllo
		targaIns = insTarga()
		ris = mioVigile.controlloMulte(targaIns)
		print(ris)
		
	#OPZIONE 8 --> ESCO
	if opzione == 8:
		print("ESCO DAL PROGRAMMA!")
		uscita = 1
		
	#pulizia dello schermo (tranne nel caso in cui l'utente esca dal programma)
	if opzione != 8:
		input("Premi INVIO per continuare...")
		os.system("clear")
