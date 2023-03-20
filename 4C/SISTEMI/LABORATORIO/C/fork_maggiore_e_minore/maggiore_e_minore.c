/*
Bracco Mattia 4C - Numero maggiore e numero minore generato random dai processi figli
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#define MIN 1
#define MAX 5

//PROTOTIPI
int chiediN();

int main() {
	
	int figli, i, num, stato_wait, min=7, max=29, maggiore=0, minore=30;
	pid_t chiSono, pid, pid_maggiore, pid_minore;
	
	figli = chiediN();
	
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
			num = num + rand()%((max-min+1)+min);
			printf("Processo figlio (PID: %d), numero random: %d\n", getpid(), num);
			exit(num);
		}
	}
	
	//ciclo per gli N figli...
	for (i=0; i<figli; i++) {
		pid = wait(&stato_wait);
		//controllo se maggiore dei precedenti --> se si sovrascrivi il maggiore
		if ((stato_wait >> 8) > maggiore) {
			maggiore = (stato_wait >> 8);
			pid_maggiore = pid;
		}
		if ((stato_wait >> 8) < minore) {
			minore = (stato_wait >> 8);
			pid_minore = pid;
		}
	}
	printf("Il processo (PID: %d) ha generato il numero maggiore (%d)\n", pid_maggiore, maggiore);
	printf("Il processo (PID %d) ha generato il numero minore (%d)\n", pid_minore, minore);

return 0;
}

//------------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val=0;
	while (val < MIN || val > MAX) {
		printf("Quanti figli vuoi generare? (%d-%d): ", MIN, MAX);
		scanf("%d", &val);
	}
return val;
}
