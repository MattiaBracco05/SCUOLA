//4C Bracco Mattia - Semafori Babbo natale - File bambini.c (postino)

#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<stdbool.h>
//LIBRERIE PER I PROCESSI
#include<unistd.h>
#include<sys/wait.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include<sys/ipc.h>
#include<sys/shm.h>
#include<sys/sem.h>
#include<sys/types.h>

//DEFINE
#define BAMBINI_MIN 2
#define BAMBINI_MAX 10 
#define REGALO_MIN 1
#define REGALO_MAX 20

//PROTOTIPI
int chiediN();
int chiediRegalo();
void semLock(int);
void semUnlock(int);

//STRUTTURE
struct sembuf buffer;
struct res {
	pid_t pid;
	int reg;
	int stat;
};
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
int main() {
	
	//variabili per shm, sem e fork
	int semid, shmid;
	pid_t chiSono;
	key_t keysem = 1434, keyshm = 4678;
	
	//variabili per il funzionamento del programma
	int N, i, regalo;
	
	struct res *target;

	//CREO LA MEMORIA CONDIVISA E IL SEMAFORO
	shmid = shmget(keyshm, sizeof(struct res), 0666);
	semid = semget(keysem, 1, 0666 | IPC_EXCL);
	//controllo eventuali errori
	if(shmid < 0 || semid < 0) {
		printf("ERRORE durante la creazione della memoria condivisa o del semaforo!\n");
		exit(-1);
	}
	
	//MI COLLEGO ALLA MEMORIA CONDIVISA
	target = (struct res*) shmat(shmid, NULL, 0);
	//controllo eventuale errore
	if((void*) target == (void*) -1) {
		printf("ERRORE durante la connessione alla memoria condivisa!\n");
		exit(-1);	
	}

	N = chiediN(); //chiedo il numero di bambini da creare

	//CICLO PER IL NUMERO DI BAMBINI DA CREARE
	for(int i=0; i<N; i++) {
	
		//CREO UN PROCESSO FIGLIO (bambino)
		if((chiSono = fork()) < 0) {
			printf("ERRORE durante la creazione della fork()!\n");
			exit(-1);
		}
		//FIGLIO --> richiede il regalo
		else if(chiSono == 0) {
			regalo = 0;
			//CICLO WHILE
			while(true) {
				//CONTROLLO LA DISPONIBILITÀ DELLE RISORSE
				if(semctl(semid, 0, GETVAL) == 1) {

					//blocco il semaforo
					semLock(semid);
					
					//azioni da eseguire
					regalo = chiediRegalo();
					target -> pid = getpid();
					target -> reg = regalo;
          while(target -> pid != 0);
          
          //sblocco il semaforo e faccio l'exit
					semUnlock(semid);
					exit(0);
				}
			} 	//chiudo ciclo while
		} 		//chiudo processo figlio
	} 			//chiudo ciclo for
	
	//PADRE --> aspetta il figlio e chiude
	for(int i = 0; i < N; i++) {
		wait(NULL);
	}

	target -> stat = 1;

return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val = 0;
	while (val < BAMBINI_MIN || val > BAMBINI_MAX) {
		printf("Quanti bambini vuoi creare? (%d-%d): ", BAMBINI_MIN, BAMBINI_MAX);
		scanf("%d", &val);
	}
	return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
int chiediRegalo() {
	int val = 0;
	while (val < REGALO_MIN || val > REGALO_MAX) {
		printf("Inserire un regalo da richiedere a Babbo Natale (%d-%d): ", REGALO_MIN, REGALO_MAX);
		scanf("%d", &val);
	}
	return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
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
//-----------------------------------------------------------------------------------------------------------------------------------
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
