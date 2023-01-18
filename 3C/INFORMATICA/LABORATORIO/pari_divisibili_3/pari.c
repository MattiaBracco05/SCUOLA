/*
Bracco Mattia 3C
*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(){

	int LIMITE=20, i=0, numero, pari, divisibile, multiplo=0;
	srand(time(NULL));
	
	while(i < LIMITE){
		numero=rand()%101+50;
		pari = numero % 2;
		//se il numero è pari lo stampo a video e verifico se è divisbile per 3 altrimenti non faccio niente e non incremento i
		if(pari == 0){
			printf("%d, ", numero);
			divisibile = numero % 3;
			i++;
			if(divisibile == 0){
				printf("il numero è divisibile per 3 \n");
				multiplo = multiplo + 1;
			}
			else{
				printf("il numero non è divisibile per 3 \n");
			}
		}
	}
	
	printf("in totale i multipli di 3 sono: %d\n", multiplo);

return 0;
}
