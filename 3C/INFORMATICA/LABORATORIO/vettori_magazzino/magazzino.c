/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI---------------------------------------------------------------------------------------------------------------------------
int creaRandom(int, int);
int Narticoli(int, int);
void caricaArticoli(int, int [], int []);
void resocontoMagazzino(int, int [], int []);
void massimoVenduti(int, int [], int []);
void calcolaPercentuale(int, int [], int []);
//------------------------------------------------------------------------------------------------------------------------------------
int main() {
	int quanti[20], venduti[20];
	int N=0;
	srand(time(NULL));
	
	N=Narticoli(4,20);
	caricaArticoli(N, quanti, venduti);
	resocontoMagazzino(N, quanti, venduti);
	massimoVenduti(N, quanti, venduti);
	calcolaPercentuale(N, quanti, venduti);
return 0;
}
//------------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	int num;
	num = rand()%(max-min+1)+min;
return num;
}
//------------------------------------------------------------------------------------------------------------------------------------
int Narticoli(int min, int max) {
	int art=0;
	while (art < min || art > max) {
		printf("Quanti articoli vuoi nel magazzino ? (%d-%d): ", min, max);
		scanf("%d", &art);
	}
return art;
}
//------------------------------------------------------------------------------------------------------------------------------------
void caricaArticoli(int N, int quanti [], int venduti []) {
	int i, range;
	for (i=0; i<N; i++) {
		quanti[i] = creaRandom(35,247);
		range = quanti[i] - 10;
		venduti[i] = creaRandom(1,range);
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void resocontoMagazzino(int N, int quanti [], int venduti []) {
	int i;
	for (i=0; i<N; i++) {
		printf("\e[1;94m--ARTICOLO %d--\n\e[0m", i+1);
		printf("Pezzi nel magazzino: %d\n", quanti[i]);
		printf("Pezzi venduti: %d\n", venduti[i]);
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void massimoVenduti(int N, int quanti [], int venduti []) {
	int max=0, art=0, totV=0, tot=0, totR=0, i;
	for (i=0; i<N; i++) {
		tot = tot + quanti[i]; //sommo il totale
		totV = totV + venduti[i]; //sommo il totale dei venduti
		if (venduti[i] > max) {
			max = venduti[i];
			art = i;
		}
	}
	totR = tot - totV;
	printf("\e[0;92mIn totale sono stati venduti %d pezzi (nel magazzino ne rimangono %d).\n", totV, totR);
	printf("L' articolo più venduto ha registrato %d pezzi venduti, ed è l' articolo n. %d\n\e[0m", max, art+1);
}
//------------------------------------------------------------------------------------------------------------------------------------
void calcolaPercentuale(int N, int quanti [], int venduti []) {
	int i, rim=0;
	float perc=0;
	for (i=0; i<N; i++) {
		rim = quanti[i] - venduti[i];
		perc = (float)(rim *100) / quanti[i];
		printf("\e[1;94mARTICOLO %d|\e[0m  perc. pezzi rimanenti: %.2f %% \n", i+1, perc);
	} 
}
