# Es: esegui le quattro operazioni matematiche
# tra due numeri usando due funzioni di controllo dell'input
# una per gli interi e una per i reali

def inFloat():
	num = 0
	flag = True
	while flag == True:
		try:
			num = float(input("Dimmi un numero float: "))
			flag = False
		except ValueError :
			flag = True
			print("Non hai inserito un numero float")
	return num;
#------------------------------------------------------------------------------------------------------------------------------------
def inInt():
	num = 0
	flag = True
	while flag == True:
		try:
			num = int(input("Dimmi un numero intero: "))
			flag = False
		except ValueError :
			flag = True
			print("Non hai inserito un numero intero")
	return num
#------------------------------------------------------------------------------------------------------------------------------------
def somma( num1, num2 ):
	return num1 + num2
#------------------------------------------------------------------------------------------------------------------------------------
def differenza( num1, num2 ):
	return num1 - num2
#------------------------------------------------------------------------------------------------------------------------------------
def moltiplicazione( num1, num2 ):
	return num1 * num2
#------------------------------------------------------------------------------------------------------------------------------------
def divisione( num1, num2 ):
	try:
		return num1 / num2
	except ZeroDivisionError:		# se ho una divisione con
		return False					# divisore 0 ritorno False
#------------------------------------------------------------------------------------------------------------------------------------
# input

num1 = inFloat()
num2 = inInt()

# elaborazione e output

print("La somma vale: ", somma(num1, num2))
print("La differenza vale: ", differenza(num1, num2))
print("Il prodotto vale: ", moltiplicazione(num1, num2))

risultato = divisione(num1, num2)

if  risultato == False:
	print("Divisione impossibile!")
else:
	print("Il quoziente vale: ", risultato)
