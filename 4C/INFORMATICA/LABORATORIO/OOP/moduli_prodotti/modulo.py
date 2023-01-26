#4C Bracco Mattia - Modulo funzioni
def calcolaSomma(N, prz, qta):
	somma = 0
	for i in range (N):
		somma = somma + (prz[i] * qta[i]) 
	return somma
#------------------------------------------------------------------------------------------------------------------------------------
def calcolaMedia(N, lista):
	somma = sum(lista)
	media = somma / N
	return media
