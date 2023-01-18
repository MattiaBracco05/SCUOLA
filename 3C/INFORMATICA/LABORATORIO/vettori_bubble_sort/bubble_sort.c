/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//AREA DEI PROTOTIPI
int CreaNumero(int, int);
int ChiediN(int, int);
void CaricaVettore(int, int []);
void StampaVettore(int, int []);
void BubbleSort(int, int []);

int main() {
	srand(time(NULL));
	int numeri[20], N;

	N = ChiediN(1,20);
	CaricaVettore(N, numeri);

	printf("--NON ORDINATI--\n");
	StampaVettore(N, numeri);

	BubbleSort(N, numeri);

	printf("--ORDINATI--\n");
	StampaVettore(N, numeri);
	

return 0;
}

//------------------------------------------------------------------------------------------------------------------------------------
int CreaNumero(int min, int max) {
return rand()%(max-min+1)+min;
}
//------------------------------------------------------------------------------------------------------------------------------------
int ChiediN(int min, int max) {
	int n=0;
	while(n<min || n>max) {
		printf("Quanti numeri vuoi che il random inserisca nel vettore ? (%d-%d): ", min, max);
		scanf("%d",&n);	
	}
return n;
}
//------------------------------------------------------------------------------------------------------------------------------------
void CaricaVettore(int N, int vett[]) {
	int i;
	for(i=0; i<N; i++) {
		vett[i] = CreaNumero(1,100);	
	}
}
//------------------------------------------------------------------------------------------------------------------------------------
void StampaVettore(int N, int vett[]) {
	int i;
	for(i=0; i<N; i++) {
		printf("%d\t", vett[i]);	
	}
	printf("\n");
}
//------------------------------------------------------------------------------------------------------------------------------------
void BubbleSort(int N, int vett[]) {
	int j, i, flag, TMP;

	j = N;
	flag = 1; //1 => TRUE, 0 => FALSE
	while(flag == 1) {
		flag = 0;	
		for(i=0; i<j; i++) {
			if(vett[i] > vett[i+1])	{
				TMP = vett[i];
				vett[i] = vett[i+1];
				vett[i+1] = TMP;
				flag = 1;		
			}	
		}
		j--;	
	}


}
