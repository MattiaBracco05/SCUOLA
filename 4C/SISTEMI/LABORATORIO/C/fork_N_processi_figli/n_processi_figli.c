/*
Bracco Mattia 4C - N processi figli
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
	
	int figli, i, num, stato_wait;
	pid_t chiSono, pid;
	
	printf("Inserisci un numero: ");
	scanf("%d", &num);
	printf("Quanti figli vuoi generare?: ");
	scanf("%d", &figli);
	
	//ciclo per gli N figli...
	for (i=0; i<figli; i++) {
		//se < 0 --> errore
		if ((chiSono = fork()) < 0) {
			printf("Errore nella creazione della fork()!\n");
			exit(-1);
		}
		//se = 0 --> figlio
		if (chiSono == 0) {
			srand(getpid()); //"srand" con "getpid()" in modo che il seme sia sempre diverso (con "time(NULL)" avrebbero tutti lo stesso seme"
			num = num + rand()%21;
			printf("Processo figlio (PID: %d), numero: %d\n", getpid(), num);
			exit(num);
		}
	}
	
	//----processo padre----
	
	//ciclo per gli N figli...
	for (i=0; i<figli; i++) {
		pid = wait(&stato_wait);
		printf("Processo figlio (PID: %d) terminato!\n", pid);
	}
	printf("Tutti i processi figli sono stati chiusi!\n");
	printf("Processo padre (PID: %d), numero alla fine del programma: %d\n", getpid(), num);
		
return 0;
}
