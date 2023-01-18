/*
Bracco Mattia 3C
*/

//AREA DEI PROTOTIPI
int creaRandom(int, int);
int chiediNum(int, int []);
int controlloDoppio(int, int, int []);

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	int numeri[14];
	int x, i;
	srand(time(NULL));
	
	x=creaRandom(7,13);
	printf("\e[0;94mDevi inserire %d numeri\e[0m\n", x);
	for (i=0; i<x; i++) {
		numeri[i]=chiediNum(x, numeri);
	}
	for (i=0; i<x; i++) {
		printf("%d\t", numeri[i]);
	}
	printf("\n");

return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {
	int num;
	num = rand()%(max-min+1)+min;
return num;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediNum (int dim, int vett []) {
	int max=44, min=4, doppio=0, num=0, exit=0;
	while (exit == 0) {
		printf("Inserisci un numero (4-44) che non sia ancora stato inserito: ");
		scanf("%d", &num);
		doppio = controlloDoppio(num, dim, vett);
		if ((num < min || num > max) || doppio != 0) {
			printf("\e[1;91mErrore ! numero fuori range o ripetuto\e[0m\n");
			exit = 0;
		} else {
			exit = 1;
		}
	}
return num;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int controlloDoppio (int num, int dim, int vett []) {
	int doppio=0, i;
	for (i=0; i<dim; i++) {
		if (num == vett[i]) {
			doppio++;
		}
	}
return doppio;
}
