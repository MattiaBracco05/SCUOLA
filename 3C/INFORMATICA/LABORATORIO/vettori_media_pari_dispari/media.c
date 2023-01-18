/*
Bracco Mattia 3C
*/

//AREA DEI PROTOTIPI
int creaRandom(int, int);
void mediaPari(int, int);
void mediaDispari(int, int);

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(NULL));
	int numeri[130], N, i, sommaPari=0, sommaDispari=0, pari=0, dispari=0;
	
	N=creaRandom(1,130);
	printf("Vado a riempire %d (random) celle del vettore con numeri random (30-128)\n", N);
	for (i=0; i<N; i++) {
		numeri[i] = creaRandom(30,128);
		printf("%d |", numeri[i]);
		if (numeri[i]%2 == 0) {
			sommaPari = sommaPari + numeri[i];
			pari++;
		} else {
			sommaDispari = sommaDispari + numeri[i];
			dispari++;
		}
	}
	printf("\n");
	mediaPari(sommaPari, pari);
	mediaDispari(sommaDispari, dispari);
}

//-----------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	int numero;
	numero = rand()%(max-min+1)+min;
return numero;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void mediaPari(int somma, int n) {
	int media;
	media = somma / n;
	printf("La media dei numeri pari è: %d\n", media);
}
//-----------------------------------------------------------------------------------------------------------------------------------
void mediaDispari(int somma, int n) {
	int media;
	media = somma / n;
	printf("La media dei numeri dispari è: %d\n", media);
}
