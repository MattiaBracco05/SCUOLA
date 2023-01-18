/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

//PROTOTIPI
int creaRandom(int, int);
void creaMatrice(int*, int*);
void caricaMatrice(int[][MAX], int, int);
void stampaMatrice(int[][MAX], int, int);
void ricercaMatrice(int[][MAX], int, int);

int main() {

	int matrice[MAX][MAX], r, c, totale=0;
	srand(time(NULL));

	system("clear");
	creaMatrice(&r, &c);
	caricaMatrice(matrice, r, c);
	stampaMatrice(matrice, r, c);
	ricercaMatrice(matrice, r, c);

return 0;
}
//------------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	return rand()%(max-min+1)+min;
}
//------------------------------------------------------------------------------------------------------------------------------------
void creaMatrice(int *rig, int *col) {
	int r=0, c=0, min=1;
	while((r<min) || (r>MAX)) {
		printf("Quante righe vuoi avere nella tua matrice? (%d-%d): ", min, MAX);
		scanf("%d", &r);
	}
	*rig = r;
	while((c<min) || (c>MAX)) {
		printf("Quante colonne vuoi avere nella tua matrice? (%d-%d): ", min, MAX);
		scanf("%d", &c);
	}	
	*col = c;
}
//------------------------------------------------------------------------------------------------------------------------------------
void caricaMatrice(int matr[][MAX], int rig, int col) {
	int i, j;
	system("clear");
	printf("Creo una matrice %dx%d...\n", rig, col);
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {
			matr[i][j]= creaRandom(8,64);
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
void ricercaMatrice(int matr[][MAX], int rig, int col) {
	int i, j, val, find=0, posR, posC;
	printf("Inserisci un numero da cercare nella matrice: ");
	scanf("%d", &val);
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {
			if(val == matr[i][j]) {
				find++;
				posR = i;
				posC = j;
			}
		}
	}
	if(find > 0) {
		printf("Numero trovato (posizione: rig: %d, col: %d)\n", posR+1, posC+1);
	}
	else {
		printf("Numero non trovato!\n");
	}
}
