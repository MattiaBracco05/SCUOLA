/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

//PROTOTIPI
char creaRandomChar(char, char);
void creaMatrice(int*, int*, int);
void caricaMatrice(char[][MAX], int, int);
void stampaMatrice(char[][MAX], int, int);
void numeroVocali(char[][MAX], int, int);
void corniceMatrice(char[][MAX], int, int);
void cercaChar(char[][MAX], int, int, char);

int main() {

	int r, c, minimo=2;	
	char matrice[MAX][MAX], lettera='F';
	srand(time(NULL));

	system("clear");
	creaMatrice(&r, &c, minimo);
	caricaMatrice(matrice, r, c);
	stampaMatrice(matrice, r, c);
	numeroVocali(matrice, r, c);
	cercaChar(matrice, r, c, lettera);

return 0;
}

//------------------------------------------------------------------------------------------------------------------------------------
char creaRandomChar(char min, char max) {
	return rand()%(max-min+1)+min;
}
//------------------------------------------------------------------------------------------------------------------------------------
void creaMatrice(int *rig, int *col, int min) {
	int r=0, c=0;
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
void caricaMatrice(char matr[][MAX], int rig, int col) {
	int i, j;
	system("clear");
	printf("Creo una matrice %dx%d...\n", rig, col);
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {
			matr[i][j]= creaRandomChar('A','Z');
		}
	}	
}
//------------------------------------------------------------------------------------------------------------------------------------
void stampaMatrice(char matr[][MAX], int rig, int col) {
	int i, j;
	printf("\e[0;94m");
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {
			printf("%c\t", matr[i][j]);
		}
		printf("\n");
	}
	printf("\e[0m");
}
//------------------------------------------------------------------------------------------------------------------------------------
void numeroVocali(char matr[][MAX], int rig, int col) {
	int i, j, tot=0, totRiga, max=0, pos;
	for(i=0; i<rig; i++) {
		totRiga = 0; //azzero il totale della singola riga
		for(j=0; j<col; j++) {
			if(matr[i][j] == 'A' || matr[i][j] == 'E' || matr[i][j] == 'I' || matr[i][j] == 'O' || matr[i][j] == 'U') {
				tot++; totRiga++;			
			}
		}
		printf("\e[0;93mRiga n.%d vocali presenti: %d\e[0m\n", i+1, totRiga);
		if(totRiga > max) {
			max = totRiga; pos = i;
		}
	}
	printf("In questa matrice sono presenti %d vocali\n", tot);
	printf("La riga con il maggior numero di vocali (%d) è la n.%d\n", max, pos+1);	
}
//------------------------------------------------------------------------------------------------------------------------------------
void cercaChar(char matr[][MAX], int rig, int col, char let) {
	int i, j, tot=0;
	//controllo bordo alto
	i=0;
	for(j=0; j<col; j++) {
		if(matr[i][j] == let) {
			tot++;			
		}
	}
	//controllo bordo basso
	i=rig-1;
	for(j=0; j<col; j++) {
		if(matr[i][j] == let) {
			tot++;			
		}
	}
	//controllo dei bordi ai lati
	for(i=1; i<rig-2; i++) { //"i=1" e "i<rig-2" perchè il bordo alto e il bordo basso sono già stati controllati
			if(matr[i][0] == let) { //controllo bordo SX
				tot++;			
			}
			if(matr[i][col-1] == let) { //controllo bordo DX
				tot++;			
			}		
	}
	if(tot > 0) {
		printf("In totale la lettera \e[0;93m|%c|\e[0m è presente %d volte sulla cornice della matrice\n", let, tot);
	} else {
		printf("\e[1;91mLa lettera \e[0;93m|%c|\e[1;91m non è presente sulla conrice della matrice\e[0m\n", let);
	}
}
