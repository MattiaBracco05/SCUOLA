/*
4C Bracco Mattia - sgranocchiamo tutto
File mensa
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <time.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include <sys/shm.h>
#include <sys/sem.h>
#include <sys/ipc.h>
#include <sys/types.h>

//STRUTURE
struct sembuf buffer;
//---------------------------------------------------------------------------------------------------------------------------------------------------------
int main() {

	system("clear");
	printf("SGRANOCCHIAMO DI TUTTO - Mensa\n");
	
	//variabili per shm e sem
	int semid=0, shmid=0, stato, *tavolo, i;
	key_t keyshm=1234, keysem=5678;

	//CREO L'ID DELLA MEMORIA CONDIVISA E DEL SEMAFORO
	shmid = shmget(keyshm, sizeof(int)*4, 0666 | IPC_CREAT);
	semid = semget(keysem, 3, 0666 | IPC_CREAT);
	//controllo eventuali errori
	if(shmid < 0 || semid < 0) {
		printf("ERRORE nella creazione della memoria condivisa o del semaforo!\n");
		exit(-1);
	}
	
	//MI COLLEGO ALLA MEMORIA CONDIVISA e controllo un eventuale errore
	if((void*) tavolo == (void*) -1) {
		printf("ERRORE collegamento memoria condivisa!\n");
		exit(-1);
	}
	
	//CICLO FOR PER IL SETTAGGIO DEI SEMAFORI PER I 3 TAVOLI
	for (i=0; i<4; i++) {
		//setto il semaforo del tavolo e controllo un eventuale errore
		stato = semctl(semid, i, SETVAL, 4);
	}
	
	//INIZIALIZZO I TAVOLI COME VUOTI
	tavolo = (int *) shmat(shmid, NULL, 0);
	for(i=0; i<4; i++) {
		tavolo[i] = 0;
	}
	
	//APRO LA MENSA (la 4 cella (3) la uso come flag per l'apertura)
	printf("LA MENSA È APERTA!\n");
	tavolo[3] = 1;
	
	//RICEVO I COMMENSALI
	while(tavolo[3] != 0) {
		printf("Mensa...\n");
		sleep(3);	
	}

	//RESOCONTO	
	printf("\n");
	printf(" ___________________________________ \n");
	printf("|                                   |\n");
	printf("|       RESOCONTO GIORNALIERO       |\n");
	printf("|___________________________________|\n");
	printf("Menù di pesce: %d commensali\n", tavolo[0]);
	printf("Menù di carne: %d commensali\n", tavolo[1]);
	printf("Menù vegeteariano: %d commensali\n", tavolo[2]);
	
	//DISTRUGGO LA MEMORIA CONDIVISA
	stato = shmctl(shmid, IPC_RMID, NULL);
	//controllo eventuale errore
	if(stato < 0) {
		printf("ERRORE durante la distruzione della memoria condivisa!\n");
		exit(-1);
	}
	
	//DISTRUGGO IL SEMAFORO
	stato = semctl(semid, 0, IPC_RMID, 0);
	//controllo eventuale errore
	if(stato < 0) {
		printf("ERRORE durante la distruzione del semaforo!\n");
		exit(-1);
	}
	
return 0;
}
