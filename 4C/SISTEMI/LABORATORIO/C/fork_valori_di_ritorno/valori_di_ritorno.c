//Bracco Mattia 4C - Eseguire una fork e stampare il PID del processo padre e del processo figlio

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> //(libreria per la gestione dei processi)

int main() {

	pid_t chiSono; //variabile di tipo "pid_t"
	chiSono = fork();

	//se chiSono < 0 --> ERRORE! --> printf e forzo la chiusra del programma con "exit(-1)"
	if (chiSono < 0) {
		printf("ERRORE DURANTE LA CREAZIONE DELLA FORK!\n");	
		exit(-1);
	}

	//se chiSono == 0 --> processo figlio
	if (chiSono == 0) {
		//qui ci sarà il codice del processo figlio...
		printf("Sono il processo figlio, il mio PID è: %d, il PID del processo padre è: %d\n", getpid(), getppid());	
	}

	//altriemnti (chiSono > 0) --> processo padre
	else {
		//qui ci sarà il codice del processo padre...
		printf("Sono il processo padre, il mio PID è: %d, il PID del mio processo padre (shell) è: %d\n", getpid(), getppid());	
	}

return 0;
}
