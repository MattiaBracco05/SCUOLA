/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//area dei prototipi
void chiediN();
int ricavaNumero();
void richiediN();
int inserisciNumero();


int main () {
	
	srand(time(NULL));
	
	chiediN(); //chiedi quanti numeri si vuole utilizzare (N)
	richiediN();
	
	
return 0;
}

//creo una procedura che chieda l' inserimento di N
void chiediN() {

	int N=0, i, num, max=0;

	while(N < 3 || N > 15){
		printf("Quanti numeri vuoi ? (3 - 15): ");
		scanf("%d", &N);
	}
	
	for(i=0; i<N; i++){
		num=ricavaNumero();
		if (num > max){
			max = num;
		}
	}
	printf("Il numero maggiore è: %d \n", max);
}

//creo una funzione che mi calcola col random il numero e me lo restituisce
int ricavaNumero() {

	int num;
	
	num=rand()%61+9;
	printf("%d \n", num);
	
return num;
}

//richiedo i numeri N con una procedura
void richiediN() {

	int N=0, i, num, min=100;

	while(N < 3 || N > 15){
		printf("Quanti numeri vuoi ? (3 - 15): ");
		scanf("%d", &N);
	}
	
	for(i=0; i<N; i++){
	 	num=inserisciNumero();
	 
	 	if (num < min){
		min = num;
		}
	}
	
	printf("Il numero minore è: %d \n", min);
	
}

//creo una funzione per inserire i numeri
int inserisciNumero() {

	int num=0;
	
	while(num < 30 || num > 100){
		printf("inserisci un numero (30 - 100): ");
		scanf("%d", &num);
	}
	
return num;
}


