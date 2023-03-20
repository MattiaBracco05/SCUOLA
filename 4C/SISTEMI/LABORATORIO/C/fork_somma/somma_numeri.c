//Bracco Mattia 4C - N processi figli

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#define MIN 1
#define MAX 5

//PROTOTIPI
int chiediN();

int main() {
	
	int figli, i, num, totale=0, stato_wait;
	pid_t chiSono, pid;
	
	figli = chiediN();

	
	//ciclo per gli N figli...
	for (i=0; i<figli; i++) {
		//se < 0 --> errore
		if ((chiSono = fork()) < 0) {
			printf("Errore nella creazione della fork()!\n");
			exit(-1);
		}
		//se = 0 --> figlio
		if (chiSono == 0) {
			srand(getpid()); //"srand" con "getpid()" in modo che il seme sia sempre diverso (con "time(NULL)" avrebbero tutti lo stesso seme"
			num = rand()%50+1;
			printf("Processo figlio (PID: %d), numero: %d\n", getpid(), num);
			exit(num);
		}
	}
	
	//----processo padre----
	
	//ciclo per gli N figli...
	for (i=0; i<figli; i++) {
		pid = wait(&stato_wait);
		totale = totale + stato_wait;
		printf("Totale parziale al %d° figlio: %d\n", i+1, totale>>8);
	}
	printf("Tutti i processi figli sono stati chiusi!, Totale: %d\n", totale>>8);
	
	/*
		xxxxxxxx
		00001010	(10 in binario)
		
		00001010 00000000 --> spostato a destra di 8 posizioni (uguale a fare x256)
		
		1- 00000001
		2- 00000010
		3- 00000100
		4- 00001000
		5- 00010000
		6- 00100000
		7- 01000000
		8- 10000000
		
		Utilizzo ">>" per shiftare a destra e "<<" per shiftare a sinistra [Es. printf("Totale: %d\n", totale>>8);]
		Alternativa 1 - divido la somma per 256 [somma = (somma / 256)]
		Alternativa 2- uso WEXIT STATUS [somma = WEXITSTATUS(stato_wait);]
	*/
	
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val=0;
	while (val < MIN || val > MAX) {
		printf("Quanti figli vuoi generare? (%d-%d): ", MIN, MAX);
		scanf("%d", &val);
	}
return val;
}
