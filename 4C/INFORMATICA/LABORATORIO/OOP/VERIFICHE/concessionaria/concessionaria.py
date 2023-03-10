#Bracco Mattia 4C - Concessionaria auto

MAX_VEICOLI = 8
MIN_VEICOLI = 4
MAX_PREZZO = 40000
MIN_PREZZO = 12000
MAX_PREZZO_PROPOSTO = 50000
MIN_PREZZO_PROPOSTO = 10000

#chiedo in input N (numero di veicoli regitsrati in concessionaria)
N = int(input("Quanti veicoli vuoi registrare?: (" + str(MIN_VEICOLI) + "-" + str(MAX_VEICOLI) + "): "))
#controllo che N sia nel range
while not (MIN_VEICOLI <= N <= MAX_VEICOLI):
	N = int(input("ERRORE! (Numero fuori range)\nQuanti veicoli vuoi registrare? (" + str(MIN_VEICOLI) + "-" + str(MAX_VEICOLI) + "): "))

i = 0
dati = []

#ciclo per gli N veicoli
for i in range (N):

	#chiedo in input la targa
	targa = input("Inserire la targa del " + str(i+1) + "° veicolo: ")
	#controllo il formato della targa (aa/001/aa)
	while (len(targa) != 7 or targa[0].isnumeric() or targa[1].isnumeric() or targa[2].isalpha() or targa[3].isalpha() or targa[4].isalpha() or targa[5].isnumeric() or targa[6].isnumeric()):
			targa = input("ERRRORE! (formato targa non valido, es. formato valido AA001AA)\nInserire la targa del " + str(i+1) + "° veicolo: ")
	
	#chiedo in input il colore
	colore = input("Inserire il colore del " + str(i+1) + "° veicolo: ")
	#controllo che il colore non sia un numero
	while colore.isnumeric():
		colore = input("ERRORE! (il colore non può essere un numero)\nInserire il colore del " + str(i+1) + "° veicolo: ")
	
	#chiedo in input il prezzo
	prezzo = int(input("Inserire il prezzo del " + str(i+1) + "° veicolo: "))
	#controllo che il prezzo sia nel range
	while not MIN_PREZZO <= prezzo <= MAX_PREZZO:
		prezzo = int(input("ERRORE! (il prezzo deve essere compreso tra " + str(MIN_PREZZO) + "€ e " + str(MAX_PREZZO) + "€)\nInserire il prezzo del " + str(i+1) + "° veicolo: "))

	#concateno i dati nella lista
	dati = dati + [targa, colore, prezzo]
	
#stampo i dati inseriti
i = 0
print(" ____________________________ ")
print("|                            |")
print("|       DATI INSERITI        |")
print("|____________________________|")
while i < (N*3):
	print("Veicolo targa: {:7s} colore: {:10s} prezzo: {:5d} €".format(dati[i], dati[i+1], dati[i+2]))
	i = i + 3
	
print(" ____________________________ ")
print("|                            |")
print("|      RICERCA COLORE        |")
print("|____________________________|")
#chiedo e controllo il colore per la ricerca dei veicoli
colore_ricerca = input("Inserire un colore per la ricerca dei veicoli: ")
while colore_ricerca.isnumeric():
	colore_ricerca = input("ERRORE! (il colore non può essere un numero)\nInserire un colore per la ricerca dei veicoli: ")

#cerco i veicoli con quel determinato colore
flag = 0
i = 0
while i < (N*3):
	if (dati[i+1] == colore_ricerca):
		print("Veicolo targa: {:7s} colore: {:10s} prezzo: {:5d} €".format(dati[i], dati[i+1], dati[i+2]))
		flag = flag + 1
	i = i + 3
#flag = 0 in caso di colore non trovato --> messaggio
if (flag == 0):
	print("Non sono presenti veicoli con il colore " + str(colore_ricerca) + " nella nostra concessionaria")

margini = []
margine_min = 50000
margine_max = 0
print(" ____________________________ ")
print("|                            |")
print("|       RICERCA TARGA        |")
print("|____________________________|")
#effettuo per 4 volte la ricerca con la targa
for j in range(4):

	#chiedo la targa  e controllo il fomrato della targa
	targa_ricerca = input("\nInserire una targa per la ricerca del veicolo: ")
	while (len(targa_ricerca) != 7 or targa_ricerca[0].isnumeric() or targa_ricerca[1].isnumeric() or targa_ricerca[2].isalpha() or targa_ricerca[3].isalpha() or targa_ricerca[4].isalpha() or targa_ricerca[5].isnumeric() or targa_ricerca[6].isnumeric()):
		targa_ricerca = input("ERRRORE! (formato targa non valido, es. formato valido AA001AA)\nInserire la targa del " + str(i+1) + "° veicolo: ")
		
	#chiedo e controllo il pezzo proposto
	prezzo_proposto = int(input("Inserire il prezzo proposto per l'aquisto: "))
	while not MIN_PREZZO_PROPOSTO <= prezzo_proposto <= MAX_PREZZO_PROPOSTO:
		prezzo_proposto = int(input("ERRORE! (il prezzo proposto deve essere compreso tra " + str(MIN_PREZZO_PROPOSTO) + "€ e " + str(MAX_PREZZO_PROPOSTO) + "€)\nInserire il prezzo proposto per l'aquisto del veicolo: "))

	#cerco il veicolo con quella determinata targa
	flag = 0
	i = 0
	while i < (N*3):
		if (dati[i] == targa_ricerca):
			print("Veicolo trovato!")
			flag = flag + 1
			#controllo se il prezzo proposto è > del prezzo di acquisto --> margine
			if (prezzo_proposto >= dati[i+2]):
				margine = prezzo_proposto - dati[i+2]
				margini.append(margine)
				#controllo se il margine è il nuovo MAX o il nuovo MIN
				if (margine < margine_min):
					margine_min = margine
				if (margine > margine_max):
					margine_max = margine
			#altrimenti è < del prezzo di acquisto --> messaggio
			else:
				print("La cifra proposta per l'acquisto non è sufficente")
				margini.append(-1)
		i = i + 3
	#flag = 0 in caso di targa non trovata --> messaggio
	if (flag == 0):
		print("Non è presente nessun veicolo con la targa " + str(targa_ricerca) + " nella nostra concessionaria")
		margini.append(-1)
		
#stampo la lista con i valori dei "margini"
#in caso di prezzo proposto < prezzo di aquisto o di targa non presente imposto il margine a -1
print(" ____________________________ ")
print("|                            |")
print("|     MARGINI ACQUISTO       |")
print("|____________________________|")
print("\nMargini di acquisto: " + str(margini))
print("Margine max: " + str(margine_max) + " € Margine min: " + str(margine_min) + " €")
