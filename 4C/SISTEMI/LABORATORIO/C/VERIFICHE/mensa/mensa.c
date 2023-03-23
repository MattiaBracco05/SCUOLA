//4C Bracco Mattia - sgranocchiamo tutto - File mensa

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
//LIBRERIE PER LA MEMORIA CONDIVISA
#include <sys/shm.h>
#include <sys/sem.h>
#include <sys/ipc.h>
#include <sys/types.h>

//STRUTTIRE
struct sembuf buffer;

//---------------------------------------------------------------------------------------------------------------------------------------------------------
int main() {
	int shmid, semid, i, semStato;
	int *tavoli;
	key_t keyshm=1234, keysem=5678;

	//CREO LA MEMORIA CONDIVISA (4 celle di interi --> 1 per la sincronizzazione 3 per i tavoli) E 3 SEMAFORI
	shmid = shmget(keyshm, sizeof(int)*4 , 0666 | IPC_CREAT); 
	semid = semget(keysem, 3, 0666 | IPC_CREAT);         
  //controllo eventuale errore
	if (shmid == -1 || semid == -1) {
		printf("Errore nella gestione della memoria o dei semafori");
		exit(-1);
	}
	
	//AGGANCIO ALLA MEMORUA
	tavoli = (int *) shmat(shmid, NULL,0);

	//SETTAGGIO INIZIALE DEI SEMAFORI
	for (i=0; i<3 ;i++) {
		semStato = semctl(semid, i, SETVAL, 4);
	}
	
	//SETTAGGIO INIZIALE DEI TAVOLI
	for (i=0;i<4;i++){
		tavoli[i] = 0;
	}
	
	//APRO LA MENSA
	printf("LA MENSA È APERTA!\nÈ adesso possibile avviare il file commensali\n");
	tavoli[3] = 1;
	printf("\n");
	printf(" ___________________________________ \n");
	printf("|                                   |\n");
	printf("|               MENÙ                |\n");
	printf("|___________________________________|\n");
	printf("|                                   |\n");
	printf("|  ·0 - CARNE                       |\n");
	printf("|  ·1 - PESCE                       |\n");
	printf("|  ·3 - VEGETARIANO                 |\n");
	printf("|___________________________________|\n");
	
	//RICEVO I COMMENSALI
	while(tavoli[3 ]!= 0){
		printf("Ricevendo i commensali...\n");
		sleep(3);
	}
	
	//FINITO DI RICEVERE I COMMENSALI --> STAMPO IL RESOCONTO
	printf("\n");
	printf(" ___________________________________ \n");
	printf("|                                   |\n");
	printf("|       RESOCONTO GIORNALIERO       |\n");
	printf("|___________________________________|\n");
	printf("Menù di pesce: %d commensali\n", tavoli[0]);
	printf("Menù di carne: %d commensali\n", tavoli[1]);
	printf("Menù vegeteariano: %d commensali\n", tavoli[2]);
	
	//DISTRUGGO LE MEMORIA CONDIVSA E I 3 SEMAFORI
	shmctl(shmid, IPC_RMID, NULL);
	for(i=0; i<3; i++){
		semctl(semid, i, IPC_RMID, 0);
	}
	
return 0;
}
