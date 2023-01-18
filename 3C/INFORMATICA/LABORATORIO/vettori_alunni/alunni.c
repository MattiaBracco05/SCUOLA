/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 26

//PROTOTIPI
int creaNumero(int, int);
int chiediN(int, int);
void insIniziale(int, char[]);
void assegnaVoti(int, int[], int[], int[], int[]);
void stampaVoti(int, char[], int[], int[], int[], int[]);
void mediaVotiAlunno(int, char[], int[], int[], int[], int[]);
void mediaUguale(int, float[], char[]);
void mediaVotiMateria(int, int[], int[], int[], int[]);

int main() {
	int N;
	int informatica[MAX], sistemi[MAX], italiano[MAX], matematica[MAX];
	char inizialiAlunni[MAX];

	srand(time(NULL));

	N = chiediN(6,26);
	insIniziale(N, inizialiAlunni);
	assegnaVoti(N, informatica, sistemi, italiano, matematica);
	stampaVoti(N, inizialiAlunni, informatica, sistemi, italiano, matematica);
	mediaVotiAlunno(N, inizialiAlunni, informatica, sistemi, italiano, matematica);
	mediaVotiMateria(N, informatica, sistemi, italiano, matematica);

return 0;
}
//------------------------------------------------------------------------------------------------------------------------------------
int creaNumero(int min, int max) {
	int num;
	num = rand()%(max-min+1)+min;
return num;
}
//------------------------------------------------------------------------------------------------------------------------------------
int chiediN(int min, int max) {
	int n=0;
	while(n<min || n>max) {
		printf("Inserisci il numero di alunni presenti nella classe (%d-%d): ", min, max);
		scanf("%d",&n);	
	}
return n;
}
//------------------------------------------------------------------------------------------------------------------------------------
void insIniziale(int N, char inizialiAlunni[]) {
	int i;
	char ins;

	for(i=0;i<N;i++) {
		ins = '0';
		while(ins<'a' || ins>'z') {
			printf("Inserisci l' iniziale minuscola del %d° alunno: ", i+1);
			while(getchar()!='\n');			
			scanf("%c", &ins);		
		}
		inizialiAlunni[i] = ins;
	}	
}
//------------------------------------------------------------------------------------------------------------------------------------
void assegnaVoti(int N, int info[], int sistemi[], int ita[], int mate[]) {
	int i;
	for(i=0; i<N; i++) {
		info[i] = creaNumero(2,10);
		sistemi[i] = creaNumero(2,10);
		mate[i] = creaNumero(2,10);
		ita[i] = creaNumero(2,10);
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void stampaVoti(int N, char alunni[], int info[], int sistemi[], int ita[], int mate[]) {
	int i;
	for(i=0; i<N; i++) {
		printf("\e[1;94m--Alunno: %c%d--\e[0m\n", alunni[i], i+1);
		printf("Voto informatica: %d | Voto sistemi: %d\n", info[i], sistemi[i]);
		printf("Voto italiano: %d | Voto matematica: %d\n", ita[i], mate[i]);
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void mediaVotiAlunno(int N, char alunni[], int info[], int sistemi[], int ita[], int mate[]) {
	int somma, i;
	float media[26];
	printf("\n");
	for(i=0; i<N; i++) {
		somma = info[i] + sistemi[i] + ita[i] + mate[i];
		media[i] = somma / 4;
		printf("\e[1;94mAlunno: %c%d\e[0m media tot: %.2f\n", alunni[i], i+1, media[i]);
	}
	printf("\n");
	mediaUguale(N, media, alunni);
}
//------------------------------------------------------------------------------------------------------------------------------------
void mediaUguale(int N, float media[], char alunni[]) {
	int i, j, f=0;
	printf("\e[1;93mAlunni con medie uguali trovati:\e[0m\n");
	for(i=0; i<N-1; i++) {
		j = i + 1;
		while(j<N) {
			if(media[i] == media[j]) {
				printf("%c%d e %c%d \n", alunni[i], i+1, alunni[j], j+1);
				f++;
			}       
			j++;
		}       
 	}
	if(f == 0) {
		printf("Non ci sono medie uguali\n");
	}
	printf("\n");
}
//------------------------------------------------------------------------------------------------------------------------------------
void mediaVotiMateria(int N, int info[], int sistemi[], int ita[], int mate[]) {
	int sommaInfo=0, sommaSistemi=0, sommaIta=0, sommaMate=0, i;
	float media;
	//sommo i voti della stessa materia
	for(i=0; i<N; i++) {
		sommaInfo = sommaInfo + info[i];
		sommaSistemi = sommaSistemi + sistemi[i];
		sommaIta = sommaIta + ita[i];
		sommaMate = sommaMate + mate[i];
	}
	media = (float) sommaInfo / N;
	printf("La media della classe di \e[1;92minformatica\e[0m è: %.2f\n", media);
	media = (float) sommaSistemi / N;
	printf("La media della classe di \e[1;92msistemi\e[0m è: %.2f\n", media);
	media = (float) sommaIta / N;
	printf("La media della classe di \e[1;92mitaliano\e[0m è: %.2f\n", media);
	media = (float) sommaMate / N;
	printf("La media della classe di \e[1;92mmatematica\e[0m è: %.2f\n", media);
}
