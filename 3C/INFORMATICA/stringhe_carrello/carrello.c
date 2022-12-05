/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXRIGHE 20
#define MAX 150

//PROTOTIPI
void inserisciProdotti(char[][MAX+1], float[], int*);
void prezzoMaggiore(char[][MAX+1], float[], int);
void primoProdotto(char[][MAX+1], float[], int);
void cercaLunghezza(char[][MAX+1], int);
void stampaLunghezze(char[][MAX+1], int);

int main() {
	int N, dim;
	float prezzi[MAXRIGHE];
	char prodotti[MAXRIGHE][MAX+1];

	system("clear");
	inserisciProdotti(prodotti, prezzi, &N);
	prezzoMaggiore(prodotti, prezzi, N);
	cercaLunghezza(prodotti, N);
	stampaLunghezze(prodotti, N);

	dim = sizeof(prodotti)/sizeof(prodotti[0]);
	primoProdotto(prodotti, prezzi, dim);

return 0;
}
//------------------------------------------------------------------------------------------------------------------------------------
void inserisciProdotti(char prod[][MAX+1], float prezzi[], int *N) {
	int i=0, exit=0;
	float prz;
	char temp[MAX+1];
	while(exit == 0 && i<MAXRIGHE) {
		//NOME PRODOTTO
		printf("Inserisci il nome del prodotto n.%d (MAX %d caratteri): ", i+1, MAX);
		gets(temp);
		while(strlen(temp) == 0 || strlen(temp) > MAX) {
			printf("ERRORE! Prodotto non inserito o con lunghezza fuori range!\n");
			printf("Inserisci il nome del prodotto n.%d (MAX %d caratteri): ", i+1, MAX);
			gets(temp);			
		}
		strcpy(prod[i], temp);
		//CONTROLLO USCITA
		if( (strcmp(temp, "VUOTO") == 0) ||(strcmp(temp, "vuoto") == 0) || (strcmp(temp, "Vuoto") == 0) ) {
			system("clear");
			printf("Termino l'inserimento dei prodotti!\n");			
			exit = 1;
		} else {
			//PREZZO PRODOTTO
			printf("Inserisci il prezzo del prodotto %s: ", temp);
			scanf("%f", &prz);
			while(prz <= 0) {
				printf("ERRORE! Il prezzo non può essere negativo o pari a 0!\n");
				printf("Inserisci il prezzo del prodotto %s: ", temp);
				scanf("%f", &prz);
			}
			while(getchar() != '\n');		
			prezzi[i] = prz;
			i++;
		}	
	}
	(*N) = i;
}
//------------------------------------------------------------------------------------------------------------------------------------
void prezzoMaggiore(char prod[][MAX+1], float prez[], int N) {
	int i;
	float max=0;
	char nome[MAX+1];

	for(i=0; i<N; i++) {
		if(prez[i] > max) {
			max = prez[i];
			strcpy(nome, prod[i]);
		}
	}
	printf("Il prodotto con il prezzo maggiore è: %s e costa: %.2f€\n", nome, max);
}
//------------------------------------------------------------------------------------------------------------------------------------
void cercaLunghezza(char prod[][MAX+1], int N) {
	int i, l=6;
	printf("Stampo i nomi dei prodotti con lunghezza pari a %d...\n", l);
	for(i=0; i<N; i++) {
		if(strlen(prod[i]) == l) {
			printf("%s\n", prod[i]);
		}	
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void stampaLunghezze(char prod[][MAX+1], int N) {
	int i, lung;
	for(i=0; i<N; i++) {
		lung = strlen(prod[i]);
		printf("Il nome del prodotto n.%d è lungo: %d\n", i+1, lung);
	}
}//------------------------------------------------------------------------------------------------------------------------------------
void primoProdotto(char prod[][MAX+1], float prez[], int N) {
	int i, j;
	float tmp;	
	char TMP[MAX+1];
	for (i=0; i<N-1; i++) {
		for (j=0; j<N-1-i; j++) {
			if (strcmp(prod[j], prod[j+1]) > 0) {
				strcpy(TMP, prod[j]);
				strcpy(prod[j], prod[j+1]);
				strcpy(prod[j+1], TMP);
				//scambio anche i prezzo
				tmp = prez[j];
				prez[j] = prez[j+1];
				prez[j+1] = tmp;
			}
		}
	}
	printf("Il primo prodotto in ordine alfabetico è: %s e costa: %.2f€\n", prod[0], prez[0]);
}
