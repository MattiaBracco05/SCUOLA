//Bracco Mattia 4C - Dato un numero processo padre e figlio lo modificano e lo stampano

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> //(libreria per la gestione dei processi)

int main() {
	
	pid_t chiSono;
	int num = 42;
	printf("Numero iniziale: %d\n", num);
	
	//chiSono < 0 --> ERRORE!
	if ((chiSono = fork()) < 0) {
		printf("ERRORE durante la creazione della fork()!\n");	
		exit(-1);	
	}

	//chiSono == 0 --> processo figlio
	if (chiSono == 0) {
		num = 8;
		printf("Sono il processo figlio (PID: %d), il numero modificato è %d\n", getpid(), num);
	}

	//chiSono > 0 --> processo padre
	else {
		num = num * 5;
		printf("Sono il processo padre (PID: %d), il numero modificato è %d\n", getpid(), num);
	}

	printf("----Numero alla fine del programma: %d----\n", num);

return 0;
}
