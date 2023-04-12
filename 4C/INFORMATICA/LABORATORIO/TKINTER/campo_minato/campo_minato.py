#4C Bracco Mattia - TKINTER Campo Minato

import random
from tkinter import *
from functools import partial
from tkinter import messagebox

matrice = []
posizione = []
righe = 9
colonne = 9
root = Tk()
root.title("Campo Minato")
root.geometry("440x500")
root.resizable(0,0)

matriceButton = []
celleScoperte = 0
celleFlag = []
numeroMine = 0

mioFont = ("Arial, 16")
#------------------------------------------------------------------------------------------------------------------------------------
def clickSX(matrice, lbl, x, y, key):
	global celleScoperte
	
	#SE C'È UNA MINA --> sconfitta()
	if matrice[x][y] == 9:
		lbl.configure(bg="black")
		sconfitta()
	#SE NON C'È UNA MINA --> sfondo bianco
	if matrice[x][y] != 9 and matrice[x][y] != 0 and matrice[x][y] != -1:
		lbl.configure(bg="white")
		lbl.configure(text = matrice[x][y])
		matrice[x][y] = -1
		celleScoperte += 1
		
	#TOLGO LE CELLE VICINE CHE NON HANNO MINE VICINO (valore "0")
	vittoria(celleScoperte)
	if matrice[x][y] == 0:
		lbl.destroy()
		scopriCelle(x,y)
#------------------------------------------------------------------------------------------------------------------------------------
def clickDX(matrice, lbl, x, y, key):
	global numeroMine
	numeroMine = 10
	#SE LA CELLA NON HA IL FLAG --> LO IMPOSTO
	if lbl["bg"] == "green":
		lbl.configure(bg="yellow", text="F")
		celleFlag.append(lbl)
	#SE LA CELLA HA IL FLAG --> LO RIMUOVO
	elif lbl["text"] == "F":
		lbl.configure(bg="green", text="")
		celleFlag.remove(lbl)
		
	#AGGIORNO LA SCRITTA SULLE MINE RIMANENTI (basata sui flag utilizzati)
	numeroMine = numeroMine - len(celleFlag)
	if numeroMine >= 0:
		print("Mine rimanenti: ", numeroMine)
	else:
		print("Flag esauriti!")
#------------------------------------------------------------------------------------------------------------------------------------
def griglia():
	matrice.clear()
	for x in range(righe):
		riga = []
		for y in range(colonne):
			riga.append(0)
		matrice.append(riga)
	mine(matrice)
#------------------------------------------------------------------------------------------------------------------------------------
def mine(matrice):
	global numeroMine
	i = 0
	while i < 10:
		riga = random.choice(matrice)
		mina = random.randint(0, len(riga))
		numeroMine = 0
		if riga[mina-1] == 9:
			continue
		else:
			riga[mina-1] = 9
			i += 1
#------------------------------------------------------------------------------------------------------------------------------------
def conteggioMine(matrice):
	for i in range(righe):	
		for j in range(colonne):
			if matrice[i][j] == 9:
				#*************** SX ***************
				if j > 0:
					#SX (UP)
					if i > 0:
						if matrice[i-1][j-1] < 9:
							matrice[i-1][j-1] += 1
					#SX
					if matrice[i][j-1] < 9:
						matrice[i][j-1] += 1
					#SX (DOWN)
					if i < (righe - 1):
						if matrice[i+1][j-1] < 9:
							matrice[i+1][j-1] += 1
				#*************** DX ***************
				if (j + 1) < righe:
					#DX (UP)
					if i > 0:
						if matrice[i-1][j+1] < 9:
							matrice[i-1][j+1] += 1
					#DX
					if matrice[i][j+1] < 9:
						matrice[i][j+1] += 1
					#DX (DOWN)
					if i < (righe - 1):
						if matrice[i+1][j+1] < 9:
							matrice[i+1][j+1] += 1
				#*************** UP ***************
				if i > 0:
					if matrice[i-1][j] < 9:
						matrice[i-1][j] += 1
				#*************** DOWN ***************
				if i < (righe - 1):
					if matrice[i+1][j] < 9:
						matrice[i+1][j] += 1
