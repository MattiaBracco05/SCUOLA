/*
4C Bracco Mattia - sgranocchiamo tutto
File commensali
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <time.h>
//LIBRERIE PER I PROCESSI
#include <sys/wait.h>
#include <unistd.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include <sys/shm.h>
#include <sys/sem.h>
#include <sys/ipc.h>
#include <sys/types.h>

//PROTOTIPI
int chiediN();
void semLock(int);
void semUnlock(int);

//DEFINE
#define MIN_COMMENSALI 2
#define MAX_COMMENSALI 50
#define MIN_MENU 0
#define MAX_MENU 3

//STRUTURE
struct sembuf buffer;
//---------------------------------------------------------------------------------------------------------------------------------------------
int main() {
	
	//variabili per shm, sem e fork
	int semid, shmid, *tavoli;
	pid_t chiSono;
	key_t  keyshm = 1234, keysem = 5678;
	
	//variabili per il funzionamento del programma
	int N, menuIns, hoMangiato;
	
	system("clear");
	printf("SGRANOCCHIAMO DI TUTTO - Commensali\n");
	
	//CREO LA MEMORIA CONDIVISA E IL SEMAFORO
	shmid = shmget(keyshm, sizeof(int)*4, 0666);
	semid = semget(keysem, 1, 0666 | IPC_EXCL);
	//controllo eventuali errori
	if(shmid < 0 || semid < 0) {
		printf("ERRORE durante la creazione della memoria condivisa o del semaforo!\n");
		exit(-1);
	}
	
	//MI COLLEGO ALLA MEMORIA CONDIVISA
	tavoli = (int *) shmat(shmid, NULL, 0);
	//controllo eventuale errore
	if((void*) tavoli == (void*) -1) {
		printf("ERRORE durante la connessione alla memoria condivisa!\n");
		exit(-1);	
	}
	
	//CHIEDO IL NUMERO DI COMMENSALI
	while(tavoli[3] != 1); //aspetto che la mensa sia pronta
	N = chiediN();
	printf("OK! Procediamo alla registrazione di %d commensali...\n", N);
	
	//CICLO PER IL NUMERO DI COMMENSALI DA REGISTRARE
	for(int i=0; i<N; i++) {
	
		//CREO UN PROCESSO FIGLIO (commensale)
		if((chiSono = fork()) < 0) {
			printf("ERRORE durante la creazione della fork()!\n");
			exit(-1);
		}
		
		//FIGLIO --> registrazione
		else if(chiSono == 0) {
			srand(getpid()); //"srand" con "getpid()" in modo che il seme sia sempre diverso (con "time(NULL)" avrebbero tutti lo stesso seme"
			menuIns = rand()%(MAX_MENU - MIN_MENU + 1) + MIN_MENU; //scelgo un menù random
			//CICLO WHILE
			while(hoMangiato == 0) {
				//CONTROLLO LA DISPONIBILITÀ DELLE RISORSE
				if(semctl(semid, menuIns, GETVAL) == 1) {

					//blocco il semaforo
					semLock(semid);
					
					//azioni da eseguire (registrazione random del menù scelto)
					if (menuIns == 0) {
						printf("Codice menù: %d | Menù scelto (random): pesce\n", menuIns);
					}
					if (menuIns == 1) {
						printf("Codice menù: %d | Menù scelto (random): carne\n", menuIns);
					}
					if (menuIns == 2) {
						printf("Codice menù: %d | Menù scelto (random): vegetariano\n", menuIns);
					}
          
          		tavoli[menuIns] += 1;
          		sleep(3);
          		hoMangiato = 1;
          		
					//sblocco il semaforo e faccio l'exit
					semUnlock(semid);
					exit(0);
				}
			} 	//chiudo ciclo while
		} 		//chiudo processo figlio
	} 			//chiudo ciclo for
	
	tavoli[3] = 0;
	
	//PADRE --> aspetta il figlio e chiude
	for(int i=0; i<N; i++) {
		wait(NULL);
	}

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
void semLock(int id){
	buffer.sem_num = 0;
	buffer.sem_flg = 0;
	buffer.sem_op = -1;
	
	//controllo blocco corretto / errore durante il blocco
	if(semop(id, &buffer, 1) == -1){
		printf("Errore durante il blocco del semaforo\n");
	} else {
		printf("Semaforo bloccato correttamente\n");
	}
}
//---------------------------------------------------------------------------------------------------------------------------------------------
void semUnlock(int id){
	buffer.sem_num = 0;
	buffer.sem_flg = 0;
	buffer.sem_op = 1;
	
	//controllo sblocco corretto / errore durante lo sblocco
	if(semop(id, &buffer, 1) == -1){
		printf("Errore durante lo sblocco del semaforo\n");
	} else {
		printf("Semaforo sbloccato correttamente\n");
	}
}
