#4C Bracco Mattia - Classe studenti

import os

MIN_STUD = 2
MAX_STUD = 25
#------------------------------------------------------------------------------------------------------------------------------------
class Persona(object):
	#costruttore
	def __init__(self, cognome="", nome="", eta=0):
		self.setNome(nome)
		self.setCognome(cognome)
		self.setEta(eta)
	
	#setter
	def setNome(self, val):
		self.__nome = val
		
	def setCognome(self, val):
		self.__cognome = val
	
	def setEta(self, val):
		self.__eta = val
		
	#getter
	def getNome(self):
		return self.__nome
	
	def getCognome(self):
		return self.__cognome
	
	def getEta(self):
		return self.__eta
		
	#str
	def presentati(self):
		print('Cognome: {0} Nome: {1} Età: {2}'.format(self.getCognome(), self.getNome(), self.getEta()))
#------------------------------------------------------------------------------------------------------------------------------------
class Studente(object):
	#costruttore
	def __init__(self, persona, voti=[]):
		self.setPersona(persona)
		self.setVoti(voti)
	
	#setter
	def setPersona(self, obj):
		self.__persona = obj
		
	def setVoti(self, lis):
		self.__voti = lis
		
	#getter
	def getPersona(self):
		return self.__persona
		
	def getVoti(self):
		return self.__voti
		
	#str
	def presentati(self):
		print('Cognome: {0} Nome: {1} Età: {2} Voti: {3}'.format(self.getPersona().getCognome(), self.getPersona().getNome(), self.getPersona().getEta(), self.getVoti()))
#------------------------------------------------------------------------------------------------------------------------------------
class GruppoClasse(object):
	#costruttore
	def __init__(self, studN=[]):
		self.setStudN(studN)
	
	#setter
	def setStudN(self, lis):
		self.__studN = lis
		
	#getter
	def getStudN(self):
		return self.__studN
	
	#str
	def stampa(self):
		for i in range (N):
			print(str(self.getStudN()[i].presentati()))

	#***** AGGIUNGI STUDENTE *****
	def aggiungiStudente(self, studNuovo):
	
		#estrapolo la lista attuale
		listaStudenti = self.getStudN()
		
		#aggiungo il nuovo studente alla lista
		listaStudenti.append(studNuovo)
		
		#imposto la nova lista
		self.setStudN(listaStudenti)

	#***** CERCA STUDENTE *****
	def cercaStudente(self, cognome):
		flag = 0
		#ciclo per il numero di studenti registrati
		for i in range (N):
			
			#controllo se il cognome corrisponde --> se si imposto il flag a "1" (studente trovato)
			if ((self.getStudN()[i].getPersona().getCognome()) == cognome):
				flag = 1
		
		#return del flag
		return flag
		
	#***** ELIMINA STUDENTE *****	
	def eliminaStudente(self, cognome):
		#ciclo per il numero di studenti registrati
		for i in range (N):
			
			#controllo se il cognome corrisponde --> se si imposto il flag a "1" (studente trovato)
			if ((self.getStudN()[i].getPersona().getCognome()) == cognome):
				pos = i
				
		#quando corrisponde --> estrapolo gli studenti
		stud = self.getStudN()
		
		#rimuovo lo studente
		stud.pop(pos)
		
		#imposto la nuova lista di studenti
		self.setStudN(stud)
	
	#***** AGGIUNGI VOTO *****	
	def aggiungiVoto(self, cognome, voto):
		#ciclo per il numero di studenti registrati
		for i in range (N):
			
			#controllo quando il cognome corrisponde
