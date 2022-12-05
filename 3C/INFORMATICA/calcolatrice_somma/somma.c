/*
Bracco Mattia 3C
dati 2 numeri, calcolare e stampare a video la loro somma
*/

#include <stdio.h>

int main() {
	//dichiarazioni variabili
	int N1, N2, Somma;
	
	printf("Inserire il primo numero: \n");
	scanf("%d",&N1);
	
	printf("Inserire il secondo numero: \n");
	scanf("%d",&N2);
	
	Somma=N1+N2;
	
	printf("La somma di %d + %d vale: %d\n",N1, N2, Somma);
	
return 0;
}									
