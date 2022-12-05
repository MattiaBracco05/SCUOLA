/*
Bracco Mattia 3C
*/

//AREA DEI PROTOTIPI
int creaRandom(int, int);
int dimensioneVettore(int, int);
void caricaVettore(int, int []);
void stampaVettore(int, int []);
void maxVettore(int, int []);
void minVettore(int, int []);

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(NULL));
	int numeri[51], dimensione;
	
	dimensione=dimensioneVettore(4,50);
	caricaVettore(dimensione, numeri);
	stampaVettore(dimensione, numeri);
	
	maxVettore(dimensione, numeri);
	minVettore(dimensione, numeri);
	
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
		vett[i]=creaRandom(27,112);
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
//-----------------------------------------------------------------------------------------------------------------------------------
void maxVettore(int dim, int vett[]) {
	int max=26, posMax, ripMax, i;
	for(i=0; i<dim; i++) {
		if(vett[i] == max) {
			ripMax++;
		}
		if(vett[i] > max) {
			max = vett[i]; posMax = i; ripMax = 0;
		}
	}
	printf("Il numero max è: %d, si trova nella posizione %d e si ripete altre %d volte\n", max, posMax, ripMax);
}
//-----------------------------------------------------------------------------------------------------------------------------------
void minVettore(int dim, int vett[]) {
	int min=113, posMin, ripMin=0, i;
	for(i=0; i<dim; i++) {
		if(vett[i] == min) {
			ripMin++;
		}
		if(vett[i] < min) {
			min = vett[i]; posMin = i; ripMin = 0;
		}
	}
	printf("Il numero min è: %d, si trova nella posizione %d e si ripete altre %d volte\n", min, posMin, ripMin);
}
