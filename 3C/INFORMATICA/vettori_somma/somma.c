/*
Bracco Mattia 3C
*/

//AREA DEI PROTOTIPI
int creaRandom();

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main() {
	srand(time(NULL));
	int numeri[60], N=0, i, tot=0;
	
	while(N < 1 || N > 60) {
		printf("Quanti numeri vuoi che il random generi ? (max 60): ");
		scanf("%d",&N);
	}
	
	for (i=0; i<N; i++) {
		numeri[i] = creaRandom();
		printf("%d | ", numeri[i]);
		tot = tot + numeri[i];
	}
	
	printf("\nLa somma vale: %d\n", tot);
}

//-----------------------------------------------------------------------------------------------------------------------------------
int creaRandom() {
	int numero;
	numero = rand()%(117-23+1)+23;
return numero;
}
