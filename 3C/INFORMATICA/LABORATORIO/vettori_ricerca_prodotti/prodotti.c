/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 20

//AREA DEI PROTOTIPI
void caricaVettore(int [], float[], int *);
void stampaVettore(int, int[], float[]);
void ordinaPrezzo(int, int[], float[]);
int ricercaDicotomica(float, int, float[]);

int main() {
	int numero[MAX], N, posizione;
	float prezzo[MAX], valore;	

	system("clear");
	caricaVettore(numero, prezzo, &N);
	system("clear");
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                               NON ORDINATI                             |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	stampaVettore(N, numero, prezzo);
	ordinaPrezzo(N, numero, prezzo);
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                      ORDINATI IN BASE AL PREZZO                        |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	stampaVettore(N, numero, prezzo);
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                                 RICERCA                                |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	printf("Inserisci un prezzo da cercare €: ");
	scanf("%f",&valore);
	posizione = ricercaDicotomica(valore, N, prezzo);
	if(posizione == -1) {
		printf("Non esistono prodotti con questo prezzo (%.2f€)\n", valore);	
	}
	else {
		printf("Il prodotto n.%d ha il prezzo cercato (%.2f€)\n", numero[posizione], valore);	
	}

return 0;
}
//------------------------------------------------------------------------------------------------------------------------------------
void caricaVettore(int num[], float prez[], int *N) {
	int exit=0, totP=0;
	while((exit == 0) && (totP < 20)) {
		num[totP] = totP+1;
		printf("Inserire il prezzo del prodotto n.%d oppure 0 per terminare: ", num[totP]);
		scanf("%f", &prez[totP]);
		if(prez[totP] == 0) {
			exit = 1;		
		}
		else {
			totP++;
		}
	}
	*N = totP;
}
//------------------------------------------------------------------------------------------------------------------------------------
void stampaVettore(int N, int num[], float prez[]) {
	int i;	
	for(i=0; i<N; i++) {
		printf("Prodotto n.%d | Costo: %.2f€\n", num[i], prez[i]);	
	}
}
//-------------------------------------------------------------------------------------------------------------------------------------
void ordinaPrezzo(int N, int num[], float prez[]) {
	int j, i, flag, TMP;
	j = N;
	flag = 1; //1 => TRUE, 0 => FALSE
	while(flag == 1) {
		flag = 0;	
		for(i=0; i<j-1; i++) {
			if(prez[i] > prez[i+1])	{
				TMP = prez[i];
				prez[i] = prez[i+1];
				prez[i+1] = TMP;
				TMP = num[i];
				num[i] = num[i+1];
				num[i+1] = TMP;
				flag = 1;		
			}	
		}
		j--;	
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
int ricercaDicotomica(float val, int N, float prez[]) {
	int i=0, j=N-1, trovato=-1, pos;

	printf("Cerco il prezzo %.2f...\n", val);
	
	while((i<=j) && (trovato==-1)) {
		pos = (i+j) / 2;
		if(prez[pos] == val) {
			trovato = pos;
		}
		else {
			if(prez[pos] > val) {
				j = pos - 1;
			}
			else {
				i = pos + 1;
			}
		}
	}
return trovato;
}
