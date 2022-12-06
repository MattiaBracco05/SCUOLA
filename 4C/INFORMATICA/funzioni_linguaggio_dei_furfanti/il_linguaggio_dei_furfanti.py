import os

def traduci(testoInserito, testoTradotto):
	for x in testoInserito:
		#se il testo è una vocale o un carattere speciale --> mantengo normale
		if x in lista_vocali or x in lista_speciali:
			testoTradotto += x
		#altrimenti --> raddoppio e inserisco una "o" al centro
		else:
			testoTradotto = testoTradotto + x + "o" + x
	#stampo il testo tradotto
	print("Testo tradotto: " + testoTradotto)
#------------------------------------------------------------------------------------------------------------------------------------
lista_vocali = "aeiou"
lista_speciali = [" ", ",", ".", "?", "!", '"',"'"]
    
uscita = 1
while uscita != 0:
	os.system("clear")
	testoInserito = input("\nInserisci il testo da tradurre: ")
	testoTradotto = ""
	traduci(testoInserito, testoTradotto)
	uscita = int(input("\nDigitare 0 per temrinare: "))
	
