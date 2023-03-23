//4C Bracco Mattia - Memoria condivisa lettore/scrittore

//SOLITE LIBRERIE PER I PROCESSI
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

//definsico la dimensione in mondo da poterla richiamare nel codice
#define SHM_SIZE 1024

//PROTOTIPI
void scrittore(int);
void lettore(int);

//-----------------------------------------------------------------------------------------------------------------
int main() {

	//chiave della memoria (key_t)
	key_t chiave;
	//identificativo della meoria (int)
	int shmid;	
	//assegno un valore alla chiave (come una password) MAI USARE COME CHIAVE 0000!
	chiave = 1234;
	
	pid_t chiSono;
	
	/*
		*****CREAZIONE DELLA MEMORIA CONDIVISA*****
	*/
	shmid = shmget(chiave, SHM_SIZE, 0666 | IPC_CREAT); //666 --> | R = 1 | W = 1 | X = 0 | --> a U-G-O, (Utente-Gruppo-Other), lo "0" davanti indica i numeri ottali
	//controllo un eventuale errore nella creazione della memoria
	if(shmid == -1) {
		printf("ERRORE nella creazione della memoria!\n");
		exit(-1);
	}
	
	/*
		*****UTILIZZO DELLA MEMORIA CONDIVISA*****
	*/
	
	/*
		PRIMO PROCESSO FIGLIO
		--> PROCESSO SCRITTORE
			--> Richiama la funzione scrittore
		IL PADRE ATTENDE CHE IL PROCESSO FIGLIO (scrittore) TERMINI
	*/
	if( (chiSono = fork()) < 0) {
		printf("ERRORE nella creazione della fork!\n");
		exit(-1);
	}
	//PROCESSO FIGLIO (scrittore)
	if(chiSono == 0) {
		scrittore(shmid);
		exit(0);
	}
	//PROCESSO PADRE --> attende il processo figlio
	else {
		wait(NULL);
	}
	
	/*
		SECONDO PROCESSO FIGLIO
		--> PROCESSO LETTORE
			--> Richiama la funzione lettore
		IL PADRE ATTENDE CHE IL PROCESSO FIGLIO (lettore) TERMINI
	*/
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
	
	/*
		*****DISTRUZIONE DELLA MEMORIA CONDIVISA*****
	*/
	shmctl(shmid, IPC_RMID, NULL);
	
	
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void scrittore(int id) {
	int i, num;
	int *p; 	//dichiaro "p" come un puntatore (*)
	
	//il flag impostato a "0" imposta i permessi per la scrittura
	p = (int *)shmat(id, NULL, 0);
	
	//controllo se si è verificato un errore
	if(p == (int *)-1) {
		printf("ERRORE! nella shmat\n");
		exit(-1);
	}
	
	//ciclo for --> chiedo l'inserimento dei numeri
	for(i=0; i<5; i++) {
		printf("Inserisci un numero: ");
		scanf("%d", &num);
		p[i] = num;
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void lettore(int id) {
	int i;
	int *p; 	//dichiaro "p" come un puntatore (*)
	
	//il flag impostato a "SHM_RDONLY" permette SOLO la lettura
	p = (int *)shmat(id, NULL, SHM_RDONLY);
	
	//controllo se si è verificato un errore
	if(p == (int *)-1) {
		printf("ERRORE! nella shmat\n");
		exit(-2);
	}
	
	//ciclo for --> stampo i numeri
	for(i=0; i<5; i++) {
		printf("%d | ", p[i]);
	}
	printf("\n");
}
