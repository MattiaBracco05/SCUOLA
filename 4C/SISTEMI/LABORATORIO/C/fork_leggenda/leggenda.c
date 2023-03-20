/*
Bracco Mattia 4C - Leggenda
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/wait.h>
#define MIN 1
#define MAX 5

//PROTOTIPI
int chiediN();

int main() {
	
	int figli, i, num, stato_wait, min=1977, max=1986;
	int caduti[5];
	pid_t chiSono, pid;
	FILE * fp;
	
	figli = chiediN();
	
	//scrivo sul file
	fp = fopen("./leggenda.txt", "w");
	fprintf(fp, "Narra la leggenda che un padre di nome %d creò %d figli, li affidò al loro destino ed insieme scrissero la Storia. Questa Storia racconta di leggende epiche, duri scontri, ardue battaglie,alcune sconfitte e molte vittorie\n", getpid(), figli);   
	fclose(fp);

	//ciclo per gli N figli...
	for (i=0; i<figli; i++) {
		//se < 0 --> errore
		if ((chiSono = fork()) < 0) {
			printf("Errore nella creazione della fork()!\n");
			exit(-1);
		}
		//se = 0 --> figlio
		if (chiSono == 0) {
			srand(getpid());
			num = rand()%(max-min+1)+min;
			printf("Processo figlio (PID: %d), numero generato: %d\n", getpid(), num);
			
			//se il processo figlio ha vinto -->
			if((num%2) == 0) {
				printf("Ho vinto!\n");
				
				//scrivo sul file
				fp = fopen("./leggenda.txt", "a");
				fprintf(fp, "Io %d figlio di %d eroico cavaliere, dopo aver affrontato tremende battaglie, posso dire di aver vinto la mia guerra con il numero %d\n", getpid(), getppid(), num);   
				fclose(fp);
				exit(0);
			}
			
			//se il processo figlio ha perso -->
			else {
				printf("Ho perso!\n");
				exit(1);
			}
		}
	}
	
	//ciclo per gli N figli (per chiuderli)
	for (i=0; i<figli; i++) {
		pid = wait(&stato_wait);
		if (stato_wait == 1) {
			caduti[i] = pid;
		}
	}
	//scrivo sul file
	fp = fopen("./leggenda.txt", "a");
	fprintf(fp, "Figli miei %d avete lottato tutti con grande coraggio e mi avete resoorgoglioso di voi. Siete caduti, ma il vostro nome rimarrà per sempre inciso nella Storia.", caduti);   
	fclose(fp);

return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val=0;
	while (val < MIN || val > MAX) {
		printf("Quanti figli vuoi generare? (%d-%d): ", MIN, MAX);
		scanf("%d", &val);
	}
return val;
}
