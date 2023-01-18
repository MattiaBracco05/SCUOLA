/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//AREA DEI PROTOTIPI----------------------------------------------------------------------------------------------------------------
void giocaPartita(int *, int *);
int giocataUtente();
int creaRandom(int, int);
void controlloVincita(int, int, int, int, int *, int *);
void controlloPartita(int, int, int *, int *, int *);
//----------------------------------------------------------------------------------------------------------------------------------
int main() {
	int exit=0, N, i, uscita, puntiUtente, puntiPc, vinteUT=0, vintePC=0, pareggi=0;
	srand(time(NULL));
	while(exit == 0) {
		N=0; //inizializzo "N" a 0 ad ogni ciclo del while
		while(N < 3 || N > 12) {	//chiedo le partite che vuole giocare
			printf("Quante partite vuoi giocare ? (3-12): ");
			scanf("%d", &N);
		}	
		puntiPc=0; puntiUtente=0; //azzero i punti parizali della singola partita
		for (i=0; i<N; i++){	//giro per "N" volte
			printf("\e[0;96m----Partita: %d----\e[0m\n", i+1);
			giocaPartita(&puntiUtente, &puntiPc);
		}
		controlloPartita(puntiUtente, puntiPc, &vinteUT, &vintePC, &pareggi); //controllo chi vince la partita
		printf("\e[0;93m");
		printf(" ________________________________________________________________________\n");
		printf("|                             DATI VITTORIE                              |\n");
		printf("|________________________________________________________________________|\n");
		printf("Vincite del computer: %d \n", vintePC);
		printf("Vincite dell' utente: %d \n", vinteUT);
		printf("Pareggi: %d \n", pareggi);
		printf("\e[0m");
		printf("Digita 1 per uscire | 0 per continuare a giocare: ");	//chiedo se vuole continuare a giocare o uscire
		scanf("%d", &uscita);
		if (uscita == 1) {
			printf("\e[1;92mEsco dal programma !\e[0m\n");
			exit=1;
		}
	}
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void giocaPartita(int *UT, int *PC) {
	int semeU, semePC, numeroU, numeroPC, pUT=0, pPC=0;
	semeU=giocataUtente();
	semePC=creaRandom(1,4);
	numeroU=creaRandom(1,10);
	numeroPC=creaRandom(1,10);
	printf("Numero carta dell' utente (random): %d \n", numeroU);
	printf("Seme carta dell' computer (1=Cuori, 2=Quadri, 3=Fiori, 4=Picche): %d \n", semePC);
	printf("Numero carta dell' computer: %d \n", numeroPC);
	controlloVincita(semeU, semePC, numeroU, numeroPC, &pUT, &pPC);	//controllo chi vince il round
	*UT = (*UT) + pUT; *PC = (*PC) + pPC;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int giocataUtente() {
	int seme, uscita=0;
	char scelta;
	while (uscita == 0) {
		printf("\e[0;94m");
		printf(" ________________________________________________________________________\n");
		printf("|                                 SEMI                                   |\n");
		printf("|Input Seme Corrsipondenza scelta PC                                     |\n");
		printf("|________________________________________________________________________|\n");
		printf("|C - Cuori (1)                                                           |\n");
		printf("|Q - Quadri (2)                                                          |\n");
		printf("|F - Fiori (3)                                                           |\n");
		printf("|P - Picche (4)                                                          |\n");
		printf("|________________________________________________________________________|\n");
		printf("\e[0m");
		printf("Inserire il seme: ");
		while(getchar()!='\n');
		scanf("%c", &scelta);
		switch(scelta) {
			case 'c':
			case 'C':
				seme=1; uscita=1;
				break;
			case 'q':
			case 'Q':
				seme=2; uscita=1;
				break;
			case 'f':
			case 'F':
				seme=3; uscita=1;
				break;
			case 'p':
			case 'P':
				seme=4; uscita=1;
				break;
			default:
				printf("\e[1;31mOperatore non valido !\e[0m\n");
		}
	}
return seme;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int creaRandom (int min, int max) {
	int num;
	num=rand()%(max-min+1)+min;
return num;	
}
//-----------------------------------------------------------------------------------------------------------------------------------
void controlloVincita(int semeUTENTE, int semeCOMPUTER, int numeroUTENTE, int numeroCOMPUTER, int *puntiUT, int *puntiPC) {
	if(semeUTENTE == semeCOMPUTER) {	//se i semi sono uguali
		if(numeroUTENTE == numeroCOMPUTER) {	//se anche i numeri sono uguali => pareggio
			printf("Pareggio ! \n");
			*puntiUT = (*puntiUT) + 1; *puntiPC = (*puntiPC) + 1;
		} else {	//controllo carta con numero maggiore
				if(numeroUTENTE > numeroCOMPUTER) {	//=> UTENTE
					printf("Vince l' utente ! \n");
					*puntiUT = (*puntiUT) + 3;
				}	else {	//=> COMPUTER
					printf("Vince il computer ! \n");
					*puntiPC = (*puntiPC) + 3;
					}
				}
		} else {	//se i semi non sono uguali
			//controllo se vince l' utente o il computers
			if( ((semeUTENTE == 1) && (semeCOMPUTER == 2)) || ((semeUTENTE == 2) && (semeCOMPUTER == 4)) || ((semeUTENTE == 3) && (semeCOMPUTER == 1)) || ((semeUTENTE == 4) && (semeCOMPUTER == 3)) ) {
				printf("Vince l' utente ! \n");
				*puntiUT = (*puntiUT) + 1;
			}	else if( ((semeCOMPUTER == 1) && (semeUTENTE == 2)) || ((semeCOMPUTER == 2) && (semeUTENTE == 4)) || ((semeCOMPUTER == 3) && (semeUTENTE == 1)) || ((semeCOMPUTER == 4) && (semeUTENTE == 3)) ) {
				printf("Vince il computer ! \n");	
				*puntiPC = (*puntiPC) + 3;
			}	else {	//altrimenti è un pareggio
					printf("Pareggio ! \n");
					*puntiUT = (*puntiUT) + 1; *puntiPC = (*puntiPC) + 1;
				}
			}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void controlloPartita(int puntiUtente, int puntiPc, int *Ut, int *Pc, int *Pa) {
		printf("\e[0;93m");
		if (puntiUtente > puntiPc) {
			(*Ut)++;
			printf("La partita la vince l' utente con %d punti !\n", puntiUtente);
		}
		if (puntiPc > puntiUtente) {
			(*Pc)++;
			printf("La partita la vince il pc con %d punti !\n", puntiPc);
		}
		if (puntiPc == puntiUtente) {
			printf("La partita termina con un pareggio !\n");
			(*Pa)++;
		}
		printf("\e[0m");
}
