/*
4C Bracco Mattia - Semaforo
File scrittore
*/

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
	shmid = shmget(keyshm, SHM_SIZE, 0666| IPC_CREAT );
	semid = semget(keysem, 1, 0666| IPC_CREAT);
	
	//controllo eventuali errori (creazione della memoria || creazione del semaforo)
	if((shmid == -1) || (semid == -1)){
		printf("Errore nella creazione della memoria o nella creazione del semaforo\n");
		exit(-1);
	}
	
	//SET SEMAFORO
	sem_stato = semctl(semid, 0, SETVAL, 1);
	/*
																							*****	semctl *****
						
	semid  	--> Identificativo del semaforo
	0 		 	-->	Perchè ho un semaforo con solo 1 cella (la 1° cella è la numero 0)
						  Nel caso di un semaforo con più celle occorre effettuare una semctl per ogni cella (possibile ciclo for)
	SETVAL	-->	Per settare il valore
	1				-->	Inizializzo il valore della cella a "1"
							Posso paragonare quel numero hai posti liberi (es. alunni che devono entrare in aula o parcheggio sotterraneo)
	*/
	
	//AGGANCIO ALLA MEMORIA
	dati = (char *)shmat(shmid, NULL, 0);	//0 per i permessi di lettura/scrittura

	//controllo eventuale errore settaggio del semaforo
	if(sem_stato == -1) {
		printf("ERRORE nella settaggio del semaforo!\n");
		exit(-1);
	}
	
	//CICLO WHILE (INFINITO) PER SCRIVERE - COPIARE
	while(1){
		/*
													***** controllo disponibilità risorse *****
		
		Contorllo se la risorsa è libera (valore == 1)
		Utilizzo "GETVAL" perchè in questo caso devo controllare un valore e non settarlo (SETVAL)
		Non dovendo settare il valore non passo il 4 parametro!
		Nel caso di un semaforo con più posti controllo che sia > di 0 (es. alunni che entrano in aula o parcheggio sotterraneo)
		*/
		if(semctl(semid, 0, GETVAL)==1) {
			//funzione per bloccare il semaforo
			semLock(semid);
			
			//azioni da eseguire (chiedo stringa - copio stringa)
			printf("Inserisci una stringa: ");
			scanf("%s",stringa);
			strcpy(dati, stringa);
			
			//funzione per sbloccare il semaforo
			semUnlock(semid);
		}	
	}
	
	//DISTRUGGO IL SEMAFORO E LA MEMORIA
	sem_stato = semctl(semid, 0, IPC_RMID, 0);
	shmctl(shmid, IPC_RMID, NULL);

	return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void semLock(int id){
	buffer.sem_num = 0;
	buffer.sem_flg = 0;
	buffer.sem_op =-1 ;
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
