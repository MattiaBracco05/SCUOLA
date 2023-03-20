/*
Bracco Mattia 4C - Corsa SBK dei processi
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <sys/wait.h>
#define MIN_PARTECIPANTI 2
#define MAX_PARTECIPANTI 10
#define MIN_LITRI 50
#define MAX_LITRI 100
#define MIN_RAND_L 40
#define MAX_RAND_L 80
#define MIN_RAND_T 5
#define MAX_RAND_T 50

//PROTOTIPI
int chiediN();
int chiediL();

int main() {

	int N, L, i=0, num, serbatoio, tempo, count=0, min=(MAX_RAND_T+1), vincitore, stato_wait;
	pid_t chiSono, pid;

	N = chiediN();
	L = chiediL();
	printf("Alla gara parteciperanno %d concorrenti, il serbatoio di ciascuna moto è inizialmente stato riempito con %d litri di benzina\n", N, L);
	
	//CICLO PER GLI N CONCORRENTI...
	for (i=0; i<N; i++) {
	
		//creo il processo figlio
		if ((chiSono = fork()) < 0) {
			printf("Errore nella creazione della fork()!\n");
			exit(-1);
		}
		if (chiSono == 0) {
			srand(getpid());
			num = rand()%(MAX_RAND_L-MIN_RAND_L+1)+MIN_RAND_L;
			serbatoio = L - num;
			//controllo se il concorrente ha ancora benzina --> gareggia
			if (serbatoio > 0) {
				tempo = rand()%(MAX_RAND_T-MIN_RAND_T+1)+MIN_RAND_T;
				printf("(concorrente PID: %d), Gareggio! (%dL), Tempo: %d minuti\n", getpid(), serbatoio, tempo);
				exit(tempo);
			}
			//altrimenti --> non prende parte alla gara
			else {
				printf("(concorrente PID: %d), Il mio serbatoio è rimasto vuoto!, Non posso prendere parte alla gara :(\n", getpid());
				exit(0);
			}
		}
		
		//processo padre
		pid = wait(&stato_wait);
		if ((stato_wait >> 8) == 0) {
			count++;
		}
		else if ((stato_wait >> 8) < min) {
			min = (stato_wait >> 8);
			vincitore = pid;
		}
	}
	
	printf("\n");
	printf("In totale non hanno preso parte alla gara %d concorrenti\n", count);
	printf("Il vincitore è il concorrente PID: %d ed ha concluso la gara con un tempo di %d minuti\n", vincitore, min);
		
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val=0;
	while (val < MIN_PARTECIPANTI || val > MAX_PARTECIPANTI)	 {
		printf("Quanti concorrenti parteciperanno alla gara? (%d-%d): ", MIN_PARTECIPANTI, MAX_PARTECIPANTI);
		scanf("%d", &val);
	}
return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediL() {
	int val=0;
	while (val < MIN_LITRI || val > MAX_LITRI)	 {
		printf("Quanto litri di benzina vuoi nel serbatoio? (%d-%d): ", MIN_LITRI, MAX_LITRI);
		scanf("%d", &val);
	}
return val;
}
