#4C Bracco Mattia - Classe palestra

import os

class Disciplina():
	#costruttore
	def __init__(self, nome, costoMensile):
		self.setNome(nome)
		self.setCostoMensile(costoMensile)
		
	#setter
	def setNome(self, val):
		self.__nome = val
		
	def setCostoMensile(self, val):
		self.__costoMensile = val
		
	#getter
	def getNome(self):
		return self.__nome
	
	def getCostoMensile(self):
		return self.__costoMensile
		
	#str
	def dettagli(self):
		print('DISCIPLINA Nome: {0} Costo: {1}'.format(self.getNome(), self.getCostoMensile()))
#------------------------------------------------------------------------------------------------------------------------------------
class Nuoto(Disciplina):
	#costruttore
	def __init__(self, nome, costoMensile, listaIscritti):
		super().__init__(nome, costoMensile)
		self.setListaIscritti(listaIscritti)
		
	#setter
	def setListaIscritti(self, lis):
		self.__listaIscritti = lis
	
	#getter
	def getListaIscritti(self):
		return self.__listaIscritti
		
	#str
	def dettagli(self):
		print('NUOTO Nome: {0} Corso: {1} Iscritti: {2}'.format(self.getNome(), self.getCostoMensile(), self.getListaIscritti()))
#------------------------------------------------------------------------------------------------------------------------------------
class Aerobica(Disciplina):
	#costruttore
	def __init__(self, nome, costoMensile, listaIscritti):
		super().__init__(nome, costoMensile)
		self.setListaIscritti(listaIscritti)
	
	#setter
	def setListaIscritti(self, lis):
		self.__listaIscritti = lis
		
	#getter
	def getListaIscritti(self):
		return self.__listaIscritti
		
	#str
	def dettagli(self):
		print('AEROBICA Nome: {0} Corso: {1} Iscritti: {2}'.format(self.getNome(), self.getCostoMensile(), self.getListaIscritti()))
#------------------------------------------------------------------------------------------------------------------------------------
class BodyBuilding(Disciplina):
	#costruttore
	def __init__(self, nome, costoMensile, listaIscritti):
		super().__init__(nome, costoMensile)
		self.setListaIscritti(listaIscritti)
	
	#setter
	def setListaIscritti(self, lis):
		self.__listaIscritti = lis
		
	#getter
	def getListaIscritti(self):
		return self.__listaIscritti
		
	#str
	def dettagli(self):
		print('BODY BUILDING Nome: {0} Corso: {1} Iscritti: {2}'.format(self.getNome(), self.getCostoMensile(), self.getListaIscritti()))
#------------------------------------------------------------------------------------------------------------------------------------
class Iscritto():
	#costruttore
	def __init__(self, nome, cognome, listaCorsi):
		self.setNome(nome)
		self.setCognome(cognome)
		self.setListaCorsi(listacorsi)
	
	#setter
	def setNome(self, val):
		self.__nome = val
	
	def setCognome(self, val):
		self.__cognome = val
	
	def setListaCorsi(self, lis):
		self.__listaCorsi = lis
	
	#getter
	def getNome(self):
		return self.__nome
		
	def getCognome(self):
		return self.__cognome
		
	def getListaCorsi(self):
		return self.__listaCorsi
		
	#str
	def dettagli(self):
		print('ISCRITTO Nome: {0} Cognome: {1} Corsi: {2}'.format(self.getNome(), self.getCognome(), self.getLisaCorsi()))
#------------------------------------------------------------------------------------------------------------------------------------
class Circolo():
	#costruttore
	def __init__(self, nome, listaIscritti):
		self.setNome(nome)
		self.setListaIscritti(listaIscritti)
		
	#setter
	def setNome(self, val):
		self.__nome = val
		
	def setListaIscritti(self, lis):
		self.__listaIscritti = lis
		
	#getter
	def getNome(self):
		return self.__nome
		
	def getListaNomi(self):
		return self.__listaIscritti
		
	#str
	def dettagli(self):
		print('CIRCOLO Nome: {0} Iscritti: {1}'.format(selg.getNome(), self.getListaIscritti()))
	
#	***** TROVA ISCRITTO *****
	def trovaIscritto(self, nome):
		print("Trova iscritto...")
		
# ***** TROVA DISCIPLINE *****
	def trovaDiscipline(self, iscritto):
		print("Trova discipline...")		
#------------------------------------------------------------------------------------------------------------------------------------
