#4C Bracco Mattia

def calcolo(base, esponente=2):
	potenza = base ** esponente
	return potenza
#------------------------------------------------------------------------------------------------------------------------------------
print(calcolo(3)) #base 3, esponente default (2)
print(calcolo(3, 3)) #base 3 esponente dichiarato (3)
print(calcolo(3, esponente = 4)) #base 3 esponente dichiarato (4)
print(calcolo()) #genera errore perchè non viene passato nessun valore (di conseguenza nemmeno la base)
