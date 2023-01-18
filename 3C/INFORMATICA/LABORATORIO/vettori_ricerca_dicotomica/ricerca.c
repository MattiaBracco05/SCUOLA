/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//AREA DEI PROTOTIPI
int creaRandom(int, int);
int chiediN(int, int);
void caricaVettore(int, int []);
void stampaVettore(int, int []);
void bubbleSort(int, int []);
int ricercaDicotomica(int, int, int[]);

int main() {
	int numeri[20], N, valore, posizione;
	srand(time(NULL));

	N = chiediN(1,10);
	caricaVettore(N, numeri);
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                               NON ORDINATI                             |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	stampaVettore(N, numeri);
	bubbleSort(N, numeri);
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                                 ORDINATI                               |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	stampaVettore(N, numeri);
	printf("\e[0;93m");
	printf(" ________________________________________________________________________\n");
	printf("|                                 RICERCA                                |\n");
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	printf("Inserisci un numero da cercare: ");
	scanf("%d", &valore);
	posizione = ricercaDicotomica(valore, N, numeri);
	if(posizione == -1) {
		printf("Numero %d non trovato\n", valore);	
	}
	else {
		printf("Numero %d trovato in posizione %d (considero anche la posizione 0)\n", valore, posizione);	
	}

return 0;
}

//------------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
return rand()%(max-min+1)+min;
}
//------------------------------------------------------------------------------------------------------------------------------------
int chiediN(int min, int max) {
	int n=0;
	while(n<min || n>max) {
		printf("Quanti numeri vuoi inserire nel vettore ? (%d-%d): ", min, max);
		scanf("%d",&n);	
	}
return n;
}
//------------------------------------------------------------------------------------------------------------------------------------
void caricaVettore(int N, int vett[]) {
	int i, num;
	for(i=0; i<N; i++) {
		vett[i] = creaRandom(1,20);
	}
	system("clear");
}
//------------------------------------------------------------------------------------------------------------------------------------
void stampaVettore(int N, int vett[]) {
	int i;
	for(i=0; i<N; i++) {
		printf("%d\t", vett[i]);	
	}
	printf("\n");
}
//------------------------------------------------------------------------------------------------------------------------------------
void bubbleSort(int N, int vett[]) {
	int j, i, flag, TMP;
	j = N;
	flag = 1; //1 => TRUE, 0 => FALSE
	while(flag == 1) {
		flag = 0;	
		for(i=0; i<j-1; i++) {
			if(vett[i] > vett[i+1])	{
				TMP = vett[i];
				vett[i] = vett[i+1];
				vett[i+1] = TMP;
				flag = 1;		
			}	
		}
		j--;	
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
int ricercaDicotomica(int val, int N, int vett[]) {
	int i=0, j=N-1, trovato=-1, pos;

	printf("Cerco il numero %d...\n", val);
	
	while((i<=j) && (trovato==-1)) {
		pos = (i+j) / 2;
		if(vett[pos] == val) {
			trovato = pos;
		}
		else {
			if(vett[pos] > val) {
				j = pos - 1;
			}
			else {
				i = pos + 1;
			}
		}
	}
return trovato;
}
