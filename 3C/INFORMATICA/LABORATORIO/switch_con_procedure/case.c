/*
Bracco Mattia 3C
*/

#include <stdio.h>

//PROTOTIPI (vanno sempre prima del main, servono per far riconoscere (prima del main) al compilatore ed evitare errori)
void caseA();
void caseB();
void caseC();
void caseD();

int main() {
	int i=0, num=0 , cont=0;
	char menu=' ', lettera=' ', let=' ';
	
	while(menu!='e' && menu!='E'){
		printf("Menu\nDigitare: \nA. data una lettera, stampare la successiva\nB. data una lettera minuscola, convertirla in maiuscolo\nC. data una lettera stabilire se è una vocale oppure una consonante\nD. dati 8 numeri, contare i positivi\nE. Esci\n");
		scanf("%c",&menu);
		while(getchar()!='\n');
	
	switch(menu){
		case 'A':
		case 'a':
			caseA();
			break;
	
		case 'B':
		case 'b':
			caseB();
			break;
		
		case 'c':
		case 'C':
			caseC();
			break;
		
		case 'd':
		case 'D':
			caseD();
			break;

