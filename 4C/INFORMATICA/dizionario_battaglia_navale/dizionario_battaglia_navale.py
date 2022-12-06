#4C Bracco Mattia - Dizionario battaglia navale

import os
#------------------------------------------------------------------------------------------------------------------------------------
def insXY(testo, testoErrore):
	
	num = input(testo)
	while(not num.isnumeric() or int(num) < 1 or int(num) > 10):	
		num = input(testoErrore)

	#return della coordinata
	return int(num)
#------------------------------------------------------------------------------------------------------------------------------------
def verificaXY(x, y):
	XY = (x,y)
	flag = 0
	#controllo se la coordinata corrisponde ad una nave già colpita
	if XY in colpite:
		input("Nave già colpita! (Premi INVIO per continuare...)")
	
	#controllo se la coordinata corrisponde ad una già giocata (acqua)
	elif campo[x-1][y-1] == '\u001b[1;31m·\u001b[0m':
		input("Coordinata già inserita! (Premi INVIO per continuare...)")
	
	#altrimenti controllo la coordinata con le navi rimanenti
	else:
		for coordinata in navi:
			for c in navi[coordinata]:
				#se coordinata = nave -->
				if XY == c:
					campo[x-1][y-1] = '    \u001b[1;92mX\u001b[0m'
					navi[coordinata].pop(XY)
					colpite[XY] = 0
					flag = 1
					break
			#se coordinata = acqua -->
			if flag == 0:
				campo[x-1][y-1] = '    \u001b[1;31m·\u001b[0m'
#------------------------------------------------------------------------------------------------------------------------------------
def stampa():
	i = 1
	#intestazione numeri colonne
	print(f"{1:10}{2:5}{3:5}{4:5}{5:5}{6:5}{7:5}{8:5}{9:5}{10:5}\n")
	
	#campo
	for rig in campo:
		print(f"{i:5}{rig[0]:5}{rig[1]:5}{rig[2]:5}{rig[3]:5}{rig[4]:5}{rig[5]:5}{rig[6]:5}{rig[7]:5}{rig[8]:5}{rig[9]:5}")
		i = i + 1
#------------------------------------------------------------------------------------------------------------------------------------
navi = {
	(4) : {
		(1,2) : 4, 
		(2,2) : 4,
		(3,2) : 4,
		(4,2) : 4
	},
	(3) : {
		(4,6) : 3,
		(4,7) : 3,
		(4,8) : 3
	},
	(2) : {
		(8,4) : 2,
		(8,5) : 2
	}
}

colpite = {}
campo = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

#ciclo fine non ho colpito tutte le navi
while (len(navi[4]) != 0 or len(navi[3]) != 0 or len(navi[2]) != 0):
	os.system("clear")
	stampa()
	x = insXY("\nInserire coordinata X della nave da colpire: ", "ERRORE! Inserire coordinata X della nave da colpire (1-10): ")
	y = insXY("Inserire coordinata Y della nave da colpire: ", "ERRORE! Inserire coordinata Y della nave da colpire (1-10): ")
	verificaXY(x, y)

#tutte le navi colpite --> esco
os.system("clear")
print("COMPLIMENTI! Hai affondato tutte le navi presenti")
stampa()
