//Bracco Mattia 3C

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	int numero;
	srand(time(NULL));	
	numero=rand()%10; //crea numeri da 0 a 9, numero=rand()%10+1; crea numeri da 1 a 10
	printf("%d\n",numero);
	
return 0;
}
