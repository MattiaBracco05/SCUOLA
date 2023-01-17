/*
4C Bracco Mattia - Mulino
File MuinoCC
*/

#include <stdio.h>
#include <stdlib.h>
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
void semLock(int);
void semUnlock(int);

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

	//variabili per shm e sem
	int semid = 0, shmid = 0;
	key_t keyshm = 1234, keysem = 5678;

	//variabili per il funzionamento del programma
	int count1 = 0, count2 = 0, count3 = 0, count4 = 0, count5 = 0;
	char nomeEvento[30];

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
	target -> eta = 0;
	target -> sala = 0;
	target -> stato = 0;
	
	//MI COLLEGO ALLA MEMORIA CONDIVISA e controllo un eventuale errore
	if((void*) target == (void*) -1) {
		printf("ERRORE collegamento memoria condivisa!\n");
		exit(-1);
	}
	
	//CREO I FILE DI REGISTRO PER GLI EVENTI
	//evento 1
	printf("Inserisci il nome dell'evento presente nella SALA 1: ");
	fgets(nomeEvento, 29, stdin);
	file = fopen("sala1.txt", "w");
	fprintf(file, "REGISTRO SALA 1\nNOME EVENTO: %s\n", nomeEvento);
	fclose(file);
	//evento 2
	printf("Inserisci il nome dell'evento presente nella SALA 2: ");
	fgets(nomeEvento, 29, stdin);
	file = fopen("sala2.txt", "w");
	fprintf(file, "REGISTRO SALA 2\nNOME EVENTO: %s\n", nomeEvento);
	fclose(file);
	//evento 3
	printf("Inserisci il nome dell'evento presente nella SALA 3: ");
	fgets(nomeEvento, 29, stdin);
	file = fopen("sala3.txt", "w");
	fprintf(file, "REGISTRO SALA 3\nNOME EVENTO: %s\n", nomeEvento);
	fclose(file);
	//evento 4
	printf("Inserisci il nome dell'evento presente nella SALA 4: ");
	fgets(nomeEvento, 29, stdin);
	file = fopen("sala4.txt", "w");
	fprintf(file, "REGISTRO SALA 4\nNOME EVENTO: %s\n", nomeEvento);
	fclose(file);
	//evento 5
	printf("Inserisci il nome dell'evento presente nella SALA 5: ");
	fgets(nomeEvento, 29, stdin);
	file = fopen("sala5.txt", "w");
	fprintf(file, "REGISTRO SALA 5\nNOME EVENTO: %s\n", nomeEvento);
	fclose(file);
  
  //attendo la 1° registrazione
  printf("In attesa delle registrazioni dei partecipanti...\n");
  
  //ciclo finchè stato è uguale a 0 --> registro il partecipante nel file dell'evento corrispondente
	while(target -> stato == 0) {
		if(target -> pid != 0) {
			//STAMPO A VIDEO
		  printf("Nuova registrazione effettuata! Partecipante ID: %d età: %d sala: %d\n", target -> pid, target -> eta, target -> sala);
		  //VERIFICO LA SALA DELL'EVENTO E SCRIVO NEI FILE
		  //se partecipa all'evento 1 -->
		  if(target -> sala == 1) {
		  	count1++;
		  	file = fopen("sala1.txt", "a");
		  	fprintf(file, "Partecipante Badge N.%d ID: %d età: %d\n", count1, target -> pid, target -> eta);
		  	fclose(file);
		  }
		  //se partecipa all'evento 2 -->
		  if(target -> sala == 2) {
		  	count2++;
		  	file = fopen("sala2.txt", "a");
		  	fprintf(file, "Partecipante Badge N.%d ID: %d età: %d\n", count2, target -> pid, target -> eta);
		  	fclose(file);
		  }
		  //se partecipa all'evento 3 -->
		  if(target -> sala == 3) {
		  	count3++;
		  	file = fopen("sala3.txt", "a");
		  	fprintf(file, "Partecipante Badge N.%d ID: %d età: %d\n", count3, target -> pid, target -> eta);
		  	fclose(file);
		  }
		  //se partecipa all'evento 4 -->
		  if(target -> sala == 4) {
		  	count4++;
		  	file = fopen("sala4.txt", "a");
		  	fprintf(file, "Partecipante Badge N.%d ID: %d età: %d\n", count4, target -> pid, target -> eta);
		  	fclose(file);
		  }
		  //se partecipa all'evento 5 -->
		  if(target -> sala == 5) {
		  	count5++;
		  	file = fopen("sala5.txt", "a");
		  	fprintf(file, "Partecipante Badge N.%d ID: %d età: %d\n", count5, target -> pid, target -> eta);
		  	fclose(file);
		  }
		  target -> pid = 0;
		}
	}
	
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
