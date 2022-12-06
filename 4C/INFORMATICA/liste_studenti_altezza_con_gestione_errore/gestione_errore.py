#Bracco Mattia 4C - Registrare altezze studenti
MAX_ALTEZZA = 200
MIN_ALTEZZA = 140
MAX_ALUNNI = 20
MIN_ALUNNI = 2

#chiedo in input N
N = int(input("Quanti alunni vuoi registrare?: (" + str(MIN_ALUNNI) + "-" + str(MAX_ALUNNI) + "): "))
#controllo che N sia nel range (5-20)
while not (MIN_ALUNNI <= N <= MAX_ALUNNI):
	N = int(input("ERRORE! (Numero fuori range)\nQuanti alunni vuoi registrare?: (" + str(MIN_ALUNNI) + "-" + str(MAX_ALUNNI) + "): "))
	
dati = []
a_max = 0

#ciclo per gli N studenti
for i in range (N):

	#chiedo in input il nome
	nome = input("Inserire il nome del " + str(i+1) + "° studente: ")
	#controllo che il nome non sia un numero o uno spazio o contenga dei numeri al suo interno
	while (nome.isalnum() and not nome.isalpha()) or nome.isnumeric() or nome.isspace():
		if nome.isnumeric():
			nome = input("ERRORE! (il nome non può essere un numero)\nInserire il nome del " + str(i+1) + "° studente: ")
		elif nome.isspace():
			nome = input("ERRORE! (il nome non può essere uno spazio)\nInserire il nome del " + str(i+1) + "° studente: ")
		elif nome.isalnum():
			nome = input("ERRORE! (il nome non può contenere dei numeri)\nInserire il nome del " + str(i+1) + "° studente: ")
			
	#chiedo in input l'altezza
	
	#-----CONTROLLO DELL'ERRORE CON "try:" E "except:"-----
	flag = False
	while flag == False:
		altezza_str = input("Inserire l'altezza in cm: ")
		try:
			altezza = int(altezza_str)
			flag = True
		except:
			print("Non hai inserito un numero!")
	print("Inserimento riuscito!")

	#controllo se è il più alto
	if altezza > a_max:
		a_max = altezza
		n_max = nome
	
	#concateno i dati nella lista
	dati = dati + [nome, altezza]
	i = i + 1

#stampo i dati inseriti
print("\n------DATI INSERITI------")
i = 0
while i < (N*2):
	print("Lo studente {:10s} è alto: {:3d}".format(dati[i], dati[i+1]))
	i = i + 2

lista_alti = []
lista_bassi = []

#creo le 2 liste
i = 0
while i < (N*2):
	if (dati[i+1] > 150):
		lista_alti.append(dati[i])
	else:
		lista_bassi.append(dati[i])
	i = i + 2
	
#stampo le 2 liste
print("\n-------LISTA ALTI--------")
print(lista_alti)
print("\n-------LISTA BASSI-------")
print(lista_bassi)

#conto gli elementi nele liste
print("\nNumero di persone nella lista delle persone alte: " + str(len(lista_alti)))
print("Numero di persone nella lista delle persone basse: " + str(len(lista_bassi)))

#stampo il nome della persona più alta
print("\nLo studente più alto è " + str(n_max) + " ed è alto: " + str(a_max) + " cm")
