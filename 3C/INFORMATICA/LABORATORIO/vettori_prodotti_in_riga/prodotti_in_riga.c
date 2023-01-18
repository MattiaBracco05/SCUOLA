/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 101

//PROTOTIPI
void caricaVettore(char [], int *);
void numeroProdotti(char [], int *, int );
void primoProdotto(char [], char [], int, int, char []);
void lungoProdotto(char [], char [], int, int, int *, char []);
int uguali(char [], char []);

int main() {

	int lunghezza=0, numero=1, valLungo=0, lPrimo=0, lungh, coin;
	char prodotti[MAX], temporaneo[MAX], primo[MAX], prodottoLungo[MAX];

	system("clear");
	caricaVettore(prodotti, &lunghezza);
	numeroProdotti(prodotti, &numero, lunghezza);
	printf("Ci sono %d prodotti\n", numero);

	//primo prodotto in ordine alfabetico
	primoProdotto(prodotti, temporaneo, lunghezza, numero, primo);
	lPrimo = strlen(primo);
	printf("Il primo prodotto in ordine alfabetico è: %s ed è lungo %d caratteri\n", primo, lPrimo);

	//prodotto più lungo
	lungoProdotto(prodotti, temporaneo, lunghezza, numero, &lungh, prodottoLungo);
	printf("Il prodotto più lungo è: %s ed è lungo %d caratteri\n", prodottoLungo, lungh);
	
	//controllo uguali
	coin = uguali(primo, prodottoLungo);
	if(coin == 0) {
		printf("Le 2 stringhe coincidono!\n");
	}
	else {
		printf("Le 2 stringhe NON coincidono!\n");
	}

return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void caricaVettore(char vett[], int *l) {
    printf("Inserisci i prodotti separandoli con uno spazio: ");
    gets(vett);
    *l=strlen(vett);
}
//-----------------------------------------------------------------------------------------------------------------------------------
void numeroProdotti(char vett[], int *N, int l) {
	int i=0;
	for(i=0;i<l;i++) {
		if(vett[i] == ' ') {
    	*N=*N+1;
		}
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void primoProdotto(char vett[], char temp[], int l, int num, char primo[]){
	int i=0, n=0, j=0, ris=0;
	for(i=0; i<20; i++) {
		primo[i]='z';
	}
	primo[i]=0;
	for(i=0; i<num; i++) {
		j=0;
		while(vett[n] != ' ' && n<l) {
			temp[j] = vett[n];
			n++;
			j++;
		}
		temp[j]=0;
		ris = strcmp(primo,temp);
    if(ris > 0) {
			strcpy(primo,temp);
    }
    n++;
   }
}
//-----------------------------------------------------------------------------------------------------------------------------------
void lungoProdotto(char prod[], char temp[], int l, int num, int *lungh, char m[]){
	int i=0, n=0, j=0, ris=0;
	*lungh=0;
	for(i=0; i<num; i++) {
		j=0;
		while(prod[n] != ' ' && n<l) {
			temp[j] = prod[n];
			n++;
			j++;
		}
		temp[j]=0;
		if(strlen(temp) > *lungh) {
			*lungh = strlen(temp);
			strcpy(m,temp);
		}
		n++;
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
int uguali(char pri[], char lungh[]){
	return strcmp(pri,lungh);
}
