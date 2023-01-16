#4C Bracco Mattia - Classe studenti

import os
#------------------------------------------------------------------------------------------------------------------------------------
class Studente(object):
	#costruttore
	def __init__(self, cognome="", nome="", eta=0, voti=[]):
		self.setNome(nome)
		self.setCognome(cognome)
		self.setEta(eta)
		self.setVoti(voti)
	
	#setter
	def setNome(self, val):
		self.__nome = val
		
	def setCognome(self, val):
		self.__cognome = val
	
	def setEta(self, val):
		self.__eta = val
		
	def setVoti(self, lis):
		self.__voti = lis
		
	#getter
	def getNome(self):
		return self.__nome
	
	def getCognome(self):
		return self.__cognome
	
	def getEta(self):
		return self.__eta
		
	def getVoti(self):
		return self.__voti
		
	#str
	def presentati(self):
		print('Cognome: {0} Nome: {1} Età: {2} Voti: {3}'.format(self.getCognome(), self.getNome(), self.getEta(), self.getVoti()))
#------------------------------------------------------------------------------------------------------------------------------------
class GruppoClasse(object):
	#costruttore
	def __init__(self, nome, objStud1, objStud2, objStud3, objStud4):
		self.setNome(nome)
		self.setStud1(objStud1)
		self.setStud2(objStud2)
		self.setStud3(objStud3)
		self.setStud4(objStud4)
	
	#setter
	def setNome(self, val):
		self.__nome = val
		
	def setStud1(self, obj):
		self.__stud1 = obj
		
	def setStud2(self, obj):
		self.__stud2 = obj
		
	def setStud3(self, obj):
		self.__stud3 = obj
		
	def setStud4(self, obj):
		self.__stud4 = obj
		
	#getter
	def getNome(self):
		return self.__nome
	
	def getStud1(self):
		return self.__stud1
		
	def getStud2(self):
		return self.__stud2
	
	def getStud3(self):
		return self.__stud3
		
	def getStud4(self):
		return self.__stud4
	
	#str
	def presentati(self):
		print("NOME CLASSE: " + str(self.getNome()) + "\n" + str(self.getStud1().presentati()) + str(self.getStud2().presentati()) + str(self.getStud3().presentati()) + str(self.getStud4().presentati()))

	#funzionalità
	def aggiungiVoto(self, nome, voto):
		#cerco lo studente
		flag = 0
		if(nome == stud1.getNome()):
			voti = stud1.getVoti()
			voti = voti.append(voto)
			voti = stud1.setVoti(voti)
			stud1.presentati()
			flag = 1
		if(nome == stud2.getNome()):
			voti = stud2.getVoti()
			voti = voti.append(voto)
			voti = stud2.setVoti(voti)
			stud2.presentati()
			flag = 1
		if(nome == stud3.getNome()):
			voti = stud3.getVoti()
			voti = voti.append(voto)
			voti = stud3.setVoti(voti)
			stud3.presentati()
			flag = 1
		if(nome == stud4.getNome()):
			voti = stud4.getVoti()
			voti = voti.append(voto)
			voti = stud4.setVoti(voti)
			stud4.presentati()
			flag = 1
		if flag == 0:
			print("Studente non trovato!")
#------------------------------------------------------------------------------------------------------------------------------------
def insNome():
	#chiedo e controllo il nome
	val = input("Inserire il nome: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il nome: ")
	return val
#------------------------------------------------------------------------------------------------------------------------------------
def insCognome():
	#chiedo e controllo il cognome
	val = input("Inserire il cognome: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il cognome: ")
	return val
#------------------------------------------------------------------------------------------------------------------------------------
def insEta():
	#chiedo e controllo l'età
	val = input("Inserire l'età: ")
	while (not val.isnumeric() or int(val) < 0):
		val = input("ERRORE! Inserire l'età: ")
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------
def insVoto():
	#chiedo e controllo l'età
	val = input("Inserire un voto: ")
	while (not val.isnumeric() or int(val) < 2 or int(val) > 10):
		val = input("ERRORE! Inserire un voto: ")
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------

#studente 1
print("\nSTUDENTE 1")
nome = insNome()
cognome = insCognome()
eta = insEta()
v1 = insVoto()
v2 = insVoto()
v3 = insVoto()
v4 = insVoto()
voti = [v1, v2, v3, v4]
stud1 = Studente (cognome, nome, eta, voti)

#studente 2
print("\nSTUDENTE 2")
nome = insNome()
cognome = insCognome()
eta = insEta()
v1 = insVoto()
v2 = insVoto()
v3 = insVoto()
v4 = insVoto()
voti = [v1, v2, v3, v4]
stud2 = Studente (cognome, nome, eta, voti)

#studente 3
print("\nSTUDENTE 3")
nome = insNome()
cognome = insCognome()
eta = insEta()
v1 = insVoto()
v2 = insVoto()
v3 = insVoto()
v4 = insVoto()
voti = [v1, v2, v3, v4]
stud3 = Studente (cognome, nome, eta, voti)

#studente 4
print("\nSTUDENTE 4")
nome = insNome()
cognome = insCognome()
eta = insEta()
v1 = insVoto()
v2 = insVoto()
v3 = insVoto()
v4 = insVoto()
voti = [v1, v2, v3, v4]
stud4 = Studente (cognome, nome, eta, voti)

#creazione gruppo classe
print("\nCreazione gruppo classe...")
nome = insNome()
miaClasse = GruppoClasse (nome, stud1, stud2, stud3, stud4)

#stampa dei dati
os.system("clear")
print("Studenti registrati:")
stud1.presentati()
stud2.presentati()
stud3.presentati()
stud4.presentati()
print("\nClasse:")
miaClasse.presentati()

#pulizia schermo
input("Premi INVIO per continuare...")
os.system("clear")

uscita = 0
while uscita == 0:
	print(" ____________________________ ")
	print("|     MENÙ DELLE OPZIONI     |")
	print("|____________________________|")
	print("|                            |")
	print("|1- AGGIUNGI VOTO            |")
	print("|2- ELIMINA STUDENTE         |")
	print("|3- EXIT                     |")
	print("|____________________________|")	
	opzione = input("\nScegliere una delle opzioni: ")
	#controllo scelta inserita
	while not opzione.isnumeric() or opzione.isspace() or int(opzione) < 1 or int(opzione) > 3:
		opzione = input("ERRORE! Scegliere una delle opzioni: ")
	opzione = int(opzione) #casting effettuato dopo il while in modo da evitare errori
	#richiamo funzione in base alla scelta
	if opzione == 1:
		nome = insNome()
		voto = insVoto()
		miaClasse.aggiungiVoto(nome, voto)
	if opzione == 2:
		nome = insNome()
		miaClasse.eliminaStudente(nome)
		
	if opzione == 3:
		print("ESCO DAL PROGRAMMA!")
		uscita = 1
