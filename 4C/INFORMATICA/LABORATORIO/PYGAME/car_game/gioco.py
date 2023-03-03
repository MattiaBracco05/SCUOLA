#4C Bracco Mattia - Car Game

#IMPORT
from __future__ import division
import pygame, math, random, time

#Inizializzo la pygame
pygame.init()

#Display di gioco
pygame.display.set_caption('4C Bracco Car Game')
width = 800
height = 600
size = (width, height)
FPS = 120
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#********** IMPORTO GLI ASSETS **********
#IMPORTO I FONT
font = pygame.font.Font('fonts/cargo.ttf', 40)
score = pygame.font.Font('fonts/cargo.ttf', 30)
nos = pygame.font.Font('fonts/cargo.ttf', 30)
timer = pygame.font.Font('fonts/cargo.ttf', 30)
desc = pygame.font.Font('fonts/blueSmile.ttf', 30)
#IMPORTO LE IMMAGINI
background = pygame.image.load('immagini/Street.jpg')
player = pygame.image.load('immagini/Player.png')
enemy = pygame.transform.scale(pygame.image.load('immagini/Enemy.png'), (70, 145))
BMW = pygame.transform.scale(pygame.image.load('immagini/BMW.jpg'), (400, 300))
#IMPORTO I SUONI (effetti sonori + soundtrack)
tires = pygame.mixer.Sound('audio/tires_skid.ogg')
crash = pygame.mixer.Sound('audio/crash.ogg')
soundtrack = pygame.mixer.Sound('audio/soundtrack.mp3')
clacson = pygame.mixer.Sound('audio/clacson.ogg')
turbo = pygame.mixer.Sound('audio/turbo.ogg')
turboFlutter = pygame.mixer.Sound('audio/turboFlutter.mp3')
Vanzini = pygame.mixer.Sound('audio/Vanzini.mp3')

#LARGHEZZA DELLA MACCHINA (larghezza dell'immagine in pixel)
playerWidth = 49

backrect = background.get_rect()

#REGOLO IL VOLUME DEI SUONI
tires.set_volume(1)
crash.set_volume(2)
clacson.set_volume(2)
turbo.set_volume(0.3)
soundtrack.set_volume(0.5)
soundtrack.play(-1)
#-----------------------------------------------------------------------------------------------------------------------------------
def avvio():
		#Vanzini su i motori
		Vanzini.play()
	
		#Titolo
		comandi = desc.render("----- LISTA DEI COMANDI -----", True, (255, 255, 0))
		screen.blit(comandi, (180, 0))
		#Comandi
		leftArrow = desc.render("LEFT ARROW | Sterza a sinistra", True, (0, 0, 255))
		screen.blit(leftArrow, (180, 30))
		rightArrow = desc.render("RIGHT ARROW | Sterza a destra", True, (0, 0, 255))
		screen.blit(rightArrow, (180, 60))
		upArrow = desc.render("UP ARROW | Accelera", True, (0, 0, 255))
		screen.blit(upArrow, (180, 90))
		space = desc.render("SPACE | Clacson", True, (0, 0, 255))
		screen.blit(space, (180, 120))
		keyN = desc.render("N | NOS", True, (0, 0, 255))
		screen.blit(keyN, (180, 150))
		#Testo finale
		final = desc.render("Guida con prduenza!", True, (0, 255, 0))
		screen.blit(final, (250, 230))
		#Immagine BMW	
		screen.blit(BMW, (320, 280))
		
		#Aggiorno lo schermo
		pygame.display.update()
		screen.blit(background, backrect)
		
		#Tempo durata scritte
		time.sleep(6)
#-----------------------------------------------------------------------------------------------------------------------------------	
def punteggio(count):
	scoreFont = score.render("Score: %d" % count, True, (0, 0, 0))
	screen.blit(scoreFont, (50, 570))
#-----------------------------------------------------------------------------------------------------------------------------------	
def NOS(flag):
	if flag == 1:
		NOSFont = nos.render("NOS: Yes", True, (0, 0, 0))
	else:
		NOSFont = nos.render("NOS: No", True, (0, 0, 0))
	screen.blit(NOSFont, (620, 570))
#-----------------------------------------------------------------------------------------------------------------------------------		
def myEnemy(enemyX, enemyY):
	screen.blit(enemy, (enemyX, enemyY))
#-----------------------------------------------------------------------------------------------------------------------------------	
def myPlayer(x, y):
	screen.blit(player, (x, y))
