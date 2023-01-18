/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	int i=0, n=0, totale=0;
	float media=0;
	
	while(n >= 0){
	printf("inserisci un numero intero: \n");
	scanf("%d", &n);
	totale = totale + n;
	media = (totale / (i+1));
	printf("la media vale: %.2f\n", media);
	i++;
	}

return 0;
}