#------------------------------------------------------------------------------------------------------------------------------------
def scopriCelle(x,y):
	global celleScoperte
	#*************** DOWN ***************
	if (0 <= x+1 <= 8) and (0 <= y <= 8) and (matrice[x+1][y] != 9) and (matrice[x+1][y] != -1):
		celleScoperte +=1 
		if matrice[x+1][y] == 0:
			matrice[x+1][y] = -1
			matriceButton[x+1][y].destroy()
			scopriCelle(x+1, y)
		else:
			matriceButton[x+1][y].configure(text=matrice[x+1][y])
			matriceButton[x+1][y].configure(bg="white")
			matriceButton[x+1][y] = -1
	#*************** UP	***************
	if (0 <= x-1 <= 8) and (0 <= y <= 8) and (matrice[x-1][y] != 9) and (matrice[x-1][y] != -1):
		celleScoperte +=1 
		if matrice[x-1][y] == 0:
			matrice[x-1][y] = -1
			matriceButton[x-1][y].destroy()
			scopriCelle(x-1, y)
		else:
			matriceButton[x-1][y].configure(text=matrice[x-1][y])
			matriceButton[x-1][y].configure(bg="white")
			matriceButton[x-1][y] = -1
	#*************** SX ***************
	if (0 <= x <= 8) and (0 <= y-1 <= 8) and (matrice[x][y-1] != 9) and (matrice[x][y-1] != -1):
		celleScoperte +=1 
		if matrice[x][y-1] == 0:
			matrice[x][y-1] = -1
			matriceButton[x][y-1].destroy()
			scopriCelle(x, y-1)
		else:
			matriceButton[x][y-1].configure(text=matrice[x][y-1])
			matriceButton[x][y-1].configure(bg="white")
			matriceButton[x][y-1] = -1
	#*************** DX ***************
	if (0 <= x <= 8) and (0 <= y+1 <= 8) and (matrice[x][y+1] != 9) and (matrice[x][y+1] != -1):
		celleScoperte +=1 
		if matrice[x][y+1] == 0:
			matrice[x][y+1] = -1
			matriceButton[x][y+1].destroy()
			scopriCelle(x, y+1)
		else:
			matriceButton[x][y+1].configure(text=matrice[x][y+1])
			matriceButton[x][y+1].configure(bg="white")
			matriceButton[x][y+1] = -1
#------------------------------------------------------------------------------------------------------------------------------------
def vittoria(celle):
	if celle == 71:
		messagebox.showinfo("Vittoria", "Hai vinto!")
		#CHIEDO ALL'UTENTE SE VUOLE CONTINUARE A GIOCARE
		if messagebox.askyesno("Partita terminata", "Vuoi continuare a giocare?") == True:
			resetta()
			celleFlag.clear()
		else:
			root.destroy()
#------------------------------------------------------------------------------------------------------------------------------------
def sconfitta():
	#MOSTRO LA POSIZIONE DI TUTTE LE MINE
	for x in range(colonne):
		for y in range(righe):
			if matrice[x][y] == 9:
				matriceButton[x][y].configure(bg="black")
	#CHIEDO ALL'UTENTE SE VUOLE RIPROVARE
	if messagebox.askyesno("Partita terminata", "Vuoi riprovare?") == True:
		resetta()
		celleFlag.clear()
	else:
		root.destroy()
#------------------------------------------------------------------------------------------------------------------------------------
def resetta():
	global matrice, matriceButton, celleScoperte
	celleScoperte = 0
	matriceButton.clear()
	griglia()
	conteggioMine(matrice)
#------------------------------------------------------------------------------------------------------------------------------------
#Punteggio
punteggio = Label(text="Score: ", fg='black', font=mioFont)	
punteggio.grid(row=11, column=0, columnspan=5)
score = IntVar()
punteggioValore = Label(textvariable=score, fg='black', font=mioFont)	
punteggioValore.grid(row=11, column=6, columnspan=4)

#Flag usati
mineRimanenti = Label(text="Mine rimanenti: ", fg='black', font=mioFont)	
mineRimanenti.grid(row=12, column=0, columnspan=5)
mineRimanentiValore = Label(text=numeroMine, fg='black', font=mioFont)	
mineRimanentiValore.grid(row=12, column=6, columnspan=4)

#Button ESCI
btnEsci = Button(text="ESCI", bg='red', font=mioFont, command=root.destroy)
btnEsci.grid(row=13, column=0, columnspan=10, sticky=EW)
		
r = 0
c = 0
#Ciclo per il numero di righe
for x in range(righe):
	
	c = 0 #Imposto il valore delle colonne a "0"
	matriceButton.append([]) #Aggiungo una riga di button
	
	#Ciclo per il numero di colonne
	for i in range(colonne):
		Botton = Frame(root)
		nome = str(x*9+i) #Il nome del button = la sua posizione
		lbl = Button(Botton, text=[], bg='green', width="2", height="1", borderwidth = 3, name=nome)
		onclickSX = partial(clickSX, matrice, lbl, x, i)
		onclickDX = partial(clickDX, matrice, lbl, x, i)
		lbl.bind("<Button-1>", onclickSX)
		lbl.bind("<Button-3>", onclickDX)
		Botton.grid(row=r, column=c)
		lbl.grid(row=r, column=c)
		matriceButton[x].append(lbl)
		c = c + 1 #Incremento il contatore delle colonne
	
	r = r +1 #Incremento il contatore delle righe
#------------------------------------------------------------------------------------------------------------------------------------
messagebox.showinfo("Istruzioni", "Istruzioni del gioco")
print("Mine totali: 10")
griglia()
conteggioMine(matrice)
root.mainloop()
