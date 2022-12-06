#Bracco Mattia 4C - Temperature città
MAX_CITTA = 5
MIN_CITTA = 1
MAX_TEMP = 35
MIN_TEMP = -10

#chiedo in input N
N = int(input("Quante città vuoi registrare?: (" + str(MIN_CITTA) + "-" + str(MAX_CITTA) + "): "))
#controllo che N sia nel range (5-20)
while not (MIN_CITTA <= N <= MAX_CITTA):
	N = int(input("ERRORE! (Numero fuori range)\nQuante città vuoi registrare?: (" + str(MIN_CITTA) + "-" + str(MAX_CITTA) + "): "))

i = 0
dati = []

#ciclo per le N città
for i in range (N):

	#chiedo in input il nome
	nome = input("Inserire il nome della " + str(i+1) + "° città: ")
	#controllo che il nome non sia un numero o uno spazio
	while (nome.isalnum() and not nome.isalpha()) or nome.isnumeric() or nome.isspace():
		if nome.isnumeric():
			nome = input("ERRORE! (il nome non può essere un numero)\nInserire il nome della " + str(i+1) + "° città: ")
		elif nome.isspace():
			nome = input("ERRORE! (il nome non può essere uno spazio)\nInserire il nome della " + str(i+1) + "° città: ")
			
	#chiedo in input la temperatura minima
	T_min = int(input("Inserire la temperatura minima registrata: "))
	#controllo che sia nel range
	while T_min < MIN_TEMP or T_min > MAX_TEMP:
		T_min = int(input("ERRORE! (il valore deve essere compreso tra " + str(MIN_TEMP) + " e " + str(MAX_TEMP) +")\nInserire la temperatura minima registrata: "))
		
	#chiedo in input la temperatura massima
	T_max = int(input("Inserire la temperatura massima registrata: "))
	#controllo che sia nel range e non sia minore della temperatura minima
	while T_max < MIN_TEMP or T_max > MAX_TEMP or T_max < T_min:
		T_max = int(input("ERRORE! (il valore deve essere compreso tra " + str(MIN_TEMP) + " e " + str(MAX_TEMP) +", e non può essere inferiore alla temperatura minima)\nInserire la temperatura massima registrata: "))
	
	#concateno i dati nella lista
	dati = dati + [nome, T_min, T_max]
	i = i + 1
	
#chiedo l'escursione termica da utilizzare come valore limite per la ricerca delle città con escursione termica elevata
val = int(input("Inserire valore riferimento per l'escursione termica: "))
while (val <= 0):
	val = int(input("ERRORE! (Il numero deve essere positivo)\nInserire valore riferimento per l'escursione termica: "))

#stampo i dati inseriti
i = 0
count = 0
print("RIEPILOGO DATI INSERITI")
while i < (N*3):
	escursione = dati[i+2] - dati[i+1]
	if escursione >= val:
		count = count + 1
	print("Nome città: " + str(dati[i]) +  " TEMP MIN: " + str(dati[i+1]) + " TEMP MAX: " + str(dati[i+2]) + " Escursione termica: " + str(escursione))
	i = i + 3
	
#stampo il contatore dell'escursione termica elevata
print("Ci sono " + str(count) + " città che hanno una escursione termica elevata superiore al valore inserito (" + str(val) + ")")
