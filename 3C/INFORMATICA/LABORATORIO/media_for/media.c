/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

	int Stud=0, somma=0, voto, i;
	float media=0.0;

	srand(time(NULL));	

	printf("Quanti studenti ? ");
	scanf("%d", &Stud);
	
	for(i=0; i < Stud; i++){
		voto=rand()%9+2;
		printf("%d\n", voto);
		somma = somma + voto;
	}	
	
	media = somma / Stud;
	
	printf("la media vale: %.2f \n", media);

return 0;
}
