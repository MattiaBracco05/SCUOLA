/*
4C Bracco Mattia - Memoria condivisa lettore/scrittore stringhe
File lettore
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>

#define DIM 1024

int main() {

	int shmid;
	char *dati;
	key_t chiave = 1234;

	//CREAZIONE ID MEMORIA (La memoria è già stata creata dal file scrittore)
	shmid = shmget(chiave, DIM, 0666);
	//Controllo eventuale errore
	if(shmid == -1) {
		printf("ERRORE nella creazione della memoria!\n");
		exit(-1);
	}
	
	//AGGANCIO ALLA MEMORIA
	dati = (char *)shmat(shmid, NULL, 0);
	
	//1° LETTURA
	printf("Leggo la stringa\n");
	printf("%s", dati);
	
	//CICLO WHILE PER LA LETTURA CONTINUA
	while(strcmp(dati, "fine\n") != 0) {
		printf("%s", dati);
	}
	
	printf("Ho finito di leggere --> Il file scrittore può chiudere\n");
	sleep(4);
	strcpy(dati, "chiudi");
	
return 0;
}
