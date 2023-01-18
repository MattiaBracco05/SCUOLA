/*
Bracco Mattia 3C
crea le tabelline dall' 1 al 10
*/

#include <stdio.h>

int main () {
	
	//area delle dichiarazioni e/o inizializzazioni
	int N=10, i=1, riga=1;
	
	printf("stampo le tabelline: \n");
	
	while(riga <= 10){
		while(i <= N){
			// il "\t" dove t sta per tabulazione, serve per separare i numeri tra di loro		
			printf("%d\t", i);
			i=i+(1*riga);
		}
	printf("\n");

	riga = riga+1;
	i=1*riga;
	N=i*10;
	}

return 0;
}