#			corrisponde di sicuro ad uno studente perchè l'utente è entrato nel menù delle azioni solo se il flag restituito dalla
#			funzione "cercaStdente" era pari a "1"
			if ((self.getStudN()[i].getPersona().getCognome()) == cognome):
			
				#quando corrisponde --> estrapolo i voti già registrati
				voti = self.getStudN()[i].getVoti()
				
				#aggiungo il nuovo voto
				voti.append(voto)
				
				#imposto la nuova lista di voti (lista aggiornata con l'ultimo voto aggiunto) allo studente
				self.getStudN()[i].setVoti(voti)

	#***** RIMUOVI VOTO *****	
	def rimuoviVoto(self, cognome, pos):
		#ciclo per il numero di studenti registrati
		for i in range (N):
			
			#controllo quando il cognome corrisponde
			if ((self.getStudN()[i].getPersona().getCognome()) == cognome):
			
				#quando corrisponde --> estrapolo i voti già registrati
				voti = self.getStudN()[i].getVoti()
				
				#controllo la posizione dell'indice rispetto il numero di elementi
				if (pos > len(voti)):
					print("ERRORE! Posizione fuori range, nessun voto verra rimosso...")
				#rimuovo il voto
				else:
					voti.pop(pos)
				
				#imposto la nuova lista di voti (lista aggiornata con l'ultimo voto aggiunto) allo studente
				self.getStudN()[i].setVoti(voti)
				
	#***** MEDIA STUDENTE *****
	def mediaStudente(self, cognome):
		#ciclo per il numero di studenti registrati
		for i in range (N):
			
			#controllo quando il cognome corrisponde
			if ((self.getStudN()[i].getPersona().getCognome()) == cognome):
			
				#quando corrisponde --> estrapolo i voti registrati
				voti = self.getStudN()[i].getVoti()
		
		#calcolo la media dei voti dello studente		
		n = len(voti)
		somma = sum(voti)
		media = somma / n
		print("Media voti dello studente: {:2.2f}".format(media))
	
	#***** DATI STUDENTE *****
	def datiStudente(self, cognome):
		#ciclo per il numero di studenti registrati
		for i in range (N):
			
			#controllo quando il cognome corrisponde
			if ((self.getStudN()[i].getPersona().getCognome()) == cognome):
			
				#quando corrisponde --> stampo i dati registrati
				voti = self.getStudN()[i].getPersona().presentati()
