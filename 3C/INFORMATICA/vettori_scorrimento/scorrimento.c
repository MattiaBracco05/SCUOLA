/*
Bracco Mattia 3C
*/

#include <stdio.h>


int main() {
	int N=0, i;
	float numeri[50];

	while(N < 1 || N > 50) {
		printf("Quanti numeri vuoi inserire ? (max 50): ");
		scanf("%d",&N);
	}
	
	for(i=0; i<N; i++) {
		printf("Inserisci il numero: ");
		scanf("%f", &numeri[i]);
	}
	
	for(i=0; i<N; i++) {
		printf("%.2f | ", numeri[i]);
	}

	printf("\nIl vettore rovesciato contiene i seguenti elementi:\n");
	for(i=N; i>0; i--) {
		printf("%.2f | ", numeri[i-1]);
	}
	printf("\n");	

return 0;
}
