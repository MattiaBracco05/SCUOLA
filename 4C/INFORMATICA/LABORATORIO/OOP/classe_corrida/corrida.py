#Correzione verifica classi

import os

class Esibizione():
	#costruttore
	def __init__(self, titolo, durata):
		self.setTitolo(titolo)
		self.setDurata(durata)
		
	#setter
	def setTitolo(self, val):
		self.__titolo = val
	
	def setDurata(self, val):
		self.__durata = val
		
	#getter
	def getTitolo(self):
		return self.__titolo
	
	def getDurata(self):
		return self.__durata
	
	#dettagli
	def dettagli(self):
		print('ESIBIZIONE Titolo: {0} Durata: {1}'.format(self.getTitolo(), self.getDurata()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Canto(Esibizione):
	#costruttore
	def __init__(self, titolo, durata, genere):
		super().__init__(titolo, durata)
		self.setGenere(genere)
		
	#setter
	def setGenere(self, val):
		self.__genere = val
		
	#getter
	def getGenere(self):
		return self.__genere
		
	#dettagli
	def dettagli(self):
		print('CANTO Titolo: {0} Durata: {1} Genere: {2}'.format(self.getTitolo(), self.getDurata(), self.getGenere()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Ginnastica(Esibizione):
	#costruttore
	def __init__(self, titolo, durata, attrezzo):
		super().__init__(titolo, durata)
		self.setAttrezzo(attrezzo)
		
	#setter
	def setAttrezzo(self, val):
		self.__attrezzo = val
		
	#getter
	def getAttrezzo(self):
		return self.__attrezzo
		
	#dettagli
	def dettagli(self):
		print('GINNASTICA Titolo: {0} Durata: {1} Attrezzo: {2}'.format(self.getTitolo(), self.getDurata(), self.getAttrezzo()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Poesia(Esibizione):
	#costruttore
	def __init__(self, titolo, durata):
		super().__init__(titolo, durata)
		
	#dettagli
	def dettagli(self):
		print('POESIA Titolo: {0} Durata: {1}'.format(self.getTitolo(), self.getDurata()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Manifestazione():
	def __init__(self, nome, listaPartecipanti=[], elencoCantanti={}, elencoGinnasti={}, elencoPoeti={}):
		self.setNome(nome)
		self.setListaPartecipanti(listaPartecipanti)
		self.setElencoCantanti(elencoCantanti)
		self.setElencoGinnasti(elencoGinnasti)
		self.setElencoPoeti(elencoPoeti)
		
	#setter
	def setNome(self, val):
		self.__nome = val
	
	def setListaPartecipanti(self, lis):
		self.__listaPartecipanti = lis
		
	def setElencoCantanti(self, diz):
		self.__elencoCantanti = diz
		
	def setElencoGinnasti(self, diz):
		self.__elencoGinnasti = diz
		
	def setElencoPoeti(self, diz):
		self.__elencoPoeti = diz
		
	#getter
	def getNome(self):
		return self.__nome
		
	def getListaPartecipanti(self):
		return self.__listaPartecipanti
		
	def getElencoCantanti(self):
		return self.__elencoCantanti
		
	def getElencoGinnasti(self):
		return self.__elencoGinnasti
		
	def getElencoPoeti(self):
		return self.__elencoPoeti
		
	#dettagli
	def dettagli(self):
		print('MANIFESTAZIONE Nome: {0}'.format(self.getNome()))
#	CONTROLLO UNIVOCO
	def controlloUnivoco(self, nomeIns, cognomeIns):
		lista = self.getListaPartecipanti()
		flag = 0
		#ciclo per il numero dei partecipanti già registrato
		for i in range(len(lista)):
			if (nomeIns == lista[i].getNome()) and (cognomeIns == lista[i].getCognome):
				print("Partecipante già registrato!")
				flag = 1
		return flag
		
#	AGGIUNGI PARTECIPANTE
	def aggiungiPartecipante(self, nuovoPartecipante):
		#lo aggiungo alla lista dei partecipanti
		lista = self.getListaPartecipanti()
		lista.append(nuovoPartecipante)
		self.setListaPartecipanti(lista)
		
		#lo aggiungo all'eventuale dizionario
		if nuovoPartecipante.getTipologia() == 'cantante' or nuovoPartecipante.getTipologia() == 'CANTANTE':
			diz = self.getElencoCantanti()
		if nuovoPartecipante.getTipologia() == 'ginnasta' or nuovoPartecipante.getTipologia() == 'GINNASTA':
			diz = self.getElencoGinnasti()
		if nuovoPartecipante.getTipologia() == 'poeta' or nuovoPartecipante.getTipologia() == 'POETA':
			diz = self.getElencoPoeti()
#-------------------------------------------------------------------------------------------------------------------------------------
class Partecipante():
	#costruttore
	def __init__(self, nome, cognome, sesso, eta, tipologia):
		self.setNome(nome)
		self.setCognome(cognome)
		self.setSesso(sesso)
		self.setEta(eta)
		self.setTipologia(tipologia)
		
	#setter
	def setNome(self, val):
		self.__nome = val
		
	def setCognome(self, val):
		self.__cognome = val
		
	def setSesso(self, val):
		self.__sesso = val
		
	def setEta(self, val):
		self.__eta = val
		
	def setTipologia(self, val):
		self.__tipologia = val
	
	#getter
	def getNome(self):
		return self.__nome
		
	def getCognome(self):
		return self.__cognome
		
	def getSesso(self):
		return self.__sesso
		
	def getEta(self):
		return self.__eta
		
	def getTipologia(self):
		return self.__tipologia
		
	#dettagli
	def dettagli(self):
		print("PARTECIPANTE Nome: {:10s} Cognome: {:10s} Sesso: {:1s} Eta: {:2d} Tipologia: {:10s}".format(self.getNome(), self.getCognome(), self.getSesso(), self.getEta(), self.getTipologia()))
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def insNomeManifestazione():
	#chiedo e controlllo il nome
	val = input("Inserire il nome della manifestazione: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il nome della manifestazione: ")
	
	#restituisco il valore (stringa)
	return val
#-------------------------------------------------------------------------------------------------------------------------------------
def insNome():
	#chiedo e controlllo il nome
	val = input("Inserire il nome: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il nome: ")
	
	#restituisco il valore (stringa)
	return val
#-------------------------------------------------------------------------------------------------------------------------------------
def insCognome():
	#chiedo e controlllo il cognome
	val = input("Inserire il cognome: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il cognome: ")
	
	#restituisco il valore (stringa)
	return val
#-------------------------------------------------------------------------------------------------------------------------------------
def insSesso():
	#chiedo e controlllo il sesso
	val = input("Inserire il sesso (M/F): ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace() or (val != "M" and val != 'm' and val != 'F' and val != 'F'):
		val = input("ERRORE! Inserire il sesso (M/F): ")
	
	#restituisco il valore (stringa)
	return val
#-------------------------------------------------------------------------------------------------------------------------------------
def insEta():	
	#chiedo e controlllo l'età
	val = input("Inserire l'età: ")
	while (not val.isnumeric() or int(val) < 1 or int(val) > 100):
		val = input("ERRORE! Inserire l'età: ")
	
	#restituisco il valore (int)
	return val
#-------------------------------------------------------------------------------------------------------------------------------------
def insTipologia():
	#chiedo e controlllo la tipologia
	val = input("Inserire la tipologia (NESSUNO/CANTANTE/GINNASTA/POETA): ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace() or (val != 'NESSUNO' and val != 'nessuno' and val != 'CANTANTE' and val != 'cantante' and val != 'GINNASTA' and val != 'ginnasta' and val != 'POETA' and val != 'poeta'):
		val = input("ERRORE! Inserire la tipologia (NESSUNO/CANTANTE/GINNASTA/POETA): ")
	
	#restituisco il valore (stringa)
	return val
#-------------------------------------------------------------------------------------------------------------------------------------
os.system("clear")

#CREO LA MANIFESTAZIONE
nomeManifestazione = insNomeManifestazione()
miaManifestazione = Manifestazione (nomeManifestazione)

uscita = 0;
while uscita == 0:
	print(" ____________________________ ")
	print("|                            |")
	print("|     MENÙ DELLE OPZIONI     |")
	print("|____________________________|")
	print("|                            |")
	print("|1- AGGIUNGI PARTECIPANTE    |")
	print("|2- TROVA PARTECIPANTE       |")
	print("|3- ELIMINA PARTECIPANTE     |")
	print("|4- STAMPA PARTECIPANTI      |")
	print("|5- STAMPA ESIBIZIONI        |")
	print("|6- EXIT                     |")
	print("|____________________________|")	
	opzione = input("\nScegliere una delle opzioni: ")
	
	#CONTROLLO OPZIONE INSERITA
	while not opzione.isnumeric() or opzione.isspace() or int(opzione) < 1 or int(opzione) > 6:
		opzione = input("ERRORE! Scegliere una delle opzioni: ")
	opzione = int(opzione) #casting effettuato dopo il while in modo da evitare errori
	os.system("clear")
	
	#OPZIONE 1 --> AGGIUNGI PARTECIPANTE
	if opzione == 1:
		print(" ____________________________ ")
		print("|                            |")
		print("|   AGGIUNGI PARTECIPANTE    |")
		print("|____________________________|")
		
		#chiedo i dati
		flag = 1
		while flag == 1:
			nome = insNome()
			cognome = insCognome()
			flag = miaManifestazione.controlloUnivoco(nome, cognome)
		sesso = insSesso()
		eta = insEta() 
		tipologia = insTipologia()
		
		#creo il partecipante
		nuovoPartecipante = Partecipante (nome, cognome, sesso, eta, tipologia)
	
		#aggiungo il nuovo partecipante
		miaManifestazione.aggiungiPartecipante(nuovoPartecipante)
		
	#PULIZIA DELLO SCHERMO
	if opzione != 7:
		os.system("clear")
