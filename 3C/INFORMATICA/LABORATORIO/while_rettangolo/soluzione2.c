/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()  {

	int i, j, numCol, numRow;
	srand(time(NULL));

	printf("inseire il numero di righe: ");
	scanf("%d", &numRow);
	while(numRow < 3){
		printf("il numero di righe non deve essere inferiore a 3: ");
		scanf("%d", &numRow);
	}

	numCol=rand()%18+3;
	printf("costruisco un rettngolo di %d righe e %d colonne \n", numRow, numCol);

	for(i=1; i<=numCol; i++){
		printf("*");
	}
	printf("\n");
	for(i = 1; i <= (numRow-2); i++){
		printf("*");
		for(j=0; j < (numCol-2); j++){
			printf("q");
		}
		printf("*\n");
	}
	for(i=1; i<=numCol; i++){
		printf("*");
	}
	printf("\n");
return 0;
}
