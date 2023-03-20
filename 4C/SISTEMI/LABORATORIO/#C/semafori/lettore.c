//4C Bracco Mattia - Semaforo - File lettore

//LIBRERIE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/sem.h> //libreria che permette di includere i semafori

//DEFINE
#define SHM_SIZE 1024

//STRUTTURE
struct sembuf buffer;	//struttura (strcut) di tipo "sembuf" chiamta "buffer"

//PROTOTIPI
void semLock(int);
void semUnlock(int);

//-----------------------------------------------------------------------------------------------------------------------------------
int main(){
	
	int shmid, semid, sem_stato;
	char *dati, stringa[20];
	key_t keyshm=1234, keysem=5678;
	
	//CREAZIONE ID MEMORIA E ID SEMAFORO
	shmid = shmget(keyshm, SHM_SIZE, 0666);
	semid = semget(keysem, 1, 0666| IPC_EXCL);	//IPC_EXCL = utilizzo esclusivo
	
	//controllo eventuali errori (creazione della memoria || creazione del semaforo)
	if((shmid ==-1) || (semid==-1)){
		printf("Errore nella creazione della memoria o nela creazione del semaforo\n");
		exit(-1);
	}
	
	//AGGANCIO ALLA MEMORIA
	dati = (char *)shmat(shmid, NULL, SHM_RDONLY);
	

	while(1){
		/*
													***** controllo disponibilità risorse *****
		
		Contorllo se la risorsa è libera (valore == 1)
		Utilizzo "GETVAL" perchè in questo caso devo controllare un valore e non settarlo (SETVAL)
		Non dovendo settare il valore non passo il 4 parametro!
		Nel caso di un semaforo con più posti controllo che sia > di 0 (es. alunni che entrano in aula o parcheggio sotterraneo)
		*/
		if(semctl(semid, 0, GETVAL)==1){
			//funzione per bloccare il semaforo
			semLock(semid);
			
			//azioni da eseguire (chiedo stringa - copio stringa)
			printf("%s\n",dati);
			
			//funzione per sbloccare il semaforo
			semUnlock(semid);
		}	
	}
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void semLock(int id){
	buffer.sem_num = 0;
	buffer.sem_flg = 0;
	buffer.sem_op = -1;
	
	//blocco del semaforo con controllo di un eventuale errore
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
	
	//sblocco del semaforo con controllo di un eventuale errore
	if(semop(id, &buffer, 1) == -1){
		printf("Errore durante lo sblocco del semaforo\n");
	} else {
		printf("Semaforo sbloccato correttamente\n");
	}
}
