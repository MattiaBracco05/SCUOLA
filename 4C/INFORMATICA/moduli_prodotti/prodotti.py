#4C Bracco Mattia - Es. prodotti con moduli

from modulo import calcolaSomma, calcolaMedia

def chiediN(minVal, maxVal):
	#chiedo in input N
	val = input("Quanti prodotti vuoi registrare?: (" + str(minVal) + "-" + str(maxVal) + "): ")
	#controllo N
	while val.isspace() or val.isalpha() or int(val) < minVal or int(val) > maxVal:
		val = input("ERRORE! (Numero fuori range)\nQuanti prodotti vuoi registrare?: (" + str(minVal) + "-" + str(maxVal) + "): ")
	#return con casting in intero
	return int(val)
#------------------------------------------------------------------------------------------------------------------------------------
def caricaDati():
	for i in range(N):
		
		print("--PRODOTTO N." + str(i+1) + "--")

		#chiedo e controllo il nome
		nome = input("Inserire il nome del " + str(i+1) + "° prodotto: ")
		while nome.isnumeric() or nome.isspace():
			nome = input("ERRORE!\nInserire il nome del " + str(i+1) + "° prodotto: ")
			
		#chiedo e controllo la quantita --> poi casting in int
		qta = input("Inserire la quantità venduta del " + str(i+1) + "° prodotto: ")
		while qta.isspace() or qta.isalpha() or int(qta) < 1 or int(qta) > 100:
			qta = input("ERRORE!\nInserire la quantità venduta del " + str(i+1) + "° prodotto: ")
		qta = int(qta)	
			
		#chiedo e controllo il prezzo --> poi casting in int
		prezzo = input("Inserire il prezzo del " + str(i+1) + "° prodotto: ")
		while prezzo.isspace() or prezzo.isalpha() or int(prezzo) < 1:
			prezzo = input("ERRORE!\nInserire il prezzo del " + str(i+1) + "° prodotto: ")
		prezzo = int(prezzo)
		
		#aggiungo i dati alle rispettive liste
		nomi.append(nome)
		quantita.append(qta)
		prezzi.append(prezzo)
#------------------------------------------------------------------------------------------------------------------------------------
def stampaDati():
	print()
	for i in range(N):
		print("Prodotto: {:10s} Quantità venduta: {:3d} Prezzo: {:3d}€".format(nomi[i], quantita[i], prezzi[i]))
#------------------------------------------------------------------------------------------------------------------------------------
nomi = []
quantita = []
prezzi = []
	
N = chiediN(2, 10)
caricaDati()
stampaDati()

totale = calcolaSomma(N, prezzi, quantita)
qtaMedia = calcolaMedia(N, quantita)
przMedio = calcolaMedia(N, prezzi)
print("\nIl ricavato totale delle vendite è di: {:4d} €".format(totale))
print("La quantità media è di: {:3.2f} prodotti".format(qtaMedia))
print("Il prezzo medio dei prodotti è di: {:3.2f} €".format(przMedio))
