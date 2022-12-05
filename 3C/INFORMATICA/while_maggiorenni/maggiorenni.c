/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main () {

	int eta=0, i=18;
	
	printf("scrivimi la tua età: ");
	scanf("%d", &eta);
	
	if(eta >= 18){
		printf("le età dei magiorenni più giovani di te sono: \n");
		
		while(i < eta){
		printf("%d\t", i);
		i=i+1;
		}
		
	}
	else {
		printf("sei troppo giovane... \n");
	}
	//inserisco una printf con il solo comando di andare a capo per mandare a capo finiti i numeri da scrivere
	printf("\n");
	
return 0;
}
