#4C BRACCO MATTIA - Gestione degli errory con try e except
flag = False

while flag == False:
	str_num = input("Inserire un numero intero: ")
	try:
		numImmesso = int(str_num)
		flag = True
	except:
		print("Non hai inserito un numero!")
		
print("Conversione riuscita!")
