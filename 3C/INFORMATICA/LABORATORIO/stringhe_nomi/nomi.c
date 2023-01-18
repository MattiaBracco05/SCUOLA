// C++ implementation

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 300
#define MAXRIGHE 10

//PROTOTIPI
void caricaNomi(char[][MAX]);
void ordinaNomi(char [][MAX], int);
void stampaNomi(char [][MAX], int);

int main() {
	int N;
	char matrice[MAXRIGHE][MAX];
	
	system("clear");
	caricaNomi(matrice);
	N = sizeof(matrice)/sizeof(matrice[0]);
	printf(" ________________________________________________________________________\n");
	printf("|                                                                        |\n");
	printf("|                     NOMI IN ORDINE DI INSERIMENTO                      |\n");
	printf("|________________________________________________________________________|\n");
	stampaNomi(matrice, N);
	printf(" ________________________________________________________________________\n");
	printf("|                                                                        |\n");
	printf("|                       NOMI IN ORDINE ALFABETICO                        |\n");
	printf("|________________________________________________________________________|\n");
	ordinaNomi(matrice, N);
	stampaNomi(matrice, N);

return 0;
}
//------------------------------------------------------------------------------------------------------------------------------------
void caricaNomi(char matr[][MAX]) {
	
	int i, l, limite=100;
	char temp[limite+1];
	for(i=0; i<10; i++) {
		printf("Inserisci il %d° nome (MAX %d caratteri): ", i+1, limite);
		gets(temp);
		while((strlen(temp) > limite) || (strlen(temp) == 0)) {
				printf("ERRORE! testo vuoto o fuori dal range MAX (%d)!\n", limite);
				printf("Inserisci il %d° nome (MAX %d caratteri): ", i+1, limite);
				gets(temp);
		}
		strcpy(matr[i], temp);
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void ordinaNomi(char nomi[][MAX], int N) {
	int i, j;	
	char TMP[MAX];
	for (i=0; i<N-1; i++) {
		for (j=0; j<N-1-i; j++) {
			if (strcmp(nomi[j], nomi[j+1]) > 0) {
				strcpy(TMP, nomi[j]);
				strcpy(nomi[j], nomi[j+1]);
				strcpy(nomi[j+1], TMP);
			}
		}
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void stampaNomi(char nomi[][MAX], int N) {
	 int i;
	 for (i=0; i<N; i++) {
		printf("Nome n.%d: %s\n", i+1, nomi[i]);
	}
}
