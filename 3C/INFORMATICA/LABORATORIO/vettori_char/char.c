/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 15

//PROTOTIPI
void caricaVettore(char[], char[], int *);
void stampaVettore(char[], int);

int main() {
	char nome[MAX], max[MAX];
	int dim=0;
	
	caricaVettore(nome, max, &dim);
	stampaVettore(max, dim);


return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------
void caricaVettore(char nome [], char max [], int *dim) {
	int N, i, j;
	char ch;
	for(i=0; i<10; i++) {
		//prima di ogni ciclo
		N=0;
		printf("Inserisci il %d nome: ", i+1);
		//prendo in input il nome
		ch = getchar();
		while(ch!='\n' && N<MAX) {
			nome[N] = ch;
			N++;
			ch = getchar();
		}
		//controllo lunghezza
		if(N > (*dim)) {
			(*dim) = N;
			for(j=0; j<N; j++) {
				max[j] = nome[j];
			}
		}	
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void stampaVettore(char vett[], int dim) {
	int i;
	printf("Il nome più lungo è composto da %d lettere\n", dim);
	printf("Nome: ");
	for(i=0; i<dim; i++) {
		printf("%c", vett[i]);
	}
	printf("\n");
}
