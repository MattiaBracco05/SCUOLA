#include <stdio.h>


int main() {
	int voti[100], N, i;
	
	printf("Quanti numeri vuoi inserire ?: ");
	scanf("%d",&N);
	//controllo che N non sia maggiore di 100
	
	for(i=0;i<N;i++) {
		printf("Inserisci il voto: ");
		scanf("%d", &voti[i]);
	}
	
	for(i=0;i<N;i++) {
		printf("%d | ", voti[i]);
	}
	printf("\n");
	printf("Valore della cella 5: %d \n", voti[4]);

return 0;
}
