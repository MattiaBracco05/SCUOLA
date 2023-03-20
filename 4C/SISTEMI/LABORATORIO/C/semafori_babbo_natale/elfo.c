//4C Bracco Mattia - Semafori Babbo natale - File elfo.c (lettore)

#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<stdbool.h>
//LIBRERIE PER I PROCESSI
#include<sys/wait.h>
#include<unistd.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include<sys/shm.h>
#include<sys/sem.h>
#include<sys/ipc.h>
#include<sys/types.h>

struct res {
	pid_t pid;
	int reg;
	int stato;
};
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
int main() {
	
	//variabili per shm e sem
	int semid = 0, shmid = 0;
	char cont[100];
	key_t keysem = 1434, keyshm = 4678;
	
	//variabili per il funzionamento del programma
	int count=1;
	
	struct res *target;
	
	FILE* file;

	//CREO L'ID DELLA MEMORIA CONDIVISA E DEL SEMAFORO
	shmid = shmget(keyshm, sizeof(struct res), 0666 | IPC_CREAT);
	semid = semget(keysem, 1, 0666 | IPC_CREAT);
	//controllo eventuali errori
	if(shmid < 0 || semid < 0) {
		printf("ERRORE nella creazione della memoria condivisa o del semaforo!\n");
		exit(-1);
	}
	
	//SETTAGGIO DEL SEMAFORO
	int stato = semctl(semid, 0, SETVAL, 1);
	//controllo eventuale errore
	if(stato < 0) {
		printf("ERRORE durante il settaggio del semaforo!\n");
		exit(-1);
	}
	
	target = (struct res*) shmat(shmid, NULL, 0);
	target -> pid = 0;
	target -> reg = 0;
	target -> stato = 0;
	
	//MI COLLEGO ALLA MEMORIA CONDIVISA e controllo un eventuale errore
	if((void*) target == (void*) -1) {
		printf("ERRORE collegamento memoria condivisa!\n");
		exit(-1);
	}
	
	//creo il file	
	file = fopen("lista.txt", "w");
	fprintf(file, "LISTA RICHIESTE DEI BAMBINI\n");
	fclose(file);
	
	//apro il file
	file = fopen("lista.txt", "a");
  
  //attendo la 1° richiesta dei bambini
  printf("In attesa delle richieste dei bambini...\n");
  
  //ciclo finchè stato è uguale a 0 --> scrivo la richiesta nella lista
	while(target -> stato == 0) {
		if(target -> pid != 0) {
		  fprintf(file, "%d: Il bambino %d desidera come regalo: %d\n", count, target -> pid, target -> reg);
		  printf( "%d: Il bambino %d desidera come regalo: %d\n", count++, target -> pid, target -> reg);
		  target -> pid = 0;
		}
	}
	
	//chiudo il file
	fclose(file);
	
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
