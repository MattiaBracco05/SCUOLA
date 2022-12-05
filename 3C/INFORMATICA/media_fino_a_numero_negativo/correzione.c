/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	int i=0, n=0, somma=0;
	float media=0;
	
	printf("inserisci un numero intero: \n");
	scanf("%d", &n);
	
	while(n >= 0){
		somma = somma + n;
		i++;
		media = somma / i;
		printf("la media vale: %.2f\n", media);
		printf("inserisci un numero intero: \n");
		scanf("%d", &n);
	}

return 0;
}
