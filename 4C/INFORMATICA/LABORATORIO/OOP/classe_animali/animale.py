#4C Bracco Mattia

import os

class animale(object):
	#costruttore
	def __init__(self, nome = 0, peso = 0, sesso = 0, verso = 0):
		self.setNome(nome)
		self.setPeso(peso)
		self.setSesso(sesso)
		self.setVerso(verso)
		
	#setter
	def setNome(self, a):
		self.__nome = a
	
	def setPeso(self, b):
		self.__peso = b
		
	def setSesso(self, c):
		self.__sesso = c
		
	def setVerso(self, d):
		self.__verso = d
	
	#getter
	def getNome(self):
		return self.__nome
		
	def getPeso(self):
		return self.__peso	
		
	def getSesso(self):
		return self.__sesso
		
	def getVerso(self):
		return self.__verso
		
	#interrogazione	
	def presentati(self):
		print("Nome:", self.getNome(), "\nPeso:", str(self.getPeso()), "\nSesso:", self.getSesso(), "\nVerso:", self.getVerso())
	
	#somma animali	
	def __add__(self, other):
		sommaPeso = self.getPeso() + other.getPeso()
		sommaNome = self.getNome() + other.getNome()
		return sommaPeso, sommaNome
#----------------------------------------------------------------------------------------------------------------------------------------------
def insNome():
	#chiedo e controllo il nome
	val = input("Inserire il nome: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il nome: ")
	return val
#----------------------------------------------------------------------------------------------------------------------------------------------
def insPeso():
	#chiedo e controllo il peso
	val = input("Inserire il peso: ")
	while (not val.isnumeric() or int(val) < 0):
		val = input("ERRORE! Inserire il peso: ")
	return int(val)
#----------------------------------------------------------------------------------------------------------------------------------------------
def insSesso():
	#chiedo e controllo il sesso
	val = input("Inserire il sesso (M/F): ")
	while (val != 'M' and val != 'F' and val != 'm' and val != 'f'):
		val = input("ERRORE! Inserire il sesso (M/F): ")
	return val
#----------------------------------------------------------------------------------------------------------------------------------------------
def insVerso():
	#chiedo e controllo il verso
	val = input("Inserire il verso: ")
	while (val.isalnum() and not val.isalpha()) or val.isnumeric() or val.isspace():
		val = input("ERRORE! Inserire il verso: ")
	return val
#----------------------------------------------------------------------------------------------------------------------------------------------
#ANIMALE 1
os.system("clear")
mioAnimale1 = animale()
#inserimento
nome = insNome()
peso = insPeso()
sesso = insSesso()
verso = insVerso()
#settaggio
mioAnimale1.setNome(nome)
mioAnimale1.setPeso(peso)
mioAnimale1.setSesso(sesso)
mioAnimale1.setVerso(verso)

#ANIMALE 2
os.system("clear")
mioAnimale2 = animale()
#inserimento
nome = insNome()
peso = insPeso()
sesso = insSesso()
verso = insVerso()
#settaggio
mioAnimale2.setNome(nome)
mioAnimale2.setPeso(peso)
mioAnimale2.setSesso(sesso)
mioAnimale2.setVerso(verso)

#presentazione
mioAnimale1.presentati()
mioAnimale2.presentati()

var = mioAnimale1 + mioAnimale2
print("Risultato: ", var)
