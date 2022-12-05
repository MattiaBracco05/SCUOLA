/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 15

//PROTOTIPI
void caricaVettore(char[]);
void stampaVettore(char[]);

int main() {
	char nome[MAX+1]; //devo mettere +1 rispetto al MAX definito precedentemente !
	
	caricaVettore(nome);
	stampaVettore(nome);


return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------
void caricaVettore(char vett []) {
	printf("Come ti chiami?: ");
	gets(vett);
}
//-----------------------------------------------------------------------------------------------------------------------------------
void stampaVettore(char vett[]) {
	system("clear");
	printf("--Metodo printf--\n");
	printf("Buongiorno, %s!\n", vett);
	printf("\n");
	printf("--Metodo puts--\n");
	printf("Buongiorno, ");
	puts(vett); //non devo mettere il "\n", la puts manda a capo in automatico
}
