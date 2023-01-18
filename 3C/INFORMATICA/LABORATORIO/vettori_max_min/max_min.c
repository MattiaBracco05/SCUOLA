/*
Bracco Mattia 3C
*/

//AREA DEI PROTOTIPI
int creaRandom(int, int);

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(NULL));
	int numeri[50], N=0, i, posMax, posMin, max=26, min=113, ripMax=0, ripMin=0;
	while(N<4 || N>50) {
		printf("Quanti numeri vuoi caricare nel vettore ? (4-50): ");
		scanf("%d", &N);
	}
	for(i=0; i<N; i++) {
		numeri[i] = creaRandom(27,112);
		printf("%d\t", numeri[i]);
		//controllo se è uguale al precedente max
		if(numeri[i] == max) {
			ripMax++;
		}
		//controllo se è uguale al precedente min
		if(numeri[i] == min) {
			ripMin++;
		}
		//controllo maggiore
		if(numeri[i] > max) {
			max = numeri[i];
			posMax = i;
			ripMax = 0;
		}
		//controllo minore
		if(numeri[i] < min) {
			min = numeri[i];
			posMin = i;
			ripMin = 0;
		}
	}
	printf("\n");
	printf("Il numero max è: %d, si trova nella posizione %d e si ripete altre %d volte\n", max, posMax, ripMax);
	printf("Il numero min é: %d, si trova nella posizione %d e si ripete altre %d volte\n", min, posMin, ripMin);
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	int numero;
	numero = rand()%(max-min+1)+min;
return numero;
}
