/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 23

//PROTOTIPI
char creaRandomChar(char, char);
void creaMatrice(int*, int*, int);
void caricaMatrice(char[][MAX], int, int);
void stampaMatrice(char[][MAX], int, int);
void scorriMatrice(char[][MAX], int, int);
void cercaDoppioni(char[][MAX], int, int, char);

int main() {

	int r, c, minimo=7;	
	char matrice[MAX][MAX], lettera='F';
	srand(time(NULL));

	system("clear");
	creaMatrice(&r, &c, minimo);
	caricaMatrice(matrice, r, c);
	stampaMatrice(matrice, r, c);
	scorriMatrice(matrice, r, c);
	stampaMatrice(matrice, r, c);
	
return 0;
}

//------------------------------------------------------------------------------------------------------------------------------------
char creaRandomChar(char min, char max) {
	char CAPS;
	CAPS = rand()%(max-min+1)+min; //decido random il CAPS
	if(CAPS == '0') {
		min = 'a'; max = 'z'; //lettere minuscole
	}
	if(CAPS == '1') {
		min = 'A'; max = 'Z'; //lettere MAIUSCOLE
	}
return rand()%(max-min+1)+min; //lettere random
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
			matr[i][j]= creaRandomChar('0','1');
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
void scorriMatrice(char matr[][MAX], int rig, int col) {
	int i, j, stato;
	char let;
	printf("Vado a sotituire con '0' i caratteri della cornice che si ripetono nella matrice...\n");
	for(i=1; i<rig-2; i++) {
		for(j=1; j<col-2; j++) {
			let = matr[i][j];
			cercaDoppioni(matr, rig, col, let);
		}
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void cercaDoppioni(char matr[][MAX], int rig, int col, char let) {
	int i, j;
	//controllo bordo alto
	i=0;
	for(j=0; j<col; j++) {
		if(matr[i][j] == let) {
			matr[i][j] = '0';
		}
	}
	//controllo bordo basso
	i=rig-1;
	for(j=0; j<col; j++) {
		if(matr[i][j] == let) {
			matr[i][j] = '0';
		}
	}
	//controllo dei bordi ai lati
	for(i=1; i<rig-2; i++) { //"i=1" e "i<rig-2" perchè il bordo alto e il bordo basso sono già stati controllati
		//bordo SX
		if(matr[i][0] == let) {
			matr[i][0] = '0';
		}
		//bordo DX
		if(matr[i][col-2] == let) {
			matr[i][col-2] = '0';
		}
	}
}