#-----------------------------------------------------------------------------------------------------------------------------------	
def messaggioImpatto(tot):
	#Creo il messaggio per la collisone e lo mostro al centro dello schermo
	messaggio = font.render("Hai colpito un pickup!", True, (0, 0, 0))
	rect = messaggio.get_rect()
	rect.center = ((width // 2), (height // 2))	
	screen.blit(messaggio, rect)
	#Creo il messaggio con il punteggio e lo mostro
	finalScore = score.render("Final score: %d" % tot, True, (0, 0, 0))
	screen.blit(finalScore, (300, 350))
	
	#Aggiorno il display
	pygame.display.update()
	#Inizio una nuova partita
	nuovaPartita()
#-----------------------------------------------------------------------------------------------------------------------------------		
def messaggioUscito(tot):
	#Creo il messaggio per la collisone e lo mostro al centro dello schermo
	messaggio = font.render("Sei uscito di strada!", True, (0,0,0))
	rect = messaggio.get_rect()
	rect.center = ((width // 2), (height // 2))
	screen.blit(messaggio, rect)
	#Creo il messaggio con il punteggio e lo mostro
	finalScore = score.render("Final score: %d" % tot, True, (0, 0, 0))
	screen.blit(finalScore, (300, 350))
	
	#Aggiorno il display
	pygame.display.update()
	#Inizio una nuova partita
	nuovaPartita()
#-----------------------------------------------------------------------------------------------------------------------------------	
def nuovaPartita():
	time.sleep(1) #Aspetto un secondo a mostrare il countdown (in questo secondo visualizzo ancora il punteggio finale e il messaggio)
	#Countdown di 3 secondi
	i = 3
	while i > 0:
		timeText = timer.render("Nuova partita: %d" % i, True, (255, 255, 0))
		screen.blit(timeText, (270, 240))
		pygame.display.update()
		i -= 1
		screen.blit(background, backrect)
		time.sleep(1)
		
	#Avvio una nuova partita
	partita()
#-----------------------------------------------------------------------------------------------------------------------------------	
avvio()
def partita():
	#Player
	x = 351
	y = 480 	
	cambiaX = 0
	cambiaVel = 0
	#Enemy
	enemyX = random.randrange(50,770)
	enemyY = -500
	enemySpeed = 2
	enemyHeight = 145
	enemyWidth = 70
	#Variabili di gioco
	score = 0
	bonus = 0
	flagNOS = 1
	
	#Ciclo while true
	while True:
		clock.tick(FPS)
		
		#Ciclo per gli eventi che si sono verificati
		for event in pygame.event.get():
		
			#******************** TASTO EXIT (X) ********************
			#Controllo se l'utente ha cliccato la "X" per chiudere la finestra di gioco
			if event.type == pygame.QUIT:
				exit()
				
			#******************** TASTI PREMUTI ********************
			#Controllo se si è verificato un evento KEYDOWN (tasto premuto)
			if event.type == pygame.KEYDOWN:
				#Controllo se l'utente ha cliccato la freccia a sinistra --> sterzo a sinistra
				if event.key == pygame.K_LEFT:
					cambiaX = -6
				#Controllo se l'utente ha cliccato la freccia a destra --> sterzo a destra
				if event.key == pygame.K_RIGHT:
					cambiaX = 6
				#Controllo se l'utente ha cliccato freccia sù --> accelero
				if event.key == pygame.K_UP:
					cambiaVel = 0.1
					turboFlutter.play()
				#Controllo se l'utente ha premuto il tasto N e il NOS è disponibile (non ancora utilizzato) --> accelero
				if event.key == pygame.K_n and flagNOS == 1:
					for i in range(5):
						cambiaVel += 0.1
						turbo.play()
					flagNOS = 0 #imposto il flag a 0 (NOS esaurito)
				#Controllo se l'utente ha premuto il tasto SPAZIO --> clacson
				if event.key == pygame.K_SPACE:
					clacson.play()
					
			#******************** TASTI RILASCIATI ********************
			#Controllo se si è verificato un evento KEYUP (tasto rilasciato)
			if event.type == pygame.KEYUP:
				#Controllo se l'utente ha rilasciato la freccia a destra o la freccia a sinistra --> proseguo dritto
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					cambiaX = 0
				#Controllo se l'utente ha rilasciato la freccia sù --> smetto di accelerare
				if event.key == pygame.K_UP:
					cambiaVel = 0
				#Controllo se il NOS è esaurito --> riduco la velocità e imposto il flag a 2 (così riduce solo una volta)
				if flagNOS == 0:
					for i in range(5):
						cambiaVel -= 0.1
						score += 1
					flagNOS = 2
		
		#******************** AGGIORNO ********************
		#Aggiorno le variabili			
		x += cambiaX
		enemySpeed += cambiaVel
		#Disegno gli oggetti sullo schermo
		screen.blit(background, backrect)
		#Enemy
		myEnemy(enemyX, enemyY)
		enemyY += enemySpeed
		#Player
		myPlayer(x,y)
		#Variabili di gioco
		punteggio(score)	
		NOS(flagNOS)
		
		#******************** CONTROLLI IMPATTO ********************
		#Controllo se è uscito di strada
		if x > (width - 87) or x < 35:
			tires.play()
			crash.play()
			turbo.stop()
			messaggioUscito(score)
		#Controllo se ha sbattuto contro un pickup
		if y < enemyY + 145:
			if x > enemyX and x < enemyX + enemyWidth or x + playerWidth > enemyX and x + playerWidth < enemyX + enemyWidth:
				crash.play()
				turbo.stop()
				messaggioImpatto(score)
		#Controllo se ha evitato il pickup --> aumento la velocità e ne genero un altro
		if enemyY > height:
			enemyY =- 145
			enemyX = random.randrange(50,720)
			enemySpeed += 0.2
			score += 1
			#Bonus ogni 10 auto schivate --> + 10 punti
			bonus += 1
			if bonus > 9:
				bonus = 0 #azzero il bonus
				score += 15
		
		pygame.display.flip()
	
partita()
