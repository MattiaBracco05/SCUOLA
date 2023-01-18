/*
Bracco Mattia 4C ~ Compito vacanze estive
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MINSQUADRE 3
#define MAXSQUADRE 5
#define MINGIOCATORI 2
#define MAXGIOCATORI 6
#define MAXGIOCATORI_tot 30
#define MAXLUN 30

//PROTOTIPI
int chiediNSquadre();
int chiediNGiocatori();
int controlloNum(int, int, int[]);
int controlloGol(int);
void azzeraMaglie(int[]);
void caricaDati(int, int, char[][MAXLUN], char[][MAXLUN], int[], int[]);
void stampaRiepilogo(int, int);
void stampaDati(int, int, char[][MAXLUN], char[][MAXLUN], int[], int[]);

int main() {
	int NSquadre, NGiocatori, numeriMaglia[MAXGIOCATORI_tot], gol[MAXGIOCATORI_tot];
	char nomiSquadre[MAXSQUADRE][MAXLUN], nomiGiocatori[MAXGIOCATORI_tot][MAXLUN];

	system("clear");
	NSquadre = chiediNSquadre();
	NGiocatori = chiediNGiocatori();
	stampaRiepilogo(NSquadre, NGiocatori);
	azzeraMaglie(numeriMaglia);
	caricaDati(NSquadre, NGiocatori, nomiSquadre, nomiGiocatori, numeriMaglia, gol);
	stampaDati(NSquadre, NGiocatori, nomiSquadre, nomiGiocatori, numeriMaglia, gol);
	
return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediNSquadre() {
	int val=0;
	while (val<MINSQUADRE || val>MAXSQUADRE) {
		printf("Quante squadre vuoi registrare? (%d-%d): ", MINSQUADRE, MAXSQUADRE);
		scanf("%d",&val);
	}
return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediNGiocatori() {
	int val=0;
	while (val<MINGIOCATORI || val>MAXGIOCATORI) {
		printf("Quante giocatori vuoi registrare per ogni squadra? (%d-%d): ", MINGIOCATORI, MAXGIOCATORI);
		scanf("%d",&val);
	}
return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void stampaRiepilogo(int squadre, int giocatori) {
	system("clear");
	printf("\e[0;94m");
	printf(" ________________________________________________________________________\n");
	printf("|                                                                        |\n");
	printf("|                          RIEPILOGO SQUADRE                             |\n");
	printf("|________________________________________________________________________|\n");
	printf("| · Squadre registrate: %d                                                |\n", squadre);
	printf("| · Numero di giocatori per ogni squadra: %d                              |\n", giocatori);
	printf("|________________________________________________________________________|\n");
	printf("\e[0m");
	while(getchar() != '\n');
	printf("\nPremi invio per continuare...");
	getchar();
}
//-----------------------------------------------------------------------------------------------------------------------------------
void azzeraMaglie (int vett[]) {
	int i;
	for (i=0; i<MAXGIOCATORI_tot; i++) {
		vett[i] == 0;
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------
void caricaDati(int squadre, int giocatori, char nomiS[][MAXLUN], char nomiG[][MAXLUN], int numeri[], int gol[]) {
	int i, j, k=0, numTemp, golTemp, flag;
	char temp[MAXLUN+1];
	for (i=0; i<squadre; i++) {	//CICLO PER LE N SQUADRE
		system("clear");
		printf("\e[0;94m");
		printf(" ________________________________________________________________________\n");
		printf("|                                                                        |\n");
		printf("|                            SQUADRA %d di %d                              |\n", i+1, squadre);
		printf("|________________________________________________________________________|\n");
		printf("\e[0m");
		//----nome squadra----
		printf("Inserisci il nome della squadra %d: ", i+1);
		gets(temp);
		while ((strlen(temp) > MAXLUN) || (strlen(temp) == 0)) {
				printf("\a\e[1;91mERRORE! nome vuoto o fuori dal range MAX (%d)!\e[0m\n", MAXLUN);
				printf("Inserisci il nome della squadra n.%d: ", i+1);
				gets(temp);
		}
		strcpy(nomiS[i], temp);
		for (j=0; j<giocatori; j++) {	//CICLO PER GLI X GIOCATORI PRESENTI IN OGNI SQUADRA
			//----cognome giocatore----
			printf("Inserisci il cognome del giocatore n.%d: ", j+1);
			gets(temp);
			while ((strlen(temp) > MAXLUN) || (strlen(temp) == 0)) {
				printf("\a\e[1;91mERRORE! cognome vuoto o fuori dal range MAX (%d)!\e[0m\n", MAXLUN);
				printf("Inserisci il cognome del giocatore n.%d: ", j+1);
				gets(temp);
			}
			strcpy(nomiG[k], temp);
			//----numero di maglia e gol segnati/subiti----
			if (j==0) { //SE E' IL PRIMO GIOCATORE INSERITO --> (POR)
				//numero di maglia
				printf("Numero assegnato automaticamente 1 (POR)\n");
				numeri[k] = 1;
				//gol subiti
				printf("Inserisci il numero di gol subiti: ");
				scanf("%d", &golTemp);
				flag = controlloGol(golTemp);
				while (flag != 0) {
					printf("Inserisci il numero di gol subiti: ");
					scanf("%d", &golTemp);
					flag = controlloGol(golTemp);
				}
				gol[k] = golTemp;			
			} else { //SE NON E' IL PRIMO GIOCATORE INSERITO --> (DIF) / (CC) / (ATT)
				//numero di maglia
				printf("Inserisci il numero di maglia per il giocatore %s: ", nomiG[k]);
				scanf("%d", &numTemp);
				flag = controlloNum(numTemp, i, numeri);
				while (flag != 0) {
					printf("Inserisci il numero di maglia per il giocatore %s: ", nomiG[k]);
					scanf("%d", &numTemp);
					flag = controlloNum(numTemp, i, numeri);
				}
				while(getchar() != '\n');
				numeri[k] = numTemp;
				//gol segnati
				printf("Inserisci il numero di gol segnati: ");
				scanf("%d", &golTemp);
				flag = controlloGol(golTemp);
				while (flag != 0) {
					printf("Inserisci il numero di gol segnati: ");
					scanf("%d", &golTemp);
					flag = controlloGol(golTemp);
				}
				gol[k] = golTemp;	
			}
			while(getchar() != '\n');
			k++; //incremento il totale dei giocatori registrati
		} //CHIUDO IL CICLO PER GLI X GIOCATORI
	} //CHIUDO IL CICLO PER LE N SQUADRE
}
//-----------------------------------------------------------------------------------------------------------------------------------
int controlloNum(int temp, int squadra, int numeri[]) {
	int i, val=0, min=2, max=11, inizioSq, fineSq;
	inizioSq = squadra * MAXGIOCATORI; fineSq = inizioSq + 6; //punti di inizio e di fine della squadra in cui sto controllando il num
	if (temp < min || temp > max) {		//controllo il range
		printf("\a\e[1;91mNumero fuori range! (%d-%d)\e[0m\n", min, max);
		val++;
	}
	for (i=inizioSq; i<fineSq; i++) { //controllo che non si ripeta all'interno della stessa squadra
		if( temp == numeri[i]) {
			printf("\a\e[1;91mNumero già presente in questa squadra!\e[0m\n");
			val++;
		}
	}
return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int controlloGol(int num) {
	int val=0;
	if (num < 0) { //controllo che non sia inferiore a 0
		printf("\a\e[1;91mIl numero di gol segnati o subiti non può essere inferiore a 0!\e[0m\n");
		val++;
	}
	if (num > 50) { //controllo che non sia maggiore di 50
		printf("\a\e[1;91mNumero di gol un po' troppo alto ;) !\e[0m\n");
		val++;
	}
return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
void stampaDati(int squadre, int giocatori, char nomiS[][MAXLUN], char nomiG[][MAXLUN], int numeri[], int gol[]) {
	int i, j, k=0, golDIF, golCC, golATT, golTot, golSubiti, min=999, pos;
	system("clear");
	//CICLO PER LE N SQUADRE
	for (i=0; i<squadre; i++) {
		golDIF=0; golCC=0; golATT=0;
		printf("\e[0;94m");
		printf(" ________________________________________________________________________\n");
		printf("|                                                                        |\n");
		printf("|                             SQUADRA: %d                                 |\n", i+1);
		printf("|________________________________________________________________________|\n");
		printf("\e[1;92mNome squadra: %s\n\e[0m", nomiS[i]);
		//PORTIERE (POR)
		printf("Maglia: %d | Cognome: %s | Gol subiti: %d | (POR)\n", numeri[k], nomiG[k], gol[k]);
		golSubiti = gol[k];
		k++;
		//ALTRI GIOCATORI (DIF) / (CC) / (ATT)
		for (j=1; j<giocatori; j++) {
			printf("Maglia: %d | Cognome: %s | Gol segnati: %d | ", numeri[k], nomiG[k], gol[k]);
			//assegno il ruolo in base al numero di maglia e incremento i parziali dei gol
			if (numeri[k] > 1 && numeri[k] < 4) {
				printf("\e[0;92m(DIF)\e[0m\n");
				golDIF += gol[k];	//incremento i gol dei DIF
			} else if (numeri[k] > 3 && numeri[k] < 7) {
				printf("\e[0;93m(CC)\e[0m\n");
				golCC += gol[k];	//incremento i gol dei CC
			} else {
				printf("\e[0;91m(ATT)\e[0m\n");
				golATT += gol[k];	//incremento i gol degli ATT
			}
			k++;
		}
		golTot = golDIF + golCC + golATT;
		printf("Gol totali: %d (\e[0;92mDIF: %d\e[0m | \e[0;93mCC: %d\e[0m | \e[0;91mATT: %d\e[0m)\n", golTot, golDIF, golCC, golATT);
		if (golSubiti < min) {
			min = golSubiti;
			pos = i;
		}
	}
	printf("\nLa squadra che ha subito meno gol (%d) è: %s\n", min, nomiS[pos]);
}
