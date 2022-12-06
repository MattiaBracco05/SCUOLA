#Bracco Mattia 4C - Realizzare grafico voti studenti
MAX_VOTI = 10
MIN_VOTI = 0
MAX_ALUNNI = 20
MIN_ALUNNI = 5

#chiedo in input N
N = int(input("Quanti alunni hanno svolto la verifica di INFO?: (" + str(MIN_ALUNNI) + " - " + str(MAX_ALUNNI) + "): "))
#controllo che N sia nel range (5-20)
while not (MIN_ALUNNI <= N <= MAX_ALUNNI):
	N = int(input("ERRORE! (Numero fuori range)\nQuanti alunni hanno svolto la verifica di INFO? (" + str(MIN_ALUNNI) + " - " + str(MAX_ALUNNI) + "): "))

i = 0
dati = []

#ciclo per gli N studenti
for i in range (N):

	#chiedo in input il nome
	nome = input("Inserire il nome del " + str(i+1) + "° studente: ")
	#controllo che il nome non sia un numero o uno spazio
	while (nome.isalnum() and not nome.isalpha()) or nome.isnumeric() or nome.isspace():
		if nome.isnumeric():
			nome = input("ERRORE! (il nome non può essere un numero)\nInserire il nome del " + str(i+1) + "° studente: ")
		elif nome.isspace():
			nome = input("ERRORE! (il nome non può essere uno spazio)\nInserire il nome del " + str(i+1) + "° studente: ")
			
	#chiedo in input il voto
	voto = int(input("Inserire il voto del " + str(i+1) + "° studente: "))
	#controllo che il voto sia nel range (0-10)
	while not MIN_VOTI <= voto <= MAX_VOTI:
		voto = int(input("ERRORE! (il voto deve essere compreso tra 0 e 10)\nInserire il voto del " + str(i+1) + "° studente: "))
	
	#concateno i dati nella lista
	dati = dati + [nome, voto]
	i = i + 1


#stampo i voti e gli *
i = 0
while i < (N*2):
	z = "*" * dati[i+1]
	print("Lo studente " + dati[i] +  " ha preso: " + str(dati[i+1]) + " " + z)
	i = i + 2
