//4C Bracco Mattia - Memoria Condivisa lettore/scrittore su 2 file distinti - File lettore

//LIBRERIE PER I PROCESSI
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

//PROTOTIPI
void lettore(int);

//definsico la dimensione in mondo da poterla richiamare nel codice
#define SHM_SIZE 1024

int main() {
	
	key_t chiave; 	//chiave della memoria (key_t)
	int shmid;		//identificativo della meoria (int)
	chiave = 1234; 	//assegno un valore alla chiave (come una password) MAI USARE COME CHIAVE 0000!
	
	pid_t chiSono;
	
	//CREAZIONE DELLA MEMORIA CONDIVISA
	shmid = shmget(chiave, SHM_SIZE, 0666); //a diffrenze del file scrittore non scrivo "| IPC_CREAT"
	
	//controllo eventuale errore
	if(shmid == -1) {
		printf("ERRORE nella creazione della memoria!\n");
		exit(-1);
	}
	
	//CREO IL PROCESSO FIGLIO
	if( (chiSono = fork()) < 0) {
		printf("ERRORE nella creazione della fork!\n");
		exit(-1);
	}
	//PROCESSO FIGLIO (lettore)
	if(chiSono == 0) {
		lettore(shmid);
		exit(0);
	}
	//PROCESSO PADRE --> attende il processo figlio
	else {
		wait(NULL);
	}
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void lettore(int id) {
	int i;
	int *p; 	//dichiaro "p" come un puntatore (*)
	
	p = (int *)shmat(id, NULL, 0);
	
	//controllo se si è verificato un errore
	if(p == (int *)-1) {
		printf("ERRORE! nella shmat\n");
		exit(-2);
	}
	
	//ciclo for --> stampo i numeri
	for(i=1; i<6; i++) {
		printf("%d | ", p[i]);
	}
	printf("\n");
	
	p[0] = 0;
}
