#4C Bracco Mattia - Battaglia Navale

#simbolo "X" --> nave colpita
#simbolo "-" --> acqua

import os

campoNascosto = [[' ']*10 for x in range(10)]
campoGioco = [[' ']*10 for x in range(10)]
numeroColonna = {'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7, 'I':8, 'J':9}
#------------------------------------------------------------------------------------------------------------------------------------
def stampaCampo(campo):
	print("    A B C D E F G H I J")
	numRighe = 1
	for righe in campo:
		if numRighe < 10:
			print("%d  |%s|" % (numRighe, "|".join(righe)))
		#oltre il numero 10 stampo uno spazio in meno in modo che sia allineato con i numeri ad 1 sola cifra
		else:
			print("%d |%s|" % (numRighe, "|".join(righe)))
		numRighe = numRighe + 1
#------------------------------------------------------------------------------------------------------------------------------------
def stampaRiepilogoNavi():
	nave1 = 0
	nave2 = 0
	nave3 = 0
	#controllo danni nave 1
	if campoGioco[5][2] == 'X':
		nave1 = nave1 + 1
	if campoGioco[6][2] == 'X':
		nave1 = nave1 + 1
	#controllo danni nave 2
	if campoGioco[1][1] == 'X':
		nave2 = nave2 + 1
	if campoGioco[1][2] == 'X':
		nave2 = nave2 + 1
	if campoGioco[1][3] == 'X':
		nave2 = nave2 + 1
	#controllo danni nave 3
	if campoGioco[3][7] == 'X':
		nave3 = nave3 + 1
	if campoGioco[4][7] == 'X':
		nave3 = nave3 + 1
	if campoGioco[5][7] == 'X':
		nave3 = nave3 + 1
	if campoGioco[6][7] == 'X':
		nave3 = nave3 + 1
	#print
	print("STATO NAVI:\nNave 1: " + str(nave1) + "/2\nNave 2: " + str(nave2) + "/3\nNave 3: " + str(nave3) + "/4")
#------------------------------------------------------------------------------------------------------------------------------------
def inserisciXY():
		#chiedo la riga da attaccare
		X = int(input("Inserire una riga da attaccare 1-10: "))
		#controllo la riga
		while X < 1 or X > 10:
			X = int(input("RIGA NON VALIDA!\nInserire una riga 1-10: "))
        
    #chiedo la colonna da attaccare
		Y = input("Inserire una colonna da attaccare A-J: ").upper()
		#controllo la colonna
		while Y not in 'ABCDEFGHIJ':
			Y = input("COLONNA NON VALIDA!\nInserire una colonna A-J: ").upper()
		
		#restituisco le coordinate
		return int(X)-1,numeroColonna[Y]
#------------------------------------------------------------------------------------------------------------------------------------
def contaNavi(campo):
	count = 0
	for X in campo:
		for Y in X:
			if Y == 'X':
				count = count + 1
	return count
#------------------------------------------------------------------------------------------------------------------------------------
def chiediNome():
	flagAdmin = 0
	password = "ADMIN"
	#chiedo il nome per l'accesso
	nome = input("Inserisci il tuo nome (digitare " + str(password) + " per vedere la posizione delle navi): ")
	#accesso come admin --> flag = 1 --> mostra posizione navi
	if (nome == password):
		print("Login effettuato come amministratore!\n")
		flagAdmin = 1
	#accesso come giocatore --> flag = 0 --> Benvenuto
	else:
		print("Benevnuto " + str(nome) + "!\n")
	#restituisco il valore
	return flagAdmin
#------------------------------------------------------------------------------------------------------------------------------------
def inserisciNavi():
	#nave1
	campoNascosto[5][2] = 'X'
	campoNascosto[6][2] = 'X'
	#nave2
	campoNascosto[1][1] = 'X'
	campoNascosto[1][2] = 'X'
	campoNascosto[1][3] = 'X'
	#nave3
	campoNascosto[3][7] = 'X'
	campoNascosto[4][7] = 'X'
	campoNascosto[5][7] = 'X'
	campoNascosto[6][7] = 'X'
#------------------------------------------------------------------------------------------------------------------------------------

flagAdmin = chiediNome()
inserisciNavi()
N = contaNavi(campoNascosto)
uscita = 0

#ciclo finche non colpisco tutte le navi
while uscita == 0:
	#stampo il campo
	print("·PRONTO PER ATTACCARE·")
	stampaCampo(campoGioco)
	stampaRiepilogoNavi()
	#mostro le navi se flag admin == 1
	if (flagAdmin == 1):
		print("POSIZIONE DELLE NAVI MOSTRATA:")
		stampaCampo(campoNascosto)
	#chiedo le coordinate
	X,Y = inserisciXY()
	#··coordinata già attaccata
	if campoGioco[X][Y] == '-' or campoGioco[X][Y] == 'X':
		print("Coordinata già attaccata!")
	#··colpito
	elif campoNascosto[X][Y] =='X':
		print("Colpito!!!")
		campoGioco[X][Y] = 'X'
	#··acqua
	else:
		print("Acqua")
		campoGioco[X][Y] = '-'
	#se ho colpito tutte le navi --> vinco e termino
	if contaNavi(campoGioco) == N:
		print("Tutte le navi sono state affondate!")
		uscita = 1
		break;

	input("Premi invio per continuare...")
	os.system('clear')
