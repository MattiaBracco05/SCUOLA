#4C Braco Mattia - Dizionario premi proloco

import os

N_MIN = 2
N_MAX = 10

def chiediN():
	#chiedo il valore di N
	val = input("Inserire il numero di premi da registrare (" + str(N_MIN) + "-" + str(N_MAX) + "): ")
	#controllo il valore
	while (not val.isnumeric() or int(val) < N_MIN or int(val) > N_MAX):
		val = input("ERRORE! Inserire il numero di premi da registrare (" + str(N_MIN) + "-" + str(N_MAX) + "): ")
	#return con il valore
	return int(val)
#-------------------------------------------------------------------------------------------------------------------------------------
def caricaPremi():
	#ciclo per il numero di premi da registrare
	for i in range(N):
	
		#chiedo e controllo la descrizione
		desc = input("Inserire la descrizione del " + str(i+1) + "° premio: ")
		while (desc.isalnum() and not desc.isalpha()) or desc.isnumeric() or desc.isspace():
			desc = input("ERRORE! Inserire la descrizione del " + str(i+1) + "° premio: ")
			
		#salvo il premio nel dizionario
		premi[i+1] = desc
#-------------------------------------------------------------------------------------------------------------------------------------
def stampaPremi():
	os.system("clear")
	#stampa decorativa
	print(" ____________________________ ")
	print("|                            |")
	print("|      PREMI REGISTRATI      |")
	print("|____________________________|")
	
	#stampa chiavi/valori
	for chiave in premi:
		print("Premio: {:2d} Descrizione: {:10s}".format(chiave, premi[chiave]))
	
	#pulizia schermo
	input("\nPremi INVIO per continuare...")
	os.system("clear")
#-------------------------------------------------------------------------------------------------------------------------------------
def cancellaPremio():
	os.system("clear")
	#chiedo e controllo la chiave da eliminare
	chiaveIns = input("Inserire il numero della chiave del premio da eliminare: ")
	while not chiaveIns.isnumeric():
		chiaveIns = input("ERRORE! Inserire il numero della chiave del premio da eliminare: ")
	chiaveIns = int(chiaveIns)
	
	#se la chiave è presente --> elimino il premio
	if chiaveIns in premi:
		del premi[chiaveIns]
	#altrimenti --> messaggio
	else:
		print("Chiave non presente!")
		
	#pulizia schermo
	input("\nPremi INVIO per continuare...")
	os.system("clear")
#-------------------------------------------------------------------------------------------------------------------------------------
def ricercaPremio():
	os.system("clear")
	#chiedo e controllo la descrizione da cercare
	descIns = input("Inserire la descrizione del premio da cercare: ")
	while (descIns.isalnum() and not descIns.isalpha()) or descIns.isnumeric() or descIns.isspace():
		descIns = input("ERRORE! Inserire la descrizione del premio da cercare: ")
	
	#cerco la descrizone
	flag = 0
	for chiave in premi:
		#se l'ho trovata --> stampo
		if premi[chiave] == descIns:
			print("Premio: {:2d} Descrizione: {:10s}".format(chiave, premi[chiave]))
			flag = 1
			
	#se non l'ho trovata --> messaggio
	if flag == 0:
		print("Descrizione non trovata!")
		
	#pulizia schermo
	input("\nPremi INVIO per continuare...")
	os.system("clear")
#-------------------------------------------------------------------------------------------------------------------------------------
premi = dict()

os.system("clear")
N = chiediN()
caricaPremi()

uscita = 0
while uscita == 0:
	print(" ____________________________ ")
	print("|                            |")
	print("|    OPZIONI DISPONIBILI     |")
	print("|____________________________|")
	print("|                            |")
	print("|  1) STAMPA ELENCO PREMI    |")
	print("|  2) ELIMINA PREMIO         |")
	print("|  3) RICERCA PREMIO         |")
	print("|  4) EXIT                   |")
	print("|____________________________|")
	#chiedo e controllo l'opzione
	scelta = input("Inserire il numero dell'opzione: ")
	while (not scelta.isnumeric() or int(scelta) < 1 or int(scelta) > 4):
		scelta = input("ERRORE! Inserire il numero dell'opzione: ")
	scelta = int(scelta)
	#azione da fare in base all'opzione inserita
	if scelta == 1:
		stampaPremi()
	if scelta == 2:
		cancellaPremio()
	if scelta == 3:
		ricercaPremio()
	if scelta == 4:
		uscita = 1
