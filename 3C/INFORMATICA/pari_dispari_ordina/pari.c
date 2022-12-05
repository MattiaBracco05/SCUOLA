/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI
int creaNumero(int, int);
void funzioneA(int *, int *, int *);
void funzioneB(int, int *, int *);


//MAIN
int main() {

	int exit=0, numero1, numero2, numero3, N, pari=0, dispari=0;
	char scelta;

	srand(time(NULL));
	
	while(exit==0) {
		printf("A ordina numeri, B calcola pari e dispari, E esci \n");
		printf("Inserire una scelta: ");
		scanf("%c", &scelta);
		while(getchar()!='\n');

		switch(scelta) {
			case 'a':
			case 'A':
				numero1=creaNumero(9,34);
				numero2=creaNumero(9,34);
				numero3=creaNumero(9,34);
				printf("Num1: %d Num2: %d Num3: %d \n", numero1, numero2, numero3);
				funzioneA(&numero1, &numero2, &numero3);
				printf("Num1: %d Num2: %d Num3: %d \n", numero1, numero2, numero3);
				break;
			case 'b':
			case 'B':
				printf("Inserisci il valore di N: ");
				scanf("%d", &N);
				funzioneB(N, &pari, &dispari);
				printf("Ci sono %d numeri pari e %d numeri dispari \n", pari, dispari);
				pari=0;
				dispari=0;
				break;
			case 'e':
			case 'E':
				printf("Esco dal programma ! \n");
				exit=1;
				break;		
			default:
				printf("Operatore non valido ! \n");
		}
	}

return 0;
}

//creaNumero
int creaNumero (int min, int max) {
return rand()%(max-min+1)+min;
}

//procedura A
void funzioneA (int *r1, int *r2, int *r3) {

	int a = *r1, b = *r2, c = *r3;

	if (a <= b) {
		if (b <= c) {
			*r1 = a; *r2 = b; *r3 = c;
		}
		else {
			*r3 = b;
			if (a <= c) {
				*r1 = a; *r2 = c;
			}
			else {
				*r1 = c; *r2 = a;
			}
		}
	}
	else {
		if (a <= c) {
			*r1 = b; *r2 = a; *r3 = c;
		}
		else {
			*r3 = a;
			if (b <= c) {
				*r1 = b; *r2 = c;
			}
			else {
				*r1 = c; *r2 = b;
			}
		}
	}

}

//procedura B
void funzioneB(int n, int *cP, int *cD) {

	int numero, i;

	for(i=0; i<n; i++){
		numero=creaNumero(7,15);
		printf("%d ", numero);
		if(numero%2==0){
			(*cP)++; //tonde per dare precedenza all "*"
		}
		else {
			(*cD)++; //tonde per dare precedenza all "*"
		}
	}
	printf("\n"); //mando a capo dopo la serie di numeri scritti in riga con le tabulazioni
}
