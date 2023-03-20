//4C Bracco Mattia - Semaforo - File scrittore

//LIBRERIE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/sem.h>	//libreria che permette di includere i semafori

//DEFINE
#define SHM_SIZE 1024

//STRUTTURE
struct sembuf buffer; //struttura (strcut) di tipo "sembuf" chiamta "buffer"

//PROTOTIPI
void semLock(int);
void semUnlock(int);

//-----------------------------------------------------------------------------------------------------------------------------------
int main(){
	int shmid, semid, sem_stato;
	char *dati, stringa[20];
	key_t keyshm=1234, keysem=5678;
	
	//CREAZIONE DELLA MEMORIA E DEL SEMAFORO
	shmid = shmget(keyshm, SHM_SIZE, 0666 | IPC_CREAT );
	semid = semget(keysem, 1, 0666 | IPC_CREAT);
	
	//controllo eventuali errori (creazione della memoria || creazione del semaforo)
	if((shmid == -1) || (semid == -1)){
		printf("Errore nella creazione della memoria o nella creazione del semaforo\n");
		exit(-1);
	}
	
	//SET SEMAFORO
	sem_stato = semctl(semid, 0, SETVAL, 1);
	
	//AGGANCIO ALLA MEMORIA
	dati = (char *)shmat(shmid, NULL, 0);	//0 per i permessi di lettura/scrittura

	//controllo eventuale errore settaggio del semaforo
	if(sem_stato == -1) {
		printf("ERRORE nella settaggio del semaforo!\n");
		exit(-1);
	}
	
	//CICLO WHILE (INFINITO) PER SCRIVERE - COPIARE
	while(strcmp(stringa, "fine\n") != 0) {
	
		if(semctl(semid, 0, GETVAL) == 1) {
			//funzione per bloccare il semaforo
			semLock(semid);
			
			//azioni da eseguire (chiedo stringa - copio stringa)
			printf("Inserisci una stringa: ");
			fgets(stringa, 19, stdin);
			strcpy(dati, stringa);
			
			//funzione per sbloccare il semaforo
			semUnlock(semid);
		}	
	}
	printf("Esco dal ciclo while!\n");
	//DISTRUGGO IL SEMAFORO E LA MEMORIA
	sem_stato = semctl(semid, 0, IPC_RMID, 0);
	shmctl(shmid, IPC_RMID, NULL);
	printf("Memoria e semaforo distrutti\n");

	return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void semLock(int id){
	buffer.sem_num = 0;
	buffer.sem_flg = 0;
	buffer.sem_op = -1 ;
	if(semop(id, &buffer, 1) == -1){
		printf("Errore durante il blocco del semaforo\n");
	} else {
		printf("Semaforo bloccato correttamente\n");
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void semUnlock(int id){
	buffer.sem_num = 0;
	buffer.sem_flg = 0;
	buffer.sem_op = 1;
	if(semop(id, &buffer, 1) == -1){
		printf("Errore durante lo sblocco del semaforo\n");
	} else {
		printf("Semaforo sbloccato correttamente\n");
	}
}
