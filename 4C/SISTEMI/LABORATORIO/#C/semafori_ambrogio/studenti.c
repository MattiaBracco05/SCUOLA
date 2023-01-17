/*
4C Bracco Mattia - Ambrogio
File studenti
*/
#include <stdio.h>
#include <stdlib.h>
//LIBRERIE PER I PROCESSI
#include <sys/wait.h>
#include <unistd.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>

//PROTOTIPI
void semLock (int, int);
void semUnlock (int, int);
int chiediN();

//DEFINE
#define MIN_STUDENTI 20
#define MAX_STUDENTI 50

//STRUTTURE
struct sembuf buffer;
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int main(){
	int shmid, semid, i, N, scelta, vassoioPosato=0, stato;
	int *carrelli; // puntatore all'area di memoria condivisa
	pid_t chiSono;
	key_t keyshm=1234, keysem=5678;
	
	system("clear");
	
	//CREO LA MEMORIA CONDIVISA (3 celle di interi --> 1 per la sincronizzazione 2 per i carrelli) E 2 SEMAFORI
	shmid = shmget(keyshm, sizeof(int)*3 , IPC_EXCL | 0666); 
	semid = semget(keysem, 2,  IPC_EXCL | 0666);         
  //controllo eventuali errori
	if (shmid == -1 || semid == -1){
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}
	
	//MI AGGANCIO ALLA MEMORIA CONDIVISA
	carrelli = (int *) shmat(shmid, NULL,0);
	
	//CHIEDO IL NUMERO DI STUDENTI
	N = chiediN();
	printf("OK! Procediamo alla registrazione di %d studenti...\n", N);
	
	//CICLO PER IL NUMERO DI STUDENTI
	for(i=0; i<N; i++) {
	
		//creo un processo figlio e controllo un eventuale errore
		if((chiSono = fork()) < 0){
			printf("Errore nella fork\n");
			exit(-1);
		}
		//processo figlio (studente)
		if(chiSono == 0) {
			srand(getpid()); 		//srand con getpid() per avere numeri casuali
			scelta = rand()%2; 	//scelgo random uno dei 2 carrelli (0 o 1)
			
			//ciclo while finchè il commensale non ha mangiato
			while(vassoioPosato == 0) {
			
				//controllo disponibilità risorse
				if(semctl(semid, scelta, GETVAL) > 0) {
				
					//blocco il semaforo
					semLock(semid,scelta);
					
					//azioni da eseguire (posare il vassoio)
					printf("Lo studente PID: %d ha scelto di posare il vassoio nel carrello %d. Posti ancora liberi nel carrello: %d\n", getpid(), scelta, semctl(semid, scelta, GETVAL));
					carrelli[scelta] += 1;	//occupo un posto nel carrello
					vassoioPosato = 1;			//imposto il flag per il vassoio posato a 1
					sleep(2);								//sleep di 2 secondi (tempo in cui posa il vassoio)
					
					//sblocco il semaforo
					semUnlock(semid, scelta);
				}
			}
			
		exit(1);
		}	
	}
	//(padre) ASPETTO I PROCESSI FIGLI (studenti)
	for(i=0; i<N; i++) {
		wait(&stato);
	}
	
	//quando tutti gli studenti hannno mangiato
	printf("Tutti gli studenti hanno posato il proprio vassoio\n");
	carrelli[2] = 0;
	
return 0;
}
//---------------------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val = 0;
	while (val < MIN_STUDENTI || val > MAX_STUDENTI) {
		printf("Quanti studenti vuoi registrare? (%d-%d): ", MIN_STUDENTI, MAX_STUDENTI);
		scanf("%d", &val);
	}
return val;
}
//---------------------------------------------------------------------------------------------------------------------------------------------
void semLock (int semid, int id) {
	buffer.sem_num = id;
	buffer.sem_flg = 0;
	buffer.sem_op = -1;
	//controllo eventuale errore
	if(semop(semid,&buffer,1) == -1) {
		printf("Errore blocco semaforo\n");
	}
}
//---------------------------------------------------------------------------------------------------------------------------------------------
void semUnlock (int semid, int id) {
	buffer.sem_num = id;
	buffer.sem_flg = 0;
	buffer.sem_op = 1;
	//controllo eventuale errore
	if(semop(semid, &buffer, 1) == -1) {
		printf("Errore sblocco semaforo\n");
	}
}
