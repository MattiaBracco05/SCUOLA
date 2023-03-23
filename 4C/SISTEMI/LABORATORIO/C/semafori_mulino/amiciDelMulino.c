//4C Bracco Mattia - Mulino - File AmiciDelMulino

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
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
int insEta();
int insSala();
void semLock(int);
void semUnlock(int);

//DEFINE
#define MIN_PARTECIPANTI 2
#define MAX_PARTECIPANTI 50
#define MIN_ETA 18
#define MIN_SALA 1
#define MAX_SALA 5

//STRUTURE
struct sembuf buffer;
struct res {
	pid_t pid;
	int eta;
	int sala;
	int stato;
};
//-----------------------------------------------------------------------------------------------------------------------------------
int main() {
	
	system("clear");
	
	//variabili per shm, sem e fork
	int semid, shmid;
	pid_t chiSono;
	key_t  keyshm = 1234, keysem = 5678;

	//variabili per il funzionamento del programma
	int N, etaIns, salaIns;
	struct res *target;
	
	//CHIEDO QUANTI PARTECIPANTI REGISTRARE
	N = chiediN();	
	printf("OK! Procediamo alla registrazione di %d partecipanti...\n", N);
	
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
	
	//CICLO PER IL NUMERO DI PARTECIPANTI DA REGISTRARE
	for(int i=0; i<N; i++) {
		//CREO UN PROCESSO FIGLIO (partecipante)
		if((chiSono = fork()) < 0) {
			printf("ERRORE durante la creazione della fork()!\n");
			exit(-1);
		}
		//FIGLIO --> registrazione
		else if(chiSono == 0) {
			etaIns = 0;
			salaIns = 0;
			//CICLO WHILE
			while(true) {
				//CONTROLLO LA DISPONIBILITÀ DELLE RISORSE
				if(semctl(semid, 0, GETVAL) == 1) {

					//blocco il semaforo
					semLock(semid);
					
					//azioni da eseguire
					etaIns = insEta();
					salaIns = insSala();
					target -> pid = getpid();
					target -> eta = etaIns;
					target -> sala = salaIns;
          while(target -> pid != 0);
          
          //sblocco il semaforo e faccio l'exit
					semUnlock(semid);
					exit(0);
				}
			} 	//chiudo ciclo while
		} 		//chiudo processo figlio
	} 			//chiudo ciclo for
	
	//PADRE --> aspetta il figlio e chiude
	for(int i=0; i<N; i++) {
		wait(NULL);
	}

	target -> stato = 1;
	
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val = 0;
	while (val < MIN_PARTECIPANTI || val > MAX_PARTECIPANTI) {
		printf("Quanti partecipanti vuoi registrare? (%d-%d): ", MIN_PARTECIPANTI, MAX_PARTECIPANTI);
		scanf("%d", &val);
	}
return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int insEta() {
	int val = 0;
	printf("Inserisci la tua età: ");
	scanf("%d", &val);
	while (val < MIN_ETA) {
		printf("La registrazione ai nostri eventi è vietata ai minori di %d anni! Inserisci la tua età: ", MIN_ETA);
		scanf("%d", &val);
	}
return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int insSala() {
	int val = 0;
	while (val < MIN_SALA || val > MAX_SALA) {
		printf("A quale sala vuoi partecipare? (%d-%d): ", MIN_SALA, MAX_SALA);
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
