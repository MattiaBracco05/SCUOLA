/*
4C Bracco Mattia - Ambrogio
File Ambrogio
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/wait.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include <sys/shm.h>
#include <sys/sem.h>
#include <sys/ipc.h>
#include <sys/types.h>

//PROTOTIPI
void semLock (int, int);
void semUnlock (int, int);

//STRUTTIRE
struct sembuf buffer;
//---------------------------------------------------------------------------------------------------------------------------------------------------------
int main() {
	int shmid, semid, i, semStato;
	int *carrelli;
	key_t keyshm=1234, keysem=5678;

	//CREO LA MEMORIA CONDIVISA E 2 SEMAFORI
	shmid = shmget(keyshm, sizeof(int)*3 , 0666 | IPC_CREAT); 
	semid = semget(keysem, 2, 0666 | IPC_CREAT);         
  //controllo eventuale errore
	if (shmid == -1 || semid == -1) {
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}
	
	//AGGANCIO ALLA MEMORUA
	carrelli = (int *) shmat(shmid, NULL,0);

	//SETTAGGIO INIZIALE DEI SEMAFORI (5 posti per i vassoi in ogni carrello)
	for (i=0; i<2 ;i++) {
		semStato = semctl(semid, i, SETVAL, 5);
	}
	
	//SETTAGGIO INIZIALE DEI CAREELLI NEL QUALE POSARE I VASSOI
	for (i=0;i<2;i++){
		carrelli[i] = 0;
	}
	
	//APRO LA MENSA
	printf(" ___________________________________ \n");
	printf("|                                   |\n");
	printf("|         LA MENSA È APERTA         |\n");
	printf("|___________________________________|\n");
	printf("È adesso possibile avviare il file studenti\n");
	carrelli[2] = 1;

	//RICEVO GLI STUDENTI
	while(carrelli[2] !=  0){
		printf("Ricevendo gli studenti...\n");
		sleep(1);
		
		//CICLO PER IL NUMERO DI CARRELLI
		for(i=0; i<2; i++) {
			//SE IL CARRELLO 0 È PIENO -->
			if(carrelli[i] == 5) {
				printf("Il carrello n.%d è momentaneamente pieno!\n", i);
				//SVUOTO IL CARRELL0
				printf("Procedo a svotare il carrello n.%d\n", i);
				carrelli[i] = 0;
				sleep(2);
				printf("Il carrello n.%d è stato svuotato!\n", i);
			}
		}
		
	}
	
	printf(" ___________________________________ \n");
	printf("|                                   |\n");
	printf("|         LA MENSA È CHIUSA         |\n");
	printf("|___________________________________|\n");
	
	//DISTRUGGO LE MEMORIA CONDIVSA E I 2 SEMAFORI
	shmctl(shmid, IPC_RMID, NULL);
	for(i=0; i<2; i++){
		semctl(semid, i, IPC_RMID, 0);
	}
	
return 0;
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
