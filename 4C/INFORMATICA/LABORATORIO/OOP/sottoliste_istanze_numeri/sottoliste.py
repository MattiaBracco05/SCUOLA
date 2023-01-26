#4C Bracco Mattia - Sottoliste e istanze

import random
import os

def chiediN():
	MIN = 10
	MAX = 20
	N = int(input("Inserire il numero di elementi da aggiungere alla lista (" + str(MIN) + "-" + str(MAX) + "): "))
	while N < MIN or N > MAX:
		N = int(input("ERRORE!\nInserire il numero di elementi da aggiungere alla lista (" + str(MIN) + "-" + str(MAX) + "): "))
	return N
#------------------------------------------------------------------------------------------------------------------------------------
def riempiLista():
	MIN = 0
	MAX = 100
	for i in range(N):
		num = random.randint(MIN,MAX)
		lista.append(num)
#------------------------------------------------------------------------------------------------------------------------------------
def stampaLista(lista):
	print(lista)
#------------------------------------------------------------------------------------------------------------------------------------
def creaSottoliste():
	for i in range (N):
		if (lista[i] % 2) == 0:
			lista_pari.append(lista[i])
		else:
			lista_dispari.append(lista[i])
#------------------------------------------------------------------------------------------------------------------------------------
def sommaSottoListe():
	sommaPari = sum(lista_pari)
	sommaDispari = sum(lista_dispari)
	print("\nSomma sottolista pari: " + str(sommaPari) + "\nSomma sottolista dispari: " + str(sommaDispari))
	if sommaPari > sommaDispari:
		print("La sottolista pari ha la somma maggiore")
	else:
		print("La sottolista dispari ha la somma maggiore")
		
#------------------------------------------------------------------------------------------------------------------------------------
def contaSottoListe():
	lenPari = len(lista_pari)
	lenDispari = len(lista_dispari)
	print("\nElementi sottolista pari: " + str(lenPari) + "\nElementi sottolista dispari: " + str(lenDispari))
	if lenPari > lenDispari:
		print("La sottolista pari è quella che contiene più elementi")
	else:
		print("La sottolista dispari è quella che contiene più elementi")
#------------------------------------------------------------------------------------------------------------------------------------
def contaIstanze(lista):	
	for i in lista:
		contatore = lista.count(i)
		simboli = "*" * contatore
		print("Numero: {:3d}".format(i) + ": " + str(simboli))
#------------------------------------------------------------------------------------------------------------------------------------
lista = []
lista_pari = []
lista_dispari = []

os.system('clear')
N = chiediN()
riempiLista()
print("\nLISTA INIZIALE:")
stampaLista(lista)
creaSottoliste()
print("\nSOTTOLISTA PARI:")
stampaLista(lista_pari)
print("\nSOTTOLISTA DISPARI:")
stampaLista(lista_dispari)
sommaSottoListe()
contaSottoListe()
print("\nISTANZE SOTTOLISTA PARI:")
contaIstanze(lista_pari)
print("\nISTANZE SOTTOLISTA DISPARI:")
contaIstanze(lista_dispari)
