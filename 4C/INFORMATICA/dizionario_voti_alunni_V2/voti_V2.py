import os
import datetime

N_STUDENTI = 2

#-----------------------------------------------------------------------------------------------------------------------------------
def cfloat(str_num: str, m: str) -> float:
	while True:
		try:
			return float(str_num)
		except ValueError:
			str_num = input(m)

#-----------------------------------------------------------------------------------------------------------------------------------
def insData() -> str:
	#chiedo la data e controllo la lunghezza della stringa
	data = input("Inserire la data di assegnazione (GG-MM-AAAA): ").split("-")
	while len(data) != 3:
		data = input("Inserre la data di assegnazione (GG-MM-YYYY): ").split("-")
	
	#ciclo while in cui:
	while True:
		#prova a formattare la stringa come data --> return data
		try:
			gg, mm, y = data
			datetime.date(int(y), int(mm), int(gg))
			return f"{gg}-{mm}-{y}"
			
		#in caso di errore --> richiedi e controlla la lunghezza della stringa
		except:
			data = input("Inserire la data di assegnazione (GG-MM-AAAA): ").split("-")
			while len(data) != 3:
				data = input("Inserire la data di assegnazione (GG-MM-AAAA): ").split("-")
#-----------------------------------------------------------------------------------------------------------------------------------
def insStudenti(students: dict):
	#ciclo per il numero di studenti
	for i in range(N_STUDENTI):
	
		#chiedo il nome e metto l'iniziale maiuscola
		nome = input(f"Inserire il nome dello studente: ")
		nome = nome.capitalize()
	
		#se non è presente nel dizionario (registro) --> lo aggiungo
		if nome not in students:
			students[nome] = dict()
		
		#inserisco voti e date finche l'utente non digita fine
		while True:
			
			#chiedo il voto
			voto = input(f"Inserire il voto di {nome} (inserire 'fine' per terminare): ")
			
			#controllo se ha digitato fine --> se si esco
			if voto.lower() == "fine":
				break
			
			#se non ha digitato fine --> chiedo di inserire un voto
			voto = cfloat(voto, "Inserire un numero: ")
			#controllo il voto inserito
			while not 0 <= voto <= 10:
				voto = cfloat(input(f"Inserire un voto tra 0 e 10: "), "Inserire un numero")
			if voto not in students[nome]:
				students[nome][voto] = []
			
			#aggiungo il voto e la data
			students[nome][voto].append(insData())
#-----------------------------------------------------------------------------------------------------------------------------------			
def mPn(students: dict) -> dict:
	res = dict()
	for nome, votos in students.items():
		for voto in votos:
			if voto not in res:
				res[voto] = []
			res[voto].append(nome)
	return res
#-----------------------------------------------------------------------------------------------------------------------------------			
def ordina(d: dict) -> list:
	return sorted(list(d.items()), key=lambda x: x[0])
#-----------------------------------------------------------------------------------------------------------------------------------			
students = {}
insStudenti(students)
os.system("clear")

#chiedo di inserire il nome di uno studente
nome = input("Inserire il nome di un studente: ")
nome = nome.capitalize()

#se è nel dizionario mi salvo i suoi voti e li ordino
if nome in students:
	voti = students[nome]
	ordinato = ordina(voti)
	#stampo i voti ordinati
	for voto, data in ordinato:
		print(f"{voto:<5}: {','.join(data).strip(',')}")
		
#se non è nel dizionario --> messaggio
else:
	print("Studente non trovato")

#pulizia schermo
input("Premi INVIO per continuare...")
os.system("clear")

#chiedo di inserire una data
dataInserita = insData()
diz = dict()

#cerco i voti registrati in quella data
for nome, voti in students.items():
	for voto, date in voti.items():
		for data in date:
			if data == dataInserita:
				if voto not in diz:
					diz[voto] = []
				diz[voto].append(nome)
				
#se sono stati assegnati voti --> stampo
if len(diz) != 0:
	for voto, nome in diz.items():
		print(f"{voto:<5}: {','.join(nome).strip(',')}")
#se non sono stati assegnati voti --> messaggio
else:
	print("Non sono stati assegnati voti in questo giorno.")
