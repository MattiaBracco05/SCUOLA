#Bracco Mattia 4C - Tabelline
num = int(input("Inserisci il numero di cui vuoi sapere la tabellina: "))
for i in range(10):
	risultato = num * (i + 1)
	print(num, "*", (i+1), "=", risultato)
print("Esco dal programma")
