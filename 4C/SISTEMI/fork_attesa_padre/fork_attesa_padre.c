/*
Bracco Mattia 4C - Attesa del processo padre
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h> //Libreria che permette di gestire l'attesa del processo padre

int main() {

	int num = 42, stato_wait;
	pid_t chiSono, pid;
	printf("Il numero iniziale è: %d\n", num);
	
	//se < 0 --> errore
	if ((chiSono = fork()) < 0) {
		printf("Errore nella creazione della fork()!\n");
		exit(-1); //exit con valore negativo per uscire in caso di errore
	}
	
	//se = 0 --> p. figlio
	if (chiSono == 0) {
		num = num * 3;
		printf("Processo figlio (PID: %d), numero modificato: %d\n", getpid(), num);
		exit(1); //exit con valore qualsiasi --> chiudo il p. figlio
	}
	
	//Da qua in poi sono dentro al p. padre...
	
	pid = wait(&stato_wait);
	/*
	&stato_wait: puntatore della fork()
	pid: valore di ritorno della exit (PID del p. figlio appena terminato)
	*/
	printf("Processo padre (PID: %d), processo figlio (PID: %d) terminato!\n", getpid(), pid);
	printf("Valore numero alla fine del programma: %d\n", num);
		
return 0;
}
