#4C Bracco Mattia - Gioco "Flappy Bird" ~ V1

import os
from os.path import join
from colorama import Fore, Back, Style
os.system("clear")
#-------------------------------------------------------------------------------------------------------------------------------------
#Stampa dell'uccello
print(Back.GREEN + Fore.RED)
print("""
───────────▄██████████████▄───────
───────▄████░░░░░░░░█▀────█▄──────
──────██░░░░░░░░░░░█▀──────█▄─────
─────██░░░░░░░░░░░█▀────────█▄────
────██░░░░░░░░░░░░█──────────██───
───██░░░░░░░░░░░░░█──────██──██───
──██░░░░░░░░░░░░░░█▄─────██──██───
─████████████░░░░░░██────────██───
██░░░░░░░░░░░██░░░░░█████████████─
██░░░░░░░░░░░██░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
██░░░░░░░░░░░██░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
─▀███████████▒▒▒▒█▓▓▓███████████▀─
────██▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓█──
─────██▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓█──
──────█████▒▒▒▒▒▒▒▒▒▒██████████───
─────────▀███████████▀────────────
""")
#Stampa del nome
print(Style.RESET_ALL)
print(Fore.WHITE)
print("""
 _  _    _____   ____                            __  __       _   _   _       
| || |  / ____| |  _ \                          |  \/  |     | | | | (_)      
| || |_| |      | |_) |_ __ __ _  ___ ___ ___   | \  / | __ _| |_| |_ _  __ _ 
|__   _| |      |  _ <| '__/ _` |/ __/ __/ _ \  | |\/| |/ _` | __| __| |/ _` |
   | | | |____  | |_) | | | (_| | (_| (_| (_) | | |  | | (_| | |_| |_| | (_| |
   |_|  \_____| |____/|_|  \__,_|\___\___\___/  |_|  |_|\__,_|\__|\__|_|\__,_|

 ______ _                            ____  _         _   __      __   __ 
|  ____| |                          |  _ \(_)       | |  \ \    / /  /_ |
| |__  | | __ _ _ __  _ __  _   _   | |_) |_ _ __ __| |   \ \  / /    | |
|  __| | |/ _` | '_ \| '_ \| | | |  |  _ <| | '__/ _` |    \ \/ /     | |
| |    | | (_| | |_) | |_) | |_| |  | |_) | | | | (_| |     \  /      | |
|_|    |_|\__,_| .__/| .__/ \__, |  |____/|_|_|  \__,_|      \/       |_|
               | |   | |     __/ |                                     
               |_|   |_|    |___/      
""")

#Resetto lo stile della print
print(Style.RESET_ALL)

#Stampa dei dettagli del gioco (se flag è impostato a 1)
flagStampa = 0
if flagStampa == 1:
	print("""
 ____________________________________________________________________ 
|                                                                    |
|                            DETTAGLI                                |
|____________________________________________________________________|
La coordinata (x=0, y=0) si trova nell'angolo in alto a SX,
pertanto per alzare l'uccellino diminuisco il valore di y (-), per abbassarlo lo incremento (+)
transform.flip(oggetto, x, y) oggetto di base, boolean specchio asse x, boolean specchio asse y
 ____________________________________________________________________ 
|                                                                    |
|                             IMPORT                                 |
|____________________________________________________________________|
·pygame
·random
·colorama (serve per impostare colori alle print)
 ____________________________________________________________________ 
|                                                                    |
|                           VARIABILI                                |
|____________________________________________________________________|
uccelloX e uccelloY    -->    Coordinate (x e Y) dell'uccellino
uccelloVelY            -->    Velocità di caduta dell'uccellino
baseX                  -->    Coordinata X della base (uso la variabile solo per x, la y è costante al valore "400")
FPS                    -->    Numero di frame per secondo del gioco
VEL_AVANZAMENTO        -->    Velocità di avanzamento della base (effetto di movimento)
 ____________________________________________________________________ 
|                                                                    |
|                           FUNZIONI                                 |
|____________________________________________________________________|
inizializza()          -->    Inizializza la posizone dell'uccelino e la velocità di caduta
disegnaOggetti()       -->    Carica gli oggetti (immagini) sullo schermo in ordine di sovrapposzione (es. prima sfondo poi sprite)
aggiorna()             -->    Aggiorna gli FPS del gioco
gameOver()             -->    Scritta game over e aspetta che l'utente chiuda la finestra (X) o prema SPAZIO per ricominciare
	""")
#-------------------------------------------------------------------------------------------------------------------------------------
#Importo e inizializzo la pygame, importo la random
import pygame
import random
pygame.init()

#Importo le immagini
sfondo = pygame.image.load('immagini/sfondo.png')
uccello = pygame.image.load('immagini/uccello.png')
base = pygame.image.load('immagini/base.png')
tuboInferiore = pygame.image.load('immagini/tubo.png')
tuboSuperiore = pygame.transform.flip(tuboInferiore, False, True)
scrittaGameOver = pygame.image.load('immagini/gameover.png')

#Importo i file audio
soundPunto = pygame.mixer.Sound(join("audio", "soundPunto.wav"))
soundGameOver = pygame.mixer.Sound(join("audio", "soundGameOver.wav"))

