#4C Bracco Mattia - Classe ospedale

import os

class Persona():
	#Costruttore
	def __init__(self, nome, cognome, codiceFiscale, dataDiNascita):
		self.setNome(nome)
		self.setCognome(cognome)
		self.setCodiceFiscale(codiceFiscale)
		self.setDataDiNascita(dataDiNascita)
		
	#Setter
	def setNome(self, val):
		self.__nome = val		
	def setCognome(self, val):
		self.__cognome = val
	def setCodiceFiscale(self, val):
		self.__codiceFiscale = val
	def setDataDiNascita(self, val):
		self.__dataDiNascita = val
		
	#Getter
	def getNome(self):
		return self.__nome
	def getCognome(self):
		return self.__cognome
	def getCodiceFiscale(self):
		return self.__codiceFiscale
	def getDataDiNascita(self):
		return self.__dataDiNascita
		
	#Str
	def dettagli(self):
		print('PERSONA Nome: {0} Cognome: {1} Codice Fiscale: {2} Data di nascita: {3}'.format(self.getNome(), self.getCognome(), self.getCodiceFiscale(), self.getDataDiNascita()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Paziente(Persona):
	#Costruttore
	def __init__(self, nome, cognome, codiceFiscale, dataDiNascita, motivoRicovero, dataRicovero):
		super().__init__(nome, cognome, codiceFiscale, dataDiNascita)
		self.setMotivoRicovero(motivoRicovero)
		self.setDataRicovero(dataRicovero)
	
	#Setter
	def setMotivoRicovero(self, val):
		self.__motivoRicovero = val
	def setDataRicovero(self, val):
		self.__dataRicovero = val
		
	#Getter
	def getMotivoRicovero(self):
		return self.__motivoRicovero
	def getDataRicovero(self):
		return self.__dataRicovero
		
	#Str
	def dettagli(self):
		print('PAZIENTE Nome: {0} Cognome: {1} Codice Fiscale: {2} Data di nascita: {3} Motivo ricovero: {4} Data ricovero: {5}'.format(self.getNome(), self.getCognome(), self.getCodiceFiscale(), self.getDataDiNascita(), self.getMotivoRicovero(), self.getDataRicovero()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Personale(Persona):
	#Costruttore
	def __init__(self, nome, cognome, codiceFiscale, dataDiNascita, matricola, livelloQualifica, reparto):
		super().__init__(nome, cognome, codiceFiscale, dataDiNascita)
		self.setMatricola(matricola)
		self.setLivelloQualifica(livelloQualifica)
		self.setReparto(reparto)
		
	#Setter
	def setMatricola(self, val):
		self.__matricola = val
	def setLivelloQualifica(self, val):
		self.__livelloQualifica = val
	def setReparto(self, val):
		self.__reparto = val
		
	#Getter
	def getMatricola(self):
		return self.__matricola
	def getLivelloQualifica(self):
		return self.__livelloQualifica
	def getReparto(self):
		return self.__reparto
		
	#Str
	def dettagli(self):
		print('PERSONALE Nome: {0} Cognome: {1} Codice Fiscale: {2} Data di nascita: {3} Matricola: {4} Livello qualifica: {5} Reparto: {6}'.format(self.getNome(), self.getCognome(), self.getCodiceFiscale(), self.getDataDiNascita(), self.getMatricola(), self.getLivelloQualifica(), self.getReparto()))
#-------------------------------------------------------------------------------------------------------------------------------------
class Ospedale():
	#Costruttore
	def __init__(self, nome, listaReparti=[]):
		self.setNome(nome)
		self.setListaReparti(listaReparti)
		
	#Setter
	def setNome(self, val):
		self.__nome = val
	def setListaReparti(self, lis):
		self.__listaReparti = lis
		
	#Getter
	def getNome(self):
		return self.__nome
	def getListaReparti(self):
		return self.__listaReparti
		
	#Str
	def dettagli(self):
		print('Ospedale: {0}'.format(self.getNome()))
		
#	AGGIUNGI REPARTO
	def aggiungiReparto(self, rep):
		lis = self.getListaReparti()
		lis.append(rep)
		self.setListaReparti(lis)
		
# CALCOLA RAPPORTO
	def calcolaRapporto(self):
		lis = self.getListaReparti()
		#ciclo per il numero di reparti
		for rep in lis:
			personale = len(rep.getListaPersonale())
			pazienti = len(rep.getListaPazienti())
			rapporto = personale / pazienti
			print('Reparto Nome: {0} rapporto personale/pazienti: {1}'.format(rep.getNome(), rapporto))
			
#	DIMETTI PAZIENTE	
	def dimetti(self, codiceFiscale):
		#ricavo la lista dei reparti
		listaReparti = self.getListaReparti()
		#ciclo per i reparti
		for reparto in listaReparti:
			#ricavo la lista dei pazienti di quel reparto
			listaPazienti = reparto.getListaPazienti()
			#ciclo per i pazienti nel reparto
			for i in range(len(listaPazienti)):
				if codiceFiscale == listaPazienti[i].getCodiceFiscale():
					pos = i
		listaPazienti.remove(pos)
#-------------------------------------------------------------------------------------------------------------------------------------
class Reparto():
	#Costruttore
	def __init__(self, nome, numeroLetti, listaPersonale=[], listaPazienti=[]):
		self.setNome(nome)
		self.setNumeroLetti(numeroLetti)
		self.setListaPersonale(listaPersonale)
		self.setListaPazienti(listaPazienti)
	
	#Setter
	def setNome(self, val):
		self.__nome = val
	def setNumeroLetti(self, val):
		self.__numeroLetti = val
	def setListaPersonale(self, lis):
		self.__listaPersonale = lis
	def setListaPazienti(self, lis):
		self.__listaPazienti = lis
		
	#Getter
	def getNome(self):
		return self.__nome
	def getNumeroLetti(self):
		return self.__numeroLetti
	def getListaPersonale(self):
		return self.__listaPersonale
	def getListaPazienti(self):
		return self.__listaPazienti
		
	#Str
	def dettagli(self):
		print('REAPRTO Nome: {0} Numero posti letto: {1}'.format(self.getNome(), self.getNumeroLetti()))
		
#	AGGIUNGI PERSONALE
	def aggiungiPersonale(self, pers):
		lis = self.getListaPersonale()
		lis.append(pers)
		self.setListaPersonale(lis)
		
# AGGIUNGI PAZIENTE
	def aggiungiPaziente(self, pers):
		lis = self.getListaPazienti()
		lis.append(pers)
		self.setListaPazienti(lis)
		
#	STAMPA
	def stampa(self):
		print("\nPERSONALE")
		lis = self.getListaPersonale()
		for pers in lis:
			print(pers.dettagli())
			
		print("\nPAZIENTI")
		lis = self.getListaPazienti()
		for pers in lis:
			print(pers.dettagli())	
#-------------------------------------------------------------------------------------------------------------------------------------
os.system("clear")

#CREO L'OSPEDALE
print("Creo l'ospedale")
mioOspedale = Ospedale("Regina Margherita")
mioOspedale.dettagli()

input("\nPremere INVIO per continuare...")
os.system("clear")

#REGISTRO IL PERSONALE
print("Registro il personale")
pers1 = Personale("Mario", "Rossi", "CFMR", "01-01-1990", "MR90", "Q1", "Medicina")
pers1.dettagli()
pers2 = Personale("Giorgio", "Bianchi", "CFGB", "02-02-1991", "GB91", "Q2", "Chirurgia")
pers2.dettagli()
pers3 = Personale("Luca", "Verde", "CFLV", "03-03-1992", "LV92", "Q1", "Ortopedia")
pers3.dettagli()

input("\nPremere INVIO per continuare...")
os.system("clear")

#REGISTRO I PAZIENTI
print("Registro i pazienti")
paz1 = Paziente("Matteo", "Arancione", "CFMA", "04-04-1994", "malattia", "03-03-2020")
paz1.dettagli()
paz2 = Paziente("Franceso", "Viola", "CFFV", "05-05-1995", "incidente", "03-03-2021")
paz2.dettagli()
paz3 = Paziente("Leonardo", "Marrone", "CFLM", "06-06-1996", "frattura", "03-03-2022")
paz3.dettagli()

input("\nPremere INVIO per continuare...")
os.system("clear")

#REGISTRO I REPARTI
print("Reigistro i reparti")
medicina = Reparto("Medicina", 10)
medicina.dettagli()
chirurgia = Reparto("Chirurgia", 10)
chirurgia.dettagli()
ortopedia = Reparto("Ortopedia", 10)
ortopedia.dettagli()

input("\nPremere INVIO per continuare...")
os.system("clear")

#AGGIUNGO LE PERSONE AI REPARTI
print("Aggiungo le persone ai reparti")
medicina.aggiungiPersonale(pers1)
medicina.aggiungiPaziente(paz1)
chirurgia.aggiungiPersonale(pers2)
chirurgia.aggiungiPaziente(paz2)
ortopedia.aggiungiPersonale(pers3)
ortopedia.aggiungiPaziente(paz2)

input("\nPremere INVIO per continuare...")
os.system("clear")

#STAMPO I REPARTI
print("Stampo i reparti")
print("\n*****MEDICINA*****")
medicina.stampa()
print("\n******CHIRURGIA*****")
chirurgia.stampa()
print("\n*****ORTOPEDIA*****")
ortopedia.stampa()

input("\nPremere INVIO per continuare...")
os.system("clear")

#AGGIUNGO I REPARTI ALL'OSPEDALE
print("Aggiungo i reparti all'ospedale")
mioOspedale.aggiungiReparto(medicina)
mioOspedale.aggiungiReparto(chirurgia)
mioOspedale.aggiungiReparto(ortopedia)

input("\nPremere INVIO per continuare...")
os.system("clear")

#CALCOLO I RAPPORTI DEI REPARTI
print("Calcolo i rapporti dei reparti")
mioOspedale.calcolaRapporto()

input("\nPremere INVIO per continuare...")
os.system("clear")

#DIMETTO UN PAZIENTE
print("Dimetto un paziente")
mioOspedale.dimetti("CFMA")

input("\nPremere INVIO per continuare...")
os.system("clear")
