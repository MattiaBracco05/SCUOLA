/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI (vanno sempre prima del main, servono per far riconoscere (prima del main) al compilatore ed evitare errori)
float calcolaMedia();

int main() {
	
	float media;
	srand(time(NULL));

	printf("Richiamo la funzione \n");
	media=calcolaMedia();
	printf("La media vale: %.2f\n", media);
	
return 0;
}

//funzione di tipo float per il calcolo della media
float calcolaMedia() {

	int num, somma=0, i;
	float risultato=0.0;

	for(i=0; i<10; i++) {
		num=rand()%10+1;
		printf("%d\t", num);
		somma = somma + num;
	}
	risultato = (float) somma / 10;

return risultato;
}



