/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {

	int N, i=0;
	float numero, TOTALE, MEDIA;
	
	printf("inserisci quanti numeri vuoi elaborare: \n");
	scanf("%d", &N);
	
	while(i < N){
	printf("inserisci un numero: \n");
	scanf("%f", &numero);
	TOTALE = TOTALE + numero;
	i = i + 1;
	}
	
	MEDIA = TOTALE / N;
	
	printf("la media vale %.2f \n", MEDIA);
	
return 0;
}
