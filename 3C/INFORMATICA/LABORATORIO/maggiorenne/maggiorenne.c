/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	
	int eta = 0;
	
	printf("inserisci la tua età: \n");
	scanf("%d", &eta);
	
	if(eta > 18){
		printf("sei maggiorenne \n");
	}
	else{
		printf("non sei maggiorenne \n");
	}

return 0;
}
