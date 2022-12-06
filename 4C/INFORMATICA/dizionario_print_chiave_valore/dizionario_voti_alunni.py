#4C Braco Mattia - Dizionario voti alunni
from collections import OrderedDict

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
		registro[nome] = voto
#-------------------------------------------------------------------------------------------------------------------------------------
def stampaVoti():
	print(" ____________________________ ")
	print("|                            |")
	print("|      VOTI REGISTRATI       |")
	print("|____________________________|")
	for chiave in registro:
		print("Studente: {:10s} Voto: {:2s}".format(chiave, registro[chiave]))
#-------------------------------------------------------------------------------------------------------------------------------------
def ordinaVoti():
	registroOrdinato = (sorted(registro.items(), key=lambda x: x[1]))
	print("Voti ordinati in modo crescente:",registroOrdinato)
#-------------------------------------------------------------------------------------------------------------------------------------
registro = dict()
caricaVoti()
stampaVoti()
ordinaVoti()
