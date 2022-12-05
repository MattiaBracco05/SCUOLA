/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()  {
	
	int righe=0, colonne, i, j;
	srand(time(NULL));	
	
	while(righe < 3){
		printf("inseire il numero di righe: ");
		scanf("%d", &righe);
	}
	colonne=rand()%18+3;
	
	printf("costruisco un rettngolo di %d righe e %d colonne \n", righe, colonne);
	
	//costrusco il bordo alto
	for(i=0; i<colonne; i++){
		printf("*");
	}
	//mando a capo
	printf("\n");
	
	//costruisco la parte centrale
	//finche le righe -2 (tolti i bordi alti e bassi) sono maggiori o uguali a 1 stampo "*" 
	for(i = 0; i < (righe-2); i++){
		printf("*");
		//finche i è minore di colonne - 2 (tolti i bordi a dx e sx) stampo "q"
		for(j=0; j < (colonne-2); j++){
			printf("q");
		}
		//stampo il bordo a destra
		printf("*");
		//mando a capo per la riga successiva e sottraggo 1 alla variabile righe
		printf("\n");
	}
	
	//costruisco il bordo basso
	for(i=0; i<colonne; i++){
		printf("*");
	}
	//mando a capo
	printf("\n");
	
return 0;
}
