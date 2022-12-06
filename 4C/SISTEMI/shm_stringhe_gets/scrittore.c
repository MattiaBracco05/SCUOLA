/*
4C Bracco Mattia - Memoria condivisa lettore/scrittore stringhe
File scrittore
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
	char *dati, stringa[50];
	key_t chiave = 1234;
	
	//CREAZIONE DELLA MEMORIA
	shmid = shmget(chiave, DIM, 0666 | IPC_CREAT);
	//Controllo eventuale errore
	if(shmid == -1) {
		printf("ERRORE nella creazione della memoria!\n");
		exit(-1);
	}
	
	//AGGANCIO ALLA MEMORIA
	dati = (char *)shmat(shmid, NULL, 0);
	//Controllo eventuale errore
	if(dati == (char *) -1) {
		printf("ERRORE durante l'aggancio della memoria!\n");
		exit(-2);
	}
	
	//1° INSERIMENTO
	printf("Inserisci una stringa: ");
	gets(stringa);
	strcpy(dati, stringa);
	
	//CICLO WHILE PER L'INSERIMENTO CONTINUO
	while(strcmp(stringa, "fine") != 0) {
		printf("Inserisci una stringa: ");
		gets(stringa);
		strcpy(dati, stringa);
	}
	
	printf("Esco dal while dell'inserimento\n");
	
	//attendo la stampa dell'ultima parola
	while(strcmp(dati, "chiudi") != 0) {
		sleep(3);
	}
	
	//DISTRUZIONE DELLA MEMORIA CONDIVISA
	shmctl(shmid, IPC_RMID, NULL);
	printf("Memoria distrutta");
	
return 0;
}
