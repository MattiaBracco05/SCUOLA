/*
Bracco Mattia 3C
creare una calcolatrice chiedendo 2 numeri (num1 e num2) e l' operatore (1=somma, 2=sottrazione, 3=moltiplicazione, 4=divisione)
*/

#include <stdio.h>

int main()  {

	int num1, num2, operatore, errore=0;
	float risultato=0.0;
	
	printf("inserire numero 1: ");
	scanf("%d", &num1);
	printf("inserire numero 2: ");
	scanf("%d", &num2);
	printf("inserire l' operaotre (1 = +, 2 = -, 3 = *, 4 = /): ");
	scanf("%d", &operatore);
	
	switch(operatore){
		case 1:
			risultato = num1 + num2;
			break;

		case 2:
			risultato = num1 - num2;
			break;

		case 3:
			risultato = num1 * num2;
			break;

		case 4:
			if (num2 == 0){
				printf("impossibile dividere un numero per 0 \n");
				errore=1;
			}
			else{
				risultato = (float) num1 / num2;
			}
			break;

		default:
			printf("hai scelto un operatore non valido ! \n");
			errore=1;
	}

	if(errore == 0){
		printf("il risultato è: %.2f \n", risultato);
	}
	
	
return 0;
}
