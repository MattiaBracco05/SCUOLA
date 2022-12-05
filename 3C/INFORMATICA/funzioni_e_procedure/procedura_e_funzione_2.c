/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI (vanno sempre prima del main, servono per far riconoscere (prima del main) al compilatore ed evitare errori)
int chiediNumero();

int main() {

	int uno, due, tre, somma=0;

	uno = chiediNumero();
	due = chiediNumero();
	tre = chiediNumero();
	
	somma = uno + due + tre;
	printf("La somma vale: %d\n", somma);

return 0;
}

//creo una funzione che chieda all' utente un numero
int chiediNumero(){

	int num;
	
	printf("Inserisci un numero: ");
	scanf("%d", &num);

return num;
}