#------------------------------------------------------------------------------------------------------------------------------------
def chiediN():
	#chiedo e controllo il numero di studenti da registrare
	val = input("Inserire il numero di studenti da registrare (" + str(MIN_STUD) + "-" + str(MAX_STUD) + "): ")
	while (not val.isnumeric() or int(val) < MIN_STUD or int(val) > MAX_STUD):
		val = input("ERRORE! Inserire il numero di studenti da registrare (" + str(MIN_STUD) + "-" + str(MAX_STUD) + "): ")
	
	#restituisco il valore (intero)
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------
def insNome():
	#chiedo e controlllo il nome
	val = input("Inserire il nome: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il nome: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------
def insCognome():
	#chiedo e controllo il cognome
	val = input("Inserire il cognome: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il cognome: ")
	
	#restituisco il valore (stringa)
	return val
#------------------------------------------------------------------------------------------------------------------------------------
def insEta():
	#chiedo e controllo l'età
	val = input("Inserire l'età: ")
	while (not val.isnumeric() or int(val) < 0):
		val = input("ERRORE! Inserire l'età: ")
	
	#restituisco il valore (intero)
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------
def insVoti():
	listaVoti = [] #inizializzo i voti come una lista vuota
	
	#ciclo finchè l'utente non vuole terminare l'inserimento dei voti (digita 0)
	while True:
	
		#chiedo e controllo il singolo voto
		val = input("Inserire un voto (digitare 0 per terminare): ")
		while (not val.isnumeric() or int(val) < 0 or int(val) > 10):
			val = input("ERRORE! Inserire un voto (digitare 0 per terminare): ")
		val = int(val)
		
		#controllo se l'utente ha deciso di uscire (digita 0) --> interrompo il ciclo while
		if val == 0:
			break
			
		#altrimenti aggiungo il voto alla lista con i voti precedenti --> continuo con il ciclo while
		else:
			listaVoti.append(val)
	
	#uscito dal ciclo while --> return con la lista contenente i voti
	return listaVoti
#------------------------------------------------------------------------------------------------------------------------------------
os.system("clear")

#chiedo il numero di studenti da registrare
N = chiediN()
listaStudenti = []

#ciclo per il numero di studenti da registrare
for i in range (N):
	#chiedo i dati
	nome = insNome()
	cognome = insCognome()
	eta = insEta()
	voti = insVoti()
	print("")
	
	#creo la persona, dalla persona ceo lo studente e lo aggiungo alla lista
	persN = Persona (cognome, nome, eta)
	studN = Studente (persN, voti)
	listaStudenti.append(studN)

#creazione gruppo classe
print(" ____________________________ ")
print("|                            |")
print("|  CREAZIONE GRUPPO CLASSE   |")
print("|____________________________|")

miaClasse = GruppoClasse (listaStudenti)

#STAMPA DEI DATI
os.system("clear")
miaClasse.stampa()

#PULIZIA DELLO SCHERMO
input("Premi INVIO per continuare...")
os.system("clear")

uscita = 0

#CICLO CON IL MENU' FINCHE' L'UTENTE NON DECIDE DI USCIRE
while uscita == 0:
	print(" ____________________________ ")
	print("|                            |")
	print("|     MENÙ DELLE OPZIONI     |")
	print("|____________________________|")
	print("|                            |")
	print("|1- RICERCA STUDENTE         |")
	print("|2- AGGIUNGI STUDENTE        |")
	print("|3- EXIT                     |")
	print("|____________________________|")	
	opzione = input("\nScegliere una delle opzioni: ")
	
	#CONTROLLO OPZIONE INSERITA
	while not opzione.isnumeric() or opzione.isspace() or int(opzione) < 1 or int(opzione) > 3:
		opzione = input("ERRORE! Scegliere una delle opzioni: ")
	opzione = int(opzione) #casting effettuato dopo il while in modo da evitare errori
	os.system("clear")
	
	#OPZIONE 1 --> CERCO UNO STUDENTE
	if opzione == 1:
		#chiedo il cognome di uno studente e lo cerco
		cognomeIns = insCognome()
		flag = miaClasse.cercaStudente(cognomeIns)
		
		#se non trovato --> messaggio
		if flag == 0:
			print("Studente non trovato!")
		
			#PULIZIA DELLO SCHERMO
			input("Premi INVIO per continuare...")
			os.system("clear")
		
		#se trovato --> menù azioni disponibili
		if flag == 1:
			print(" ____________________________ ")
			print("|                            |")
			print("|     AZIONI DISPONIBILI     |")
			print("|____________________________|")
			print("|                            |")
			print("|1- AGGIUNGI VOTO            |")
			print("|2- RIMUOVI VOTO             |")
			print("|3- MEDIA VOTI               |")
			print("|4- DATI ANAGRAFICI          |")
			print("|5- ELIMINA STUDENTE         |")
			print("|____________________________|")	
			azione = input("\nScegliere una delle azioni da eseguire: ")
	
			#CONTROLLO AZIONE INSERITA
			while not azione.isnumeric() or azione.isspace() or int(azione) < 1 or int(azione) > 5:
				azione = input("ERRORE! Scegliere una delle azioni da eseguire: ")
			azione = int(azione) #casting effettuato dopo il while in modo da evitare errori
			os.system("clear")
				
			#AZIONE 1 --> AGGIUNGI VOTO
			if azione == 1:
				print(" ____________________________ ")
				print("|                            |")
				print("|       AGGIUNGI VOTO        |")
				print("|____________________________|")
				
				#voto da aggiungere
				votoIns = input("Inserire un voto da aggiungere allo studente: ")
				while (not votoIns.isnumeric() or int(votoIns) < 1 or int(votoIns) > 10):
					votoIns = input("ERRORE! Inserire un voto da aggiungere allo studente: ")
				votoIns = int(votoIns)
				
				#aggiungo il voto allo studente e stampo la classe aggiornata
				miaClasse.aggiungiVoto(cognomeIns, votoIns)
				miaClasse.stampa()
				
				#PULIZIA DELLO SCHERMO
				input("Premi INVIO per continuare...")
				os.system("clear")
			
			#AZIONE 2 --> RIMUOVI VOTO
			if azione == 2:
				print(" ____________________________ ")
				print("|                            |")
				print("|        RIMUOVI VOTO        |")
				print("|____________________________|")
				
				#posizione del voto da rimuovere
				posIns = input("Inserire la posizione del voto da rimuovere allo studente: ")
				while (not posIns.isnumeric() or int(posIns) < 1 or int(posIns) > 10):
					posIns = input("ERRORE! Inserire la posizione del voto da rimuovere allo studente: ")
				posIns = int(posIns)
			
				#rimuovo il voto allo studente e stampo la classe aggiornata
				miaClasse.rimuoviVoto(cognomeIns, posIns)
				miaClasse.stampa()
			
				#PULIZIA DELLO SCHERMO
				input("Premi INVIO per continuare...")
				os.system("clear")
			
			#AZIONE 3 --> MEDIA VOTI
			if azione == 3:
				print(" ____________________________ ")
				print("|                            |")
				print("|         MEDIA VOTI         |")
				print("|____________________________|")
				
				miaClasse.mediaStudente(cognomeIns)
			
				#PULIZIA DELLO SCHERMO
				input("Premi INVIO per continuare...")
				os.system("clear")
			
			#AZIONE 4 --> DATI ANAGRAFICI
			if azione == 4:
				print(" ____________________________ ")
				print("|                            |")
				print("|      DATI ANAGRAFICI       |")
				print("|____________________________|")
			
				miaClasse.datiStudente(cognomeIns)
			
				#PULIZIA DELLO SCHERMO
				input("Premi INVIO per continuare...")
				os.system("clear")
				
			#AZIONE 5 ---> ELIMINA STUDENTE	
			if azione == 5:
				print(" ____________________________ ")
				print("|                            |")
				print("|      ELIMINA STUDENTE      |")
				print("|____________________________|")
				
				#richiesta di conferma
				conf = input("Confermi di voler eliminare lo studente dal registro? (S/N): ")
				while (conf != 'S' and conf != 's' and conf != 'n' and conf != 'N'):
					conf = input("ERRORE! Confermi di voler eliminare lo studente dal registro? (S/N): ")
				
				#se conferma --> elimino
				if (conf == 's' or conf == 'S'):
				
					#rimuovo lo studente e stampo la classe aggiornata
					miaClasse.eliminaStudente(cognomeIns)			
					N = N - 1 #rimuovo 1 dal totale degli studenti registrati (ne ho appena eliminato 1)
					miaClasse.stampa()
					
				#se non conferma --> annullo
				if (conf == 'n' or conf == 'N'):
					print("Operazione annullata!")
				
				#PULIZIA DELLO SCHERMO
				input("Premi INVIO per continuare...")
				os.system("clear")
				
	#OPZIONE 2 --> AGGIUNGO STUDENTE
	if opzione == 2:
		print(" ____________________________ ")
		print("|                            |")
		print("|     AGGIUNGI STUDENTE      |")
		print("|____________________________|")
		#chiedo i dati
		nome = insNome()
		cognome = insCognome()
		eta = insEta()
		voti = insVoti()
	
		#creo la persona, dalla persona ceo lo studente
		persN = Persona (cognome, nome, eta)
		studN = Studente (persN, voti)
		
		#modifico l'elenco della classe
		miaClasse.aggiungiStudente(studN)
		
		N = N + 1 #aggiungo 1 dal totale degli studenti registrati (ne ho appena aggiunto 1)
		
		#PULIZIA DELLO SCHERMO
		input("Premi INVIO per continuare...")
		os.system("clear")
	
	#OPZIONE 3 --> ESCO
	if opzione == 3:
		print("ESCO DAL PROGRAMMA!")
		uscita = 1
