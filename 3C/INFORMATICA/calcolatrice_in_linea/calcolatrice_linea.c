/*
Bracco Mattia 3C
*/

#include <stdio.h>

//area dei prototipi----------------------------------------------------------------------------------------------------------------
int addizione(int,int);
int sottrazione(int,int);
int moltiplicazione(int,int);
float divisione(int,int);
int potenza(int,int);

//-----------------------------------------------------------------------------------------------------------------------------------
int main() {
	
	int numero1, numero2, exit=0;
	float ris;
	char operatore;

	while (exit==0) {
	
		printf(" ________________________________________________________________________\n");
		printf("|                          MENU DEGLI OPERATORI                          |\n");
		printf("|COMANDO          CHE COSA FA                                            |\n");
		printf("|________________________________________________________________________|\n");
		printf("| +) ADDIZIONE                                                           |\n");
		printf("| -) SOTTRAZIONE                                                         |\n");
		printf("| *) MOLTIPLICAZIONE                                                     |\n");
		printf("| /) DIVISIONE                                                           |\n");
		printf("| ^) POTENZA                                                             |\n");
		printf("| EEE) EXIT                                                              |\n");
		printf("|________________________________________________________________________|\n");
        
		printf("Inserire l' operazione senza usare spazi (es. 1+1): ");
		scanf("%d", &numero1);
		operatore=getchar();
		scanf("%d", &numero2);
		while(getchar()!='\n');
		
		switch (operatore) {
			
			case '+':
				ris = addizione(numero1, numero2);		
				break;
			case '-':
				ris = sottrazione(numero1, numero2);
				break;
			case '*':
				ris = moltiplicazione(numero1, numero2);
				break;
			case '/':
				ris = divisione(numero1, numero2);
				break;
			case '^':
				ris = potenza(numero1, numero2);
				break;
			case 'e':
			case 'E':
				printf("Esco dal programma ! \n");
				exit=1;
				break;
			default:
				printf("Operatore non valido ! \n");
						
		}
		//stampo il risultato solo se non ho scelto di uscire
		if (exit==0) {
		 printf("Il risultato è %.2f \n", ris);
		}
	}

return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------
int addizione (int num1, int num2) {

	int somma;
	
	somma =  num1 + num2;

return somma;
}

//-----------------------------------------------------------------------------------------------------------------------------------
int sottrazione (int num1, int num2) {

	int differenza;
	
	differenza = num1 - num2;

return differenza;
}

//-----------------------------------------------------------------------------------------------------------------------------------
int moltiplicazione (int num1, int num2) {

	int prodotto;
	
	prodotto = num1 * num2;

return prodotto;
}

//-----------------------------------------------------------------------------------------------------------------------------------
float divisione (int num1, int num2) {

	float quoziente;
	
	quoziente = (float) num1 / num2;

return quoziente;
}

//-----------------------------------------------------------------------------------------------------------------------------------
int potenza (int num1, int num2) {

	int elevato=1, i=0;
	
	while(i < num2) {
		elevato = num1 * elevato;
		i=i+1;
	}

return elevato;
}