#Carico il font e lo assegno alla variabile fnt
fnt = pygame.font.SysFont("Times New Roman", 24)

#Scrivo "Hello world!" e ottengo la Surface surf_text
scoreText = fnt.render("Score: -", True, "yellow")

#Creo la finestra di gioco (passo come parametro una tupla contenente i valori di x e di y)
SCHERMO = pygame.display.set_mode((288, 512))
FPS = 50
VEL_AVANZAMENTO = 3
#-------------------------------------------------------------------------------------------------------------------------------------
class Tubi():
	#costruttore
	def __init__(self):
		self.x = 300
		self.y = random.randint(-75, 150)
		print("Inferiore: ", self.y + 210)
		print("Superiore: ", self.y - 210)
		
	#Movimento del tubo verso l'uccello
	def avanza_e_disegna(self):
		self.x -= VEL_AVANZAMENTO
		SCHERMO.blit(tuboInferiore, (self.x, self.y + 210))
		SCHERMO.blit(tuboSuperiore, (self.x, self.y - 210))
	
	#Collisione con l'uccellino
	def collisione(self, uccello, uccelloX, uccelloY):
		#Tolleranza per la collisione (l'uccello è "tondo" ma viene gestito come un rettangolo)
		tolleranza = 5
		
		#Coordinate dei lati SX e DX
		#uccello
		uccelloLatoSX = uccelloX + tolleranza
		uccelloLatoDX = uccelloX + uccello.get_width() - tolleranza
		#tubi
		tubiLatoSX = self.x
		tubiLatoDX = self.x + tuboInferiore.get_width()
		 
		#Coordinate dei lati SÙ E GIÙ
		#uccello
		uccelloLatoSU = uccelloY + tolleranza
		uccelloLatoGIU = uccelloY + uccello.get_height() - tolleranza
		#tubi
		tubiLatoSU = self.y + 110
		tubiLatoGIU = self.y + 210
		
		#Controllo la collisione
		#verifico se l'uccello è nell'area pericolosa
		if (uccelloLatoDX > tubiLatoSX) and (uccelloLatoSX < tubiLatoDX):
			#Se sono nell'area pericolosa --> verifico se si scontra contro un tubo 
			if (uccelloLatoSU < tubiLatoSU) or (uccelloLatoGIU > tubiLatoGIU):
				gameOver()
#-------------------------------------------------------------------------------------------------------------------------------------
def inizializza():
	global uccelloX, uccelloY, uccelloVelY, baseX, tubi, score
	uccelloX, uccelloY = 60, 150
	uccelloVelY = 0
	baseX = 0
	tubi = []
	tubi.append(Tubi())
	score = -1
#-------------------------------------------------------------------------------------------------------------------------------------
def disegnaOggetti():
	SCHERMO.blit(sfondo,(0, 0))
	for tub in tubi:
		tub.avanza_e_disegna()
	SCHERMO.blit(scoreText, (110, 0))
	SCHERMO.blit(uccello, (uccelloX, uccelloY))
	SCHERMO.blit(base, (baseX, 400))
#-------------------------------------------------------------------------------------------------------------------------------------
def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)
#-------------------------------------------------------------------------------------------------------------------------------------
def gameOver():
	soundGameOver.play()
	SCHERMO.blit(scrittaGameOver, (50, 150))
	aggiorna()
	restart = False
	
	#Finchè non ricomincia (o l'utente chiude la finestra dall"x")
	while not restart:
		#Rilevo se nel buffer degli eventi si è verificato qualcosa
		for evento in pygame.event.get():
			#Verifico se l'evento è un tasto premuto e (and) se il tasto premuto è "SPAZIO"
			if(evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE):
				inizializza()
				restart = True
			#Verifico se si è verificato l'evento di chiusura (click sulla X della finestra)
			if evento.type == pygame.QUIT:
				pygamme.quit()
#-------------------------------------------------------------------------------------------------------------------------------------
inizializza()

while True:
	uccelloVelY += 1
	uccelloY += uccelloVelY
	disegnaOggetti()
	aggiorna()
	
	#Rilevo se nel buffer degli eventi si è verificato qualcosa
	for evento in pygame.event.get():
	
		#Verifico se l'evento è un tasto premuto e (and) se il tasto premuto è "FRECCIA SU"
		if(evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP):
			uccelloVelY = -10
		#Verifico se si è verificato l'evento di chiusura (click sulla X della finestra)
		if evento.type == pygame.QUIT:
			pygamme.quit()
		
	#Sposto la base e la faccio ricominciare prima che finisca
	baseX -= VEL_AVANZAMENTO
	if baseX < -45:
		baseX = 0
		
	#Controllo se l'uccello si è schiantato contro la base
	if uccelloY > 380:
		gameOver()
		
	#Se l'uccello è fuori pericolo dall'ultimo tubo --> ne aggiungo un altro
	if tubi[-1].x < 150:
		tubi.append(Tubi())
		soundPunto.play()
		score += 1
		print("Score: ", score)
		scoreText = fnt.render("Score: " + str(score), True, "yellow")
	
	#Controllo la collisone con il tubo
	for i in tubi:
		i.collisione(uccello, uccelloX, uccelloY)
