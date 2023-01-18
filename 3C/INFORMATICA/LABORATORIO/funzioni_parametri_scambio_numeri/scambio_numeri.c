/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//area dei prototipi-----------------------------------------------------------------------------------------------------------------
void scambia(int, int);
void scambiaIndirizzo(int *, int *);

//-----------------------------------------------------------------------------------------------------------------------------------
int main() {

	int num1, num2;
	srand(time(NULL));

	num1=rand()%10+1;
	num2=rand()%20+10;
	printf("Numero 1: %d Numero 2: %d \n", num1, num2);

	scambia(num1, num2);
	printf("-NUMERI (NON) SCAMBIATI 1 PROC.- \n");
	printf("Numero 1: %d Numero 2: %d \n", num1, num2); //non vengono cambiati nel main ma solo nella procedura !
	
	scambiaIndirizzo(&num1, &num2);
	printf("-NUMERI SCAMBIATI 2 PROC.- \n");
	printf("Numero 1: %d Numero 2: %d \n", num1, num2);
	

return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------
void scambia(int a, int b) {
	int temp = 0;
	temp = a;
	a = b;
	b = temp;
	printf("-DENTRO ALLA 1 PROCEDURA- \n");
	printf("a: %d b: %d \n", a, b);
}

//-----------------------------------------------------------------------------------------------------------------------------------
void scambiaIndirizzo(int *n1, int *n2) {
	int temp;
	temp = *n1;
	*n1 = *n2;
	*n2 = temp;
	printf("-DENTRO ALLA 2 PROCEDURA- \n");
	printf("a: %d b: %d \n", *n1, *n2);
}



