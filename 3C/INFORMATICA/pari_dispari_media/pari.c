/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//PROTOTIPI
int creaNumero(int, int);
void conta(int , int *, int *);


//MAIN
int main() {

	int exit=0, numero1, numero2, numero3, N, pari=0, dispari=0;
	char scelta;

	srand(time(NULL));
	
	while(exit==0) {
		printf("\e[0;94mA contiuna, E esci \n");
		printf("Inserire una scelta: ");
		scanf("%c", &scelta);
		while(getchar()!='\n');

		switch(scelta) {
			case 'a':
			case 'A':
				N = creaNumero(1,10);
				conta(N, &pari, &dispari);
				printf("\e[0mCi sono %d numeri pari e %d numeri dispari \n", pari, dispari);
				pari=0;
				dispari=0;
				break;
			case 'e':
			case 'E':
				printf("\e[1;92mEsco dal programma ! \e[0m\n");
				exit=1;
				break;		
			default:
				printf("\e[1;91mOperatore non valido ! \n");
		}
	}

return 0;
}

//creaNumero
int creaNumero (int min, int max) {
return rand()%(max-min+1)+min;
}

//procedura B
void conta(int n, int *cP, int *cD) {

	int numero, i, tot=0;
	float media;

	for(i=0; i<n; i++){
		numero=creaNumero(7,15);
		tot = tot + numero;
		printf("%d ", numero);
		if(numero%2==0){
			(*cP)++; //tonde per dare precedenza all "*"
		}
		else {
			(*cD)++; //tonde per dare precedenza all "*"
		}
	}
	printf("\n"); //mando a capo dopo la serie di numeri scritti in riga con le tabulazioni
	media = (float) tot / n;
	printf("\e[0mLa media dei numeri vale: %.2f \n", media);
}
