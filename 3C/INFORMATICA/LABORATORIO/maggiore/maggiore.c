/*
Bracco Mattia 3C
dati 2 numeri interi stabilire il maggiore
*/

#include <stdio.h>

int main(){
	
	int N1, N2;	
	
	printf("inserire il primo numero: \n");
	scanf("%d", &N1);
	
	printf("inserire il secondo numero: \n");
	scanf("%d", &N2);
	
	if (N1 > N2){
		printf("il numero maggiore è: %d\n", N1);
	}
	
	else {
		printf("il numero maggiore è: %d\n", N2);
	}
	
return 0;
}
