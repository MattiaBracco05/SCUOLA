/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//AREA DEI PROTOTIPI
void dado();
int creaRandom();
int lettere();
int estrazione();

int main() {
	
	srand(time(NULL));
	
	int exit=0, distanza, frequenza;
	char Scelta;
	
	while (exit==0) {
		printf("A) Dadi \n");
		printf("B) Confronto lettere \n");
		printf("C) Frequenza numeri \n");
		printf("E) Esci \n");
		printf("Inserire una scelta: ");
		scanf("%c", &Scelta);
		while(getchar()!='\n');
		
		switch(Scelta) {
			
			case 'a':
			case 'A':
				dado();
				break;
			
			case 'b':	
			case 'B':
				distanza=lettere();
				printf("La distanza è %d \n", distanza);
				break;
			
			case 'c':
			case 'C':
				frequenza=estrazione();
				printf("Il numero con maggiore frequenza è: %d \n", frequenza);
				break;
			
			case 'e':
			case 'E':
				printf("Esco dal programma ! \n");
				exit=1;
				break;
					
			default:
				printf("Hai inserito un operatore non valido ! \n");
		}
	}

return 0;
}

void dado() {

	int N=0, i, utente1, utente2, computer1, computer2, sommaUtente=0, sommaComputer=0, pareggio=0, utente=0, computer=0;
	
	//chiedo il numero di partite (1 - 10)
	while (N < 1 || N > 10) {
		printf("Numero partite: ");
		scanf("%d", &N);
	}
	
	//gioco le N partite
	for (i=0; i<N; i++) {
		printf("Partita %d \n", i+1);
		printf("Utente: \n");
		utente1 = creaRandom();
		utente2 = creaRandom();
		printf("\n");
		printf("Computer: \n");
		computer1 = creaRandom();
		computer2 = creaRandom();
		
		//determino chi vince la singola partita
		sommaUtente = utente1 + utente2;
		sommaComputer = computer1 + computer2;
		printf("\n");
		printf("Somma Utente: %d Somma Computer: %d \n", sommaUtente, sommaComputer);
		
		if (sommaUtente == sommaComputer) {
			printf("Pareggio ! \n");
			pareggio++;
		}
		else {
			if (sommaUtente > sommaComputer){
				printf("Vince l' utente ! \n");
				utente++;
			}
			else {
				printf("Vince il computer ! \n");
				computer++;
			}
		}
	}
	
	//resoconto finale di tutte le partite
	printf("Partite pareggiate: %d, Partite vinte dal computer %d, Partite vinte dall' utente: %d \n", pareggio, computer, utente);

}

//funzione per generare numeri random
int creaRandom() {

	int numero;
	
	numero=rand()%5+1;
	printf("%d \t", numero);
	
return numero;
}

//funzione per le lettere
int lettere() {

	int distanza;
	char lettera1=' ', lettera2=' ';
	
	//inseirmento prima lettera
	while (lettera1 < 'a' || lettera1 > 'z') {
		printf("Inserisci una lettera minuscola: ");
		scanf("%c", &lettera1);
		while(getchar()!='\n');
	}
	
	//inserimento seconda lettera
	while (lettera2 < 'a' || lettera2 > 'z') { 
		printf("Inserisci una seconda lettera minuscola: ");
		scanf("%c", &lettera2);
		while(getchar()!='\n');
	}
	
	//controllo uguali o diverse, stampo in maiuscolo
	if (lettera1 == lettera2) {
		printf("Le lettere sono uguali. ");
	}
	else {
		printf("Le lettere NON sono uguali. ");
	}
	
	printf("Le lettere MAIUSCOLE sono %c e %c \n", lettera1-32, lettera2-32);
	
	//distanza tra le lettere
	if (lettera1 > lettera2) {
		distanza = lettera1 - lettera2;
	}
	else {
		distanza = lettera2 - lettera1;
	}
	
return distanza;
}

int estrazione() {

	int N=0, i, numero, num1=0, num2=0, num3=0, num4=0, num5=0, num6=0, maggiore;
	
	//inserisco numero di estrazioni
	while (N < 6 || N > 20) {
		printf("Inserire numero estrazioni (6 - 20): ");
		scanf("%d", &N);
	}
	
	//faccio le N estrazioni e incremento il contatore del numero che è uscito
	for (i=0; i<N; i++){
		numero = creaRandom();
		
		switch (numero) {
			case 1:
				num1++;
				break;
			case 2:
				num2++;
				break;
			case 3:
				num3++;
				break;
			case 4:
				num4++;
				break;
			case 5:
				num5++;
				break;
			case 6:
				num6++;
				break;
		}
	}
	//stampo la tabella delle frequenze
	printf("\n");
	printf("1: "); for (i=0; i<num1; i++){ printf("*"); }
	printf("\n");
	printf("2: "); for (i=0; i<num2; i++){ printf("*"); }
	printf("\n");
	printf("3: "); for (i=0; i<num3; i++){ printf("*"); }
	printf("\n");
	printf("4: "); for (i=0; i<num4; i++){ printf("*"); }
	printf("\n");
	printf("5: "); for (i=0; i<num5; i++){ printf("*"); }
	printf("\n");
	printf("6: "); for (i=0; i<num6; i++){ printf("*"); }
	printf("\n");
	
	//verifico quale numero ha la frequenza maggiore
	if (num1 > num2 && num1 > num3 && num1 > num4 && num1 > num5 && num1 > num6){
		maggiore=1;
	}
	
	if (num2 > num1 && num2 > num3 && num2 > num4 && num2 > num5 && num2 > num6){
		maggiore=2;
	}
	
	if (num3 > num1 && num3 > num2 && num3 > num4 && num3 > num5 && num3 > num6){
		maggiore=3;
	}
	
	if (num4 > num1 && num4 > num2 && num4 > num3 && num4 > num5 && num4 > num6){
		maggiore=4;
	}
	
	if (num5 > num1 && num5 > num2 && num5 > num3 && num5 > num4 && num5 > num6){
		maggiore=5;
	}
	
	if (num6 > num1 && num6 > num2 && num6 > num3 && num6 > num4 && num6 > num5){
		maggiore=6;
	}
	
	
return maggiore;
}
