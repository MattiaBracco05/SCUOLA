/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 5

//PROTOTIPI
int creaRandom(int, int);
void caricaVettori(int[], int[], char[]);
void numeroCamere(int[]);
void numeroGiorni(int[]);
void tipologiaCamere(int[], char[]);
void stampaVettori(int[], int[], char[]);
void mediaGiorni(int[]);
void totaleGiorni(int[]);
void presenzeMassime(int[], int[]);
void limite(int[], int[], char[]);


int main() {
	int camere[MAX], giorni[MAX];
	char tipologia[MAX];
	srand(time(NULL));
	system("clear");
	
	caricaVettori(camere, giorni, tipologia);
	stampaVettori(camere, giorni, tipologia);
	mediaGiorni(giorni);
	totaleGiorni(giorni);
	presenzeMassime(camere, giorni);
	limite(camere, giorni, tipologia);
	
return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
return rand()%(max-min+1)+min;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void caricaVettori(int c[], int g[], char t[]) {
	numeroCamere(c);
	numeroGiorni(g);
	tipologiaCamere(c,t);
}
//-----------------------------------------------------------------------------------------------------------------------------------
void numeroCamere(int vett[]) {
	int i;
	for(i=0; i<MAX; i++) {
		vett[i] = i + 1;
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void numeroGiorni(int vett[]) {
	int i;
	for (i=0; i<MAX; i++) {
		vett[i] = creaRandom(1,21);
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void tipologiaCamere(int num[], char vett[]) {
	int i, exit;
	char scelta;
	for(i=0; i<MAX; i++){
		exit=0;
		system("clear");
		while(exit == 0) {
				printf("\e[0;94m");
			  printf(" ________________________________________________________________________\n");
        printf("|                           CAMERE DISPONIBILI                           |\n");
        printf("|________________________________________________________________________|\n");
        printf("| S - Camera Singola                                                     |\n");
        printf("| M - Camera Matrimoniale                                                |\n");
        printf("| T - Camera Tripla                                                      |\n");
        printf("| Q - Camera Quadrupla                                                   |\n");
        printf("|________________________________________________________________________|\n");
        printf("\e[0m");
        printf("Inserire tipologia camera n.%d: ", num[i]);
        scanf("%c", &scelta);
        while(getchar()!='\n');
        switch(scelta){
						case 'S':
						case 'M':
						case 'T':
						case 'Q':
							exit = 1;
            	break;
            default:
            	printf("\e[1;91mOperatore non valido!, ricordati che la lettera deve essere MAIUSCOLA\e[0m\n");        
				}
		vett[i] = scelta;		
		}
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void stampaVettori(int c[], int g[], char t[]) {
	int i;
	system("clear");
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                                DATI CAMERE                             |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	for(i=0; i<MAX; i++)	{
		printf("Camera: %d | Tipo: %c | Giorni: %d\n", c[i], t[i], g[i]);
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void mediaGiorni(int vett[]) {
	int i, tot=0;
	float media;
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                               STATISTICHE                              |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	for(i=0; i<MAX; i++) {
		tot = tot + vett[i];
	}
	media = (float) tot / MAX;
	printf("La media dei giorni è: %.2f\n", media);
}
//-----------------------------------------------------------------------------------------------------------------------------------
void totaleGiorni(int vett[]) {
	int i, tot=0;
	for(i=0; i<MAX; i=i+2) {
		tot = tot + vett[i];
	}
	printf("Il totale dei giorni della camere dispari è: %d\n", tot);
}
//-----------------------------------------------------------------------------------------------------------------------------------
void presenzeMassime(int c[], int g[]) {
	int i, max=0, pos;
	for(i=0; i<MAX; i++) {
		if(g[i] > max) {
			max = g[i];
			pos = c[i];
		}
	}
	printf("La camera con il maggior numero di giorni (%d) è la n.%d\n", max, pos);
}
//-----------------------------------------------------------------------------------------------------------------------------------
void limite(int c[], int g[], char t[]) {
	int i, lim, flag=0;
	lim = creaRandom(1,21);
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                             RICERCA LIMITE                             |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	printf("Cerco camere con un numero di giorni maggiore di %d...\n", lim);
	for(i=0; i<MAX; i++) {
		if(g[i] > lim) {
			printf("Camera: %d | Tipologia: %c | Giorni: %d\n", c[i], t[i], g[i]);
			flag++;
		}
	}
	if(flag == 0) {
		printf("\e[1;91mNon sono state trovate camere con un numero di giorni superiore al limite (%d)!\e[0m\n", lim);
	}
}
