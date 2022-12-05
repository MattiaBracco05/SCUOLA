/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

//PROTOTIPI
void cifraTesto(char[], char[], char[]);

int main(){
	int i,n,c;
	char text[MAX], key[MAX], result[MAX];
	
	system("clear");
	printf("Inserisci la frase senza spazi: ");
	gets(text);
	printf("Inserisci la lettera da usare come chiave: ");
	gets(key);
	
	cifraTesto(text, key, result);
	
	system("clear");
	printf("Testo inserito: %s\n", text);
	printf("Chiave utilizzata: %s\n", key);
	printf("Testo criptato: %s\n",result);

return 0;
}

void cifraTesto(char testo[], char chiave[], char testoCifrato[]) {
	int i = 0, j = 0, spostamento=0;
	
	while (i < strlen(testo)) {
		if (j == strlen(chiave)) {
			j=0;
		}
		spostamento = ((testo[i] - 'a') + (chiave[j] - 'a')) % 26;
		testoCifrato[i] = 'a' + spostamento;
		j++;
		i++;
	}
	testoCifrato[i] = '\0';
}
