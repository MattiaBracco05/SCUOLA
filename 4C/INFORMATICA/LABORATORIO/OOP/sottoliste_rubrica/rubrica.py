#4C Bracco Mattia - Rubrica contatti

import os
#------------------------------------------------------------------------------------------------------------------------------------
def aggiungiContatto(lista):
	print(" ____________________________ ")
	print("|                            |")
	print("|   MENÙ AGGIUNGI CONTATTO   |")
	print("|____________________________|")
	#inserimento e controllo nome
	nome = input("\nInserire il nome: ")
	while (nome.isalnum() and not nome.isalpha()) or nome.isnumeric() or nome.isspace():
			nome = input("ERRORE! Inserire il nome: ")
	#inserimento e controllo cognome
	cognome = input("Inserire il cognome: ")
	while (cognome.isalnum() and not cognome.isalpha()) or cognome.isnumeric() or cognome.isspace():
		cognome = input("ERRORE! Inserire il cognome: ")
	#inserimento e controllo numero di telefono
	telefono = input("Inserire il numero di telefono: ")
	while not telefono.isnumeric() or telefono.isspace() or telefono.isalpha():
			telefono = input("ERRORE! Inserire il numero di telefono: ")
	#inserimento e controllo mail
	mail = input("Inserire indirizzo mail: ")
	while mail.isspace():
		mail = input("ERRORE! Inserire indirizzo mail: ")
	#aggiungo i dati alla lista
	lista.append([nome, cognome, telefono, mail])
	#pulizia schermo
	input("\nPremi invio per continuare...")
	os.system("clear")
#------------------------------------------------------------------------------------------------------------------------------------
def cercaNumero(lista):
	print(" ____________________________ ")
	print("|                            |")
	print("|     MENÙ CERCA CONTATTO    |")
	print("|____________________________|")
	#inserimento e controllo numero di telefono
	telefonoIns = input("\nInserire il numero di telefono da cercare in rubrica: ")
	while not telefonoIns.isnumeric() or telefonoIns.isspace() or telefonoIns.isalpha():
			telefonoIns = input("ERRORE! Inserire il numero di telefono da cercare in rubrica: ")
	#cerco il numero
	flag = 0
	for i in range(len(lista)):
		if lista[i][2] == telefonoIns:
			print("Nome: {:10s}".format(lista[i][0]) + " Cognome {:10s}".format(lista[i][1]))
			flag = flag + 1
	if flag == 0:
		print("Ci dispiace, il numero da lei inserito non è presente in rubrica")
	#pulizia schermo
	input("\nPremi invio per continuare...")
	os.system("clear")
	
#------------------------------------------------------------------------------------------------------------------------------------
def eliminaContatto(lista):
	print(" ____________________________ ")
	print("|                            |")
	print("|   MENÙ ELIMINA CONTATTO    |")
	print("|____________________________|")
	#inserimento e controllo cognome
	cognomeIns = input("\nInserire il cognome del contatto da eliminare: ")
	while (cognomeIns.isalnum() and not cognomeIns.isalpha()) or cognomeIns.isnumeric() or cognomeIns.isspace():
		cognomeIns = input("ERRORE! Inserire il cognome: ")
	#cerco il cognome
	flag = 0
	for i in range(len(lista)):
		if lista[i][1] == cognomeIns:
			del lista[i]
			flag = flag + 1
			print("Conatto eliminato con successo")
			stampaRubrica(lista)
	if flag == 0:
		print("Cognome non presente in rubrica!")
		#pulizia schermo
		input("\nPremi invio per continuare...")
		os.system("clear")
#------------------------------------------------------------------------------------------------------------------------------------
def stampaRubrica(lista):
	print(" ____________________________ ")
	print("|                            |")
	print("|    MENÙ STAMPA CONTATTI    |")
	print("|____________________________|")
	#stampo
	print("\nCONTATTI SALVATI IN RUBRICA:")
	for i in range(len(lista)):
		print("{:2d}-".format(i+1) + " Nome: {:10s}".format(lista[i][0]) + " Cognome: {:10s}".format(lista[i][1]) + " Numero: {:10s}".format(lista[i][2]) + " Mail: {:10s}".format(lista[i][3]))
	#pulizia schermo
	input("\nPremi invio per continuare...")
	os.system("clear")
#------------------------------------------------------------------------------------------------------------------------------------
rubrica = []
exit = 0
while exit == 0:
	#inserimento scelta
	print(" ____________________________ ")
	print("|     MENÙ DELLE OPZIONI     |")
	print("|____________________________|")
	print("|                            |")
	print("|1- AGGIUNGI CONTATTO        |")
	print("|2- CERCA CONTATTO           |")
	print("|3- ELIMINA CONTATTO         |")
	print("|4- STAMPA CONTATTI          |")
	print("|5- EXIT                     |")
	print("|____________________________|")	
	opzione = input("\nScegliere una delle opzioni: ")
	#controllo scelta inserita
	while not opzione.isnumeric() or opzione.isspace() or int(opzione) < 1 or int(opzione) > 5:
		opzione = input("ERRORE! Scegliere una delle opzioni: ")
	opzione = int(opzione) #casting effettuato dopo il while in modo da evitare errori
	#richiamo funzione in base alla scelta
	if opzione == 1:
		aggiungiContatto(rubrica)
	if opzione == 2:
		cercaNumero(rubrica)
	if opzione == 3:
		eliminaContatto(rubrica)
	if opzione == 4:
		stampaRubrica(rubrica)
	if opzione == 5:
		print("Esco dal programma!")
		exit = 1
