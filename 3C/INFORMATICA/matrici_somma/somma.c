/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 25

//PROTOTIPI
int creaRandom(int, int);
void creaMatrice(int*, int*);
void caricaMatrice(int[][MAX], int, int);
void stampaMatrice(int[][MAX], int, int);
void sommaRighe(int[][MAX], int, int, int*);
void sommaColonne(int[][MAX], int, int);
void mediaMatrice(int, int, int);

int main() {

	int matrice[MAX][MAX], r, c, totale=0;
	srand(time(NULL));

	system("clear");
	creaMatrice(&r, &c);
	caricaMatrice(matrice, r, c);
	stampaMatrice(matrice, r, c);
	sommaRighe(matrice, r, c, &totale);
	sommaColonne(matrice, r, c);
	mediaMatrice(totale, r, c);
return 0;
}
//------------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	return rand()%(max-min+1)+min;
}
//------------------------------------------------------------------------------------------------------------------------------------
void creaMatrice(int *rig, int *col) {
	int val=0, min=10;
	while((val<min) || (val>MAX)) {
		printf("Quante grande vuoi avere la tua matrice quadrata? (%d-%d): ", min, MAX);
		scanf("%d", &val);
	}
	*rig = val;
	*col = val;
}
//------------------------------------------------------------------------------------------------------------------------------------
void caricaMatrice(int matr[][MAX], int rig, int col) {
	int i, j;
	system("clear");
	printf("Creo una matrice %dx%d...\n", rig, col);
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {
			matr[i][j]= creaRandom(10,25);
		}
	}	
}
//------------------------------------------------------------------------------------------------------------------------------------
void stampaMatrice(int matr[][MAX], int rig, int col) {
	int i, j;
	printf("\e[0;94m");
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {
			printf("%d\t", matr[i][j]);
		}
		printf("\n");
	}
	printf("\e[0m");
}
//------------------------------------------------------------------------------------------------------------------------------------
void sommaRighe(int matr[][MAX], int rig, int col, int *tot) {
	int i, j, totRiga;
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                               SOMMA RIGHE                              |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	for(i=0; i<rig; i++) {
		totRiga=0; //azzero ad ogni riga il tot
		for(j=0; j<col; j++) {
			totRiga = totRiga + matr[i][j]; //aggiungo al totale della riga il valore di ogni colonna presente in quella riga
		}
		*tot = *tot + totRiga;
		printf("n.%d vale: %d\n", i+1, totRiga);
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void sommaColonne(int matr[][MAX], int rig, int col) {
	int i, j, totColonna;
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                             SOMMA COLONNE                              |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	for(i=0; i<col; i++) {
		totColonna=0; //azzero ad ogni riga il tot
		for(j=0; j<rig; j++) {
			totColonna = totColonna + matr[i][j]; //aggiungo al totale della riga il valore di ogni colonna presente in quella riga
		}
		printf("n.%d vale: %d\n", i+1, totColonna);
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void mediaMatrice(int tot, int rig, int col) {
	int areaMatrice;
	float media;
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                            MEDIA MATRICE                               |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	areaMatrice = rig * col;
	media = (float) tot / areaMatrice;
	printf("Media: %.2f\n", media);
}
