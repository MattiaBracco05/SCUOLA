/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI (vanno sempre prima del main, servono per far riconoscere (prima del main) al compilatore ed evitare errori)
void sommaNumeri();
int moltiplica();

int main() {

	int risultato;
	srand(time(NULL));

	printf("Richiamo la prima volta la procedura \n");
	sommaNumeri();
	printf("Richiamo di nuovo la procedura \n");
	sommaNumeri();
	
	printf("Richiamo la funzione \n");
	risultato = moltiplica();
	printf("Il prodotto vale %d\n", risultato);
	
return 0;
}

//PROCEDURA
void sommaNumeri() { //void (vuota) perchè non restituisce nulla al main

	//queste variabili nascono e muoiono nella procedura
	int num, somma=0, i;

	for(i=0; i<10; i++) {
		num=rand()%146+5;
		printf("%d\t", num);
		somma = somma + num;
	}
	printf("La somma vale %d\n", somma);
}

//FUNZIONE
int moltiplica() { //int perchè restitusisce un intero al main
	
	//queste variabili nascono e muoiono nella funzione
	int num, prodotto=1, i;

	for(i=0; i<3; i++) {
		num=rand()%10+2;
		printf("%d\t", num);
		prodotto = prodotto * num;
	}
	
return prodotto;
}

