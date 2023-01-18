/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#define MAX 10

//PROTOTIPI
void inserisciTesto(char[], int);
void aggiornaDati(char[], int*, int*, int*, int*);
void stampaDati(int, int, int, int);
int main() {

	int max=250, righe=0, parole=0, caratteri=0, caratteriAlfa=0;
	char vettore[max+1];

	system("clear");
	inserisciTesto(vettore, max);

return 0;
}

//------------------------------------------------------------------------------------------------------------------------------------
void inserisciTesto(char vett[], int max) {
	int i=0, exitRighe=0, exitTesto, lunghezza;
	int righe=0, parole=0, caratteri=0, caratteriAlfa=0;
	while(exitRighe == 0 && i<MAX) {
		//inserimento testo
		exitTesto = 0;
		while(exitTesto == 0) {
			printf("Inserisci testo n.%d (MAX %d caratteri): ", i+1, max);
			gets(vett);			
			//controllo lunghezza
			lunghezza = strlen(vett);
			if(lunghezza < max) {
				exitTesto = 1;			
			} else {
				printf("Non devi superare i %d caratteri!\n", max);
			}
		}
		//controllo uscita
		if(vett == "FINE" || vett == "Fine" || vett == "fine") {
			printf("Termino l'inserimento");
			exitRighe = 1;
		} else {
			aggiornaDati(vett, &righe, &parole, &caratteri, &caratteriAlfa);
		}
		i++;
	}
	//stampo i DATI
	stampaDati(righe, parole, caratteri, caratteriAlfa);
}
//------------------------------------------------------------------------------------------------------------------------------------
void aggiornaDati(char vett[], int *righe, int *parole, int *caratteri, int *caratteriAlfa) {
	int l, i;
	//incremento le righe (+1) e i caratteri tot (caratteri + l)
	l = strlen(vett);
	(*righe)++;
	*caratteri = *caratteri + l;
	//conto le parole (guardando gli spazi (" "))
	for(i=0; i<l; i++) {
		if(vett[i] == ' ') {
			(*parole)++;		
		}
	}
	(*parole)++; //ne aggiungo 1 al conteggio dato che l'ultima ha l'invio e non lo spazio!
	//conto i caratteri alfabetici
	for(i=0; i<l; i++) {
		if((vett[i] >= 'a' && vett[i] <= 'z') || (vett[i] >= 'A' && vett[i] <= 'Z')) {
			(*caratteriAlfa)++;		
		}
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void stampaDati(int rig, int par, int car, int carAlfa) {
	printf(" ________________________________________________________________________\n");
	printf("|                          DATI TESTI INSERITI                           |\n");
	printf("|________________________________________________________________________|\n");
	printf("\n");
	printf("Righe inserite: %d\n", rig);
	printf("Parole inserite: %d\n", par);
	printf("Caratteri inseriti: %d\n", car);
	printf("Caratteri alfabetici inseriti: %d\n", carAlfa);
}
