/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 30

//PROTOTIPI
int creaRandom(int, int);
void caricaVettori(int[], int[], char[]);
void numeroCamere(int[]);
void numeroGiorni(int[]);
void tipologiaCamere(char[]);
void stampaVettori(int[], int[], char[]);
void mediaGiorni(int[]);
void totaleGiorni(int[]);
void presenzeMassime(int[]);
void limiteRandom(int[], int[], char[]);

int main() {
	int camere[MAX], giorni[MAX];
	char tipologia[MAX];
	srand(time(NULL));

	caricaVettori(camere, giorni, tipologia);
	stampaVettori(camere, giorni, tipologia);
	mediaGiorni(giorni);
	totaleGiorni(giorni);
	presenzeMassime(giorni);
	limiteRandom(camere, giorni, tipologia);

return 0;
}
//-------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	return rand()%(max-min+1)+min;
}
//-------------------------------------------------------------------------------------------------------------------------------
void caricaVettori(int camere[], int giorni[], char tipologia[]) {
	numeroCamere(camere); //numero le camere
	numeroGiorni(giorni); //creo i giorni (random)
	tipologiaCamere(tipologia); //chiedo di inserire la tipologia
}
//-------------------------------------------------------------------------------------------------------------------------------
void numeroCamere(int vett[]) {
	int i, N=MAX;
	for(i=0; i<N; i++) {
		vett[i] = i+1;
	}
}
//-------------------------------------------------------------------------------------------------------------------------------
void numeroGiorni(int vett[]) {
	int i, N=MAX;
	for(i=0; i<N; i++) {
		vett[i] = creaRandom(1,21);
	}
}
//-------------------------------------------------------------------------------------------------------------------------------
void tipologiaCamere(char vett[]) {
	int i, N=MAX, exit;
	char scelta;

	for(i=0; i<N; i++) {
		exit=0; //imposto exit a "0" ad ogni ciclo del for
		while(exit == 0) {
    	printf(" ________________________________________________________________________\n");
    	printf("|                         CAMERE DISPONIBILI                             |\n");
			printf("|________________________________________________________________________|\n");
			printf("| S - Camera singola                                                     |\n");
			printf("| M - Camera matrimoniale                                                |\n");
			printf("| T - Camera tripla                                                      |\n");
			printf("| Q - Camera quadrupla                                                   |\n");
			printf("|________________________________________________________________________|\n");
			printf("\n");
			printf("Inserire la tipologia della camera n. %d: ", i+1);
			scanf("%c", &scelta);
			while(getchar()!='\n');
			switch(scelta) {
				case 'S':
					exit = 1;
					break;
				case 'M':
					exit = 1;
					break;
				case 'T':
					exit = 1;	
					break;
				case 'Q':
					exit = 1;
					break;
				default:
					printf("Operatore non valido! Ricordati che la lettera deve essere MAIUSCOLA\n");	
			}
		}
		vett[i] = scelta;
	}
}
//-------------------------------------------------------------------------------------------------------------------------------
void stampaVettori(int camere[], int giorni[], char tipologia[]) {
	int i, N=MAX;
	printf(" ________________________________________________________________________\n");
	printf("|                           DATI DELLE CAMERE                            |\n");
	printf("|________________________________________________________________________|\n");
	for(i=0; i<N; i++) {
		printf("Camera: %d | Tipologia: %c | Giorni: %d\n", camere[i], tipologia[i], giorni[i]);	
	}
}
//-------------------------------------------------------------------------------------------------------------------------------
void mediaGiorni(int giorni[]) {
	int i, N=MAX, tot=0;
	float media=0;
	for(i=0; i<N; i++) {
		tot = tot + giorni[i];	
	}
	media = (float) tot / N;
	printf(" ________________________________________________________________________\n");
	printf("|                          STATISTICHE CAMERE                            |\n");
	printf("|________________________________________________________________________|\n");
	printf("La media dei giorni è: %.2f\n", media);
}
//-------------------------------------------------------------------------------------------------------------------------------
void totaleGiorni(int giorni[]) {
	int i, N=MAX, tot=0;
	for(i=0; i<N; i++) {
		tot = tot + giorni[i];	
		i++; //ho messo questo i++ perche se nel for scrivevo "i+2" non me lo stampava
	}
	printf("Il totale dei giorni delle camere dispari è: %d\n", tot);
}
//-------------------------------------------------------------------------------------------------------------------------------
void presenzeMassime(int giorni[]) {
	int i, N=MAX, max=0, pos;
	for(i=0; i<N; i++) {
		if(giorni[i] > max) {
			max = giorni[i];
			pos = i;
		}
	}
	printf("La camera con il maggior numero di giorni (%d) è la n. %d\n", max, pos);
}
//-------------------------------------------------------------------------------------------------------------------------------
void limiteRandom(int camere[], int giorni[], char tipologia[]) {
	int lim, i, N=MAX, flag=0;
	lim = creaRandom(1,21);
	printf(" ________________________________________________________________________\n");
	printf("|                              LIMITE RANDOM                             |\n");
	printf("|________________________________________________________________________|\n");
	printf("Camere con un numero di gionri maggiore di: %d\n", lim);
	for(i=0; i<N; i++) {
		if(giorni[i] > lim) {
			printf("Camera: %d | Tipologia: %c | Giorni: %d\n", camere[i], tipologia[i], giorni[i]);
			flag++;
		}	
	}
	if(flag == 0) {
		printf("Non sono state trovate camere con un numero di giorni superiori al limite (%d)\n", lim);	
	}
}
