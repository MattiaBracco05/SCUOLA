#4C Bracco Mattia - Classe squadra

import os
#-------------------------------------------------------------------------------------------------------------------------------------
class Squadra:
	#Costruttore
	def __init__(self, nome, vinte=0, pareggiate=0, perse=0):
		self.setNome(nome)
		self.setVinte(vinte)
		self.setPareggiate(pareggiate)
		self.setPerse(perse)

	#Setter
	def setNome(self, val):
		self.__nome = val

	def setVinte(self, val):
		self.__vinte = val

	def setPareggiate(self, val):
		self.__pareggiate = val

	def setPerse(self, val):
		self.__perse = val

	#Getter
	def getNome(self):
		return self.__nome
	
	def getVinte(self):
		return self.__vinte
		
	def getPareggiate(self):
		return self.__pareggiate
	
	def getPerse(self):
		return self.__perse
		
	#STR
	def dettagli(self):
		print("Squadra: {:10s} Punti: {:2d} ~ Vinte: {:2d} Pareggiate: {:2d} Perse {:2d}".format(self.getNome(), self.calcolaPunti(), self.getVinte(), self.getPareggiate(), self.getPerse()))
	
	def __int__(self):
		return self.calcolaPunti()
#	CALCOLA PUNTI	SQUADRA
	def calcolaPunti(self):
		totale = 0
		vinte = self.getVinte()
		pareggiate = self.getPareggiate()
		totale = (vinte * 3) + pareggiate
		return totale

#	INIZIO ANNO (AZZERA PUNTI SQUADRA)
	def inizioAnno(self):
		self.setVinte(0)
		self.setPareggiate(0)
		self.setPerse(0)

#	VINCE
	def vince(self):
		partiteVinte = self.getVinte()
		partiteVinte += 1
		self.setVinte(partiteVinte)

#	PAREGGIA
	def pareggia(self):
		partitePareggiate = self.getPareggiate()
		partitePareggiate += 1
		self.setPareggiate(partitePareggiate)
		
#	PERDE
	def perde(self):
		partitePerse = self.getPerse()
		partitePerse += 1
		self.setPerse(partitePerse)
		
#	CONFRONTA
	def confronta(self, squad2):
		puntiS1 = self.calcolaPunti()
		puntiS2 = squad2.calcolaPunti()
		differenza = puntiS1 - puntiS2
		if differenza > 0:
			print("{:10s} ha {:2d} punti in più di {:10s}".format(self.getNome(), differenza, squad2.getNome()))
		else:
			print("{:10s} ha {:2d} punti in meno di {:10s}".format(self.getNome(), differenza, squad2.getNome()))
#-------------------------------------------------------------------------------------------------------------------------------------
os.system("clear")

print("Registro automaticamente le squadre...")
S1 = Squadra("Torino")
S2 = Squadra("Roma")
S1.dettagli()
S2.dettagli()

print("\nAssegno una vittoria al Torino e un pareggio alla Roma")
S1.vince()
S2.pareggia()
S1.dettagli()
S2.dettagli()

print("\nRicavo i punti delle 2 squadre")
punti = S1.calcolaPunti()
print("Punti Torino:", punti)
punti = S2.calcolaPunti()
print("Punti Roma:", punti)

print("\nConfronto le 2 squadre")
S1.confronta(S2)

print("\nAssegno una sconfitta alle 2 squadre")
S1.perde()
S2.perde()
S1.dettagli()
S2.dettagli()

print("\nRicavo i punti con il metodo __int__")
print("Punti Torino:", int(S1))
print("Punti Roma:", int(S2))

print("\nAzzero la stagione")
S1.inizioAnno()
S2.inizioAnno()
S1.dettagli()
S2.dettagli()
