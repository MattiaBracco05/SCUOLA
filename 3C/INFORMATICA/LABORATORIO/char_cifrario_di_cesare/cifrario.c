/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	
	int chiave;
	char let1=0, let2=0, let3=0, let4=0;
	
	printf("inserire una parola di 4 lettere in minusciolo: ");
	let1=getchar();
	let2=getchar();
	let3=getchar();
	let4=getchar();
	while(getchar()!='\n'); //azzero il buffer della tastiera
		
	while((let1 < 'a' || let1 > 'z') || (let2 < 'a' || let2 > 'z') || (let3 < 'a' || let3 > 'z') || (let4 < 'a' || let4 > 'z')) {
		printf("le lettere devono essere minuscole !, reinserisci: ");
		let1=getchar();
		let2=getchar();
		let3=getchar();
		let4=getchar();
		while(getchar()!='\n'); //azzero il buffer della tastiera
	}
	
	printf("parola in MAIUSCOLO: ");
	printf("%c%c%c%c \n", let1-32, let2-32, let3-32, let4-32);
	
	printf("inserisci una chiave di codifica: ");
	scanf("%d", &chiave);
	
	printf("parola cittografata: %c%c%c%c \n", let1+chiave, let2+chiave, let3+chiave, let4+chiave);
return 0;
}
