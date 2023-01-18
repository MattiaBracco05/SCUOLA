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
void caricaMatrice(int[][MAX], int, int); //devo passare "MAX" nelle "[]" delle colonne
void stampaMatrice(int[][MAX], int, int); //devo passare "MAX" nelle "[]" delle colonne

int main() {

	int matrice[MAX][MAX], r, c;
	srand(time(NULL));

	system("clear");
	creaMatrice(&r, &c);
	caricaMatrice(matrice, r, c);
	stampaMatrice(matrice, r, c);

return 0;
}
//------------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	return rand()%(max-min+1)+min;
}
//------------------------------------------------------------------------------------------------------------------------------------
void creaMatrice(int *rig, int *col) {
	int r=0, c=0;
	while((r<1) || (r>MAX)) {
		printf("Quante righe vuoi avere nella tua matrice? (1-%d): ", MAX);
		scanf("%d", &r);
	}
	*rig = r;
	while((c<1) || (c>MAX)) {
		printf("Quante colonne vuoi avere nella tua matrice? (1-%d): ", MAX);
		scanf("%d", &c);
	}
	*col = c;
}
//------------------------------------------------------------------------------------------------------------------------------------
//devo scrivere "MAX" nelle "[]" delle colonne
void caricaMatrice(int matr[][MAX], int rig, int col) {
	int i, j;
	system("clear");
	printf("Creo una matrice %dx%d (righe x colonne)...\n", rig, col);
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {
			matr[i][j]= creaRandom(0,9);
		}
	}	
}
//------------------------------------------------------------------------------------------------------------------------------------
//devo scrivere "MAX" nelle "[]" delle colonne
void stampaMatrice(int matr[][MAX], int rig, int col) {
	int i, j;
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {
			printf("%d\t", matr[i][j]);
		}
		printf("\n");
	}
}
