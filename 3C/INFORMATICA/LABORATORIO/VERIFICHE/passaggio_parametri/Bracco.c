/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//AREA DEI PROTOTIPI
int creaRandom(int,int);
int chiediNumero();
int confronto();
int frequenza();

char chiediLettera();

void dadi();

//----------------------------------------------------------------------------------------------------------------------------------
int main() {

	int exit=0, dist, freq;
	char scelta;
	
	srand(time(NULL));
	
	while(exit == 0){	
	
		printf(" ________________________________________________________________________\n");
        printf("|                          MENU DEGLI OPERATORI                          |\n");
        printf("|COMANDO          CHE COSA FA                                            |\n");
        printf("|________________________________________________________________________|\n");
        printf("| A- Dadi                                                                |\n");
        printf("| B- Confronto lettere                                                   |\n");
        printf("| C- Frequenza numeri                                                    |\n");
        printf("| E- EXIT                                                                |\n");
        printf("|________________________________________________________________________|\n");
        
		scelta = chiediLettera();
	
		switch(scelta){
		
			case 'A':
			case 'a':
				dadi();
				break;
				
			case 'B':
			case 'b':
				dist = confronto();
				printf("La distanza tra le due lettere è di %d \n", dist);
				break;
				
			case 'C':
			case 'c':
				freq = frequenza();
				printf("Il numero con frequenza maggiore è: %d ! \n", freq);	
				break;
				
			case 'E':
			case 'e':
				printf("Esco dal programma ! \n");
				exit = 1;
				break;
			
			default:
				printf("Operatore non valido ! \n");
		}
	}

return 0;
}

//----------------------------------------------------------------------------------------------------------------------------------
int chiediNumero() {

	int Num=0;
	
	while (Num < 1 || Num > 10) {
		printf("Inserire un numero (1-10): ");
		scanf("%d", &Num);
	}

return Num;
}

//----------------------------------------------------------------------------------------------------------------------------------
char chiediLettera() {

	char Let;
	while(getchar()!='\n');
	while (Let < 'a' || Let > 'b') {
		printf("Inserire una lettera: \n");
		scanf("%c", &Let);
	}
	while(getchar()!='\n');

return Let;
}

//----------------------------------------------------------------------------------------------------------------------------------
int creaRandom(int min, int max) {

	int rand;

	rand = random()%((max-min+1)-min);

return rand;
}

//----------------------------------------------------------------------------------------------------------------------------------
void dadi() {

		int partite=0, i, PC, PC2, UTENTE, UTENTE2, sommaPC=0, sommaUTENTE=0;
		
		partite = chiediNumero();

		for (i=0; i < partite; i++) {
			printf("\n");
			printf("Partita: %d \n", i+1);
			PC = creaRandom(1,6);
			UTENTE = creaRandom(1,6);
			PC2 = creaRandom(1,6);
			UTENTE2 = creaRandom(1,6);
			
			sommaPC = PC + PC2;
			sommaUTENTE = UTENTE + UTENTE2;
			
			printf("PC: num1 = %d, num2 = %d, somma = %d \n", PC, PC2, sommaPC);
			printf("UTENTE: num1 = %d, num2 = %d, somma = %d \n", UTENTE, UTENTE2, sommaUTENTE);
			
		if (sommaPC > sommaUTENTE) {
			printf("Ha vinto il computer! \n");
		}
		else {
			if (sommaPC == sommaUTENTE) {
				printf("Pareggio ! \n");
			}
			else {
				printf("Ha vinto l' utente ! \n");
			}
		}
	}
}

//----------------------------------------------------------------------------------------------------------------------------------
int confronto(){

	int distanza;
	char l1, l2;
	
	l1 = chiediLettera();
	l2 = chiediLettera();
	
	if (l1 == l2) {
		printf("Le lettere sono uguali ! \n");
	}
	else {
		printf("Le lettere non sono uguali ! \n");
	}
	
	printf("La lettera %c in maiuscolo = %c\n", l1, l1-32);
	printf("La lettera %c in maiuscolo = %c\n", l2, l2-32);
	
	if ((l1 - l2) > 0) {
		distanza = l1 - l2;
	}
	else {
		distanza = l2 - l1;
	}

return distanza;
}

//----------------------------------------------------------------------------------------------------------------------------------
int frequenza() {

	int estrazioni=0, i, pallina, max;
	int p1=0, p2=0, p3=0, p4=0, p5=0, p6=0;
	
	estrazioni = chiediNumero();
	
	for (i=0; i<estrazioni; i++) {
		pallina = creaRandom(1,6);
		
		switch (pallina) {
			case 1:
				p1++;
			case 2:
				p2++;
			case 3:
				p3++;
			case 4:
				p4++;
			case 5:
				p5++;
			case 6:
				p6++;
		}
	}
	
	if (p1 > p2 && p1 > p3 && p1 > p4 && p1 > p5 && p1 > p6) {
		max = 1;
	}
	else if (p2 > p1 && p2 > p3 && p2 > p4 && p2 > p5 && p2 > p6) { 
		max = 2;
	}
	else if (p3 > p1 && p3 > p2 && p3 > p4 && p3 > p5 && p3 > p6) { 
		max = 3;
	}
	else if (p4 > p1 && p4 > p2 && p4 > p3 && p4 > p5 && p4 > p6) { 
		max = 4;
	}
	else if (p5 > p1 && p5 > p2 && p5 > p3 && p5 > p4 && p5 > p6) { 
		max = 5;
	}
	else {
		max = 6;
	}
	
return max;
}

