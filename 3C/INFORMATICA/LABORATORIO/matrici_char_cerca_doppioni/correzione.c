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
void cercaDoppioni(char[][MAX], int, int);

int main() {

	int r, c, minimo=7;	
	char matrice[MAX][MAX], lettera='F';
	srand(time(NULL));

	system("clear");
	creaMatrice(&r, &c, minimo);
	caricaMatrice(matrice, r, c);
	stampaMatrice(matrice, r, c);
	cercaDoppioni(matrice, r, c;
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
void cercaDoppioni(char matr[][MAX], int rig, int col) {
	int i, j, x, y, flag;	
	//scorro la matrice
	for(i=0; i<rig; i++) {
		for(j=0; j<col; j++) {

			//se la cella è diversa da '0'
			if(matr[i][j] != '0') {
				flag = 0; //azzero il flag

				//scorro la "sotto matrice" attorno alla cella
				for(x=i-1; x<=i+1; x++) {
					if(x>=0 && x<rig) {
						for(y=j-1; y<=j+1; y++) {
							if(y>=0 && y<col) {
								if(y!=j || x!=i) {
									//se trovo una lettera uguale nella cornice => metto il flag a "1"
									if(matr[i][j] == matr[x][y]) {
										flag = 1;
									}
								}
							}
						}
					}
				}

				//se trovato (flag == 1)
				if(flag == 1) {
					//scorro la "sotto matrice"
					for(x=i-1; x<=i+1; x++) {
						if(x>=0 && x<rig) {
							for(y=j-1; y<=j+1; y++) {
								if(y>=0 && y<col) {
									if(y!=j || x!=i) {
										//se non è la cella stessa => metto lo '0'
										if(matr[i][j] != matr[x][y]) {
											matr[x][y] = '0';
										}
									}
								}
							}
						}
					}
				}

			} //chiudo il controllo " != '0' "
		} //chiudo i 2 cicli for per scorrere le matrici
	}
}
