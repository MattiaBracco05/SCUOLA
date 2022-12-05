/*
Bracco Mattia 3C
*/

//AREA DEI PROTOTIPI
int creaRandom(int, int);
int dimensioneVettore(int, int);
void caricaVettore(int, int []);
void stampaVettore(int, int []);

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(NULL));
	int dimensione, numeri[30];

	dimensione=dimensioneVettore(4,25);
	caricaVettore(dimensione, numeri);
	stampaVettore(dimensione, numeri);
	
return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	int numero;
	numero = rand()%(max-min+1)+min;
return numero;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int dimensioneVettore(int min, int max) {
	int dim=0;
	while(dim<min || dim>max) {
		printf("Inserisci la dimensione del vettore (%d-%d): ", min, max);
		scanf("%d", &dim);
	}
return dim;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void caricaVettore(int dim, int vett[]) {
	int i;
	for(i=0; i<dim; i++) {
		vett[i]=creaRandom(0,11);
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void stampaVettore(int dim, int vett[]) {
	int i;
	for(i=0; i<dim; i++) {
		printf("%d\t", vett[i]);
	}
	printf("\n");
}
