/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

	int studenti=0, altezza, fascia, fascia1=0, fascia2=0, i=0;
	
	while((studenti < 4) || (studenti > 26)){
		printf("inserire numero studenti (tra 4 e 26) \n");
		scanf("%d", &studenti);
	}
	
	for(i=0; i < studenti; i++){
		fascia=rand()%1;
		
		if(fascia == 0){
			altezza=rand()%32+150;
		}
		if(fascia == 1){
			altezza=rand()%12+178;
		}
		
		printf("%d\n", altezza);
		
		if(altezza < 190){
			fascia1 = fascia1 + 1;
		}
		else{
			fascia2 = fascia2 + 1;
		}
	}
	
	printf("n studenti fascia 1 (150 - 182): %d \n", fascia1);
	printf("n studenti fascia 2 (190 - 201): %d \n", fascia2);
	
	if(fascia1 > fascia2){
		printf("la fascia maggiore è la 1 (150 - 182) \n");
	}
	else{
		printf("la fascia maggiore è la 2 (190 - 201) \n");
	}

return 0;
}
