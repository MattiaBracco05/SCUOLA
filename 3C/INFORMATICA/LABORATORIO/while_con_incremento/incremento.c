/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main () {
	
	//area delle dichiarazioni e/o inizializzazioni
	int N=100, i=10, riga=1;
	
	printf("stampo le tabelline: \n");
	
	while(riga <= 10){
		while(i <= N){
			// il "\t" dove t sta per tabulazione, serve per separare i numeri tra di loro		
			printf("%d\t", i);
			i=i+(10*riga);
		}
	printf("\n");

	riga = riga+1;
	i=10*riga;
	N=i*10;
	}

return 0;
}
