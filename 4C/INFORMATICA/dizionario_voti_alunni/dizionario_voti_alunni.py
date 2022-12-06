#4C Braco Mattia - Dizionario voti alunni

N_STUDENTI = 5

def caricaVoti():
	for i in range(N_STUDENTI):
		#chiedo il nome e lo controllo
		nome = input("Inserire il nome del " + str(i+1) + "° studente: ")
		while (nome.isalnum() and not nome.isalpha()) or nome.isnumeric() or nome.isspace():
			nome = input("ERRORE!\tInserire il nome del " + str(i+1) + "° studente: ")
		#chiedo il voto e lo controllo
		voto = input("Inserire il voto del " + str(i+1) + "° studente: ")
		while (not voto.isnumeric() or int(voto) < 1 or int(voto) > 10):
			voto = input("ERRORE!\tInserire il voto del " + str(i+1) + "° studente: ")
		#salvo i valori nel dizionario
		registro['Studente '+ str(i+1)] = nome
		registro['Voto studente' + str(i+1)] = voto
		print(registro)
#-------------------------------------------------------------------------------------------------------------------------------------

registro = dict()
caricaVoti()
