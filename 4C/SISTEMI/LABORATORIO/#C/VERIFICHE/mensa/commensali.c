/*
4C Bracco Mattia - sgranocchiamo tutto
File commensali
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
#define MIN_COMMENSALI 20
#define MAX_COMMENSALI 50

//STRUTTURE
struct sembuf buffer;
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int main(){
	int shmid, semid, i, N, menu, hoMangiato=0, stato;
	int *tavoli; // puntatore all'area di memoria condivisa
	pid_t chiSono;
	key_t keyshm=1234, keysem=5678;
	
	system("clear");
	
	//CREO LA MEMORIA CONDIVISA E IL SEMAFORO
	shmid = shmget(keyshm, sizeof(int)*4 , IPC_EXCL | 0666); 
	semid = semget(keysem, 3,  IPC_EXCL | 0666);         
  //controllo eventuali errori
	if (shmid == -1 || semid == -1){
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}
	
	//MI AGGANCIO ALLA MEMORIA CONDIVISA
	tavoli = (int *) shmat(shmid, NULL,0);
	
	//CHIEDO IL NUMERO DI COMMENSALI
	printf("SGRANOCCHIAMO DI TUTTO - Commensali\n");
	N = chiediN();
	printf("OK! Procediamo alla registrazione di %d commensali...\n", N);
	
	//CICLO PER IL NUMERO DI COMMENSALI
	for(i=0; i<N; i++) {
	
		//creo un processo figlio e controllo un eventuale errores
		if((chiSono=fork()) < 0){
			printf("Errore nella fork\n");
			exit(-1);
		}
		//processo figlio (commensale)
		if(chiSono == 0) {
			srand(getpid()); 		//srand con getpid() per avere numeri casuali
			menu = rand() % 3; 	//scelgo random uno dei 3 menù
			
			//ciclo while finchè il commensale non ha mangiato
			while(hoMangiato == 0) {
			
				//controllo disponibilità risorse
				if(semctl(semid, menu, GETVAL) > 0) {
				
					//blocco il semaforo
					semLock(semid,menu);
					
					//azioni da eseguire (mangiare per 3 secondi al rispettivo tavolo)
					printf("Il commensale PID: %d ha scelto il menu %d. Posti liberi rimanenti al tavolo: %d\n", getpid(), menu, semctl(semid, menu, GETVAL));
					tavoli[menu] += 1;	//occupo un posto al tavolo
					hoMangiato = 1;		//imposto il flag per aver mangiato a 1
					sleep(3);			//sleep di 3 secondi (tempo in cui mangia)
					
					//sblocco il semaforo
					semUnlock(semid,menu);
				}
			}
			
		exit(1);
		}	
	}
	//(padre) ASPETTO I PROCESSI FIGLI (commensali)
	for(i=0; i<N; i++) {
		wait(&stato);
	}
	
	//quando tutti i commensali hannno mangiato
	printf("Tutti i commensali hanno finito il loro pasto\n");
	tavoli[3]=0;
	
return 0;
}
//---------------------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val = 0;
	while (val < MIN_COMMENSALI || val > MAX_COMMENSALI) {
		printf("Quanti commensali vuoi registrare? (%d-%d): ", MIN_COMMENSALI, MAX_COMMENSALI);
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
