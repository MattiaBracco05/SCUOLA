/*
Bracco Mattia 3C, verifica 16/11/2021
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {

	int scelta, scelta1=0, scelta2=0, scelta3=0, scelta4=0, prezzo1=8, prezzo2=14, prezzo3=25, prezzo4=32, persone=0, acqua, nbott, totbott=0, pbott=2, consegna, consegne=0, pconsegne=5, SPESA, i=0; 
	float perc;	
	srand(time(NULL));	

	while(persone < 5 || persone > 25){
	printf("inserire il numero delle persone (tra 5 e 25): ");
	scanf("%d", &persone);
	}
	
	for (i=0; i<persone; i++){
		printf("scegliere un menù: ");
		scanf("%d", &scelta);
		
		switch(scelta){
			case 1:
				scelta1 = scelta1 + 1;
				break;
			case 2:
				scelta2 = scelta2 + 1;
				break;
			case 3:
				scelta3 = scelta3 + 1;
				break;
			case 4:
				scelta4 = scelta4 + 1;
				break;
			default:
				printf("errore !, scelta non valida \n");
				break;
		}
		
		printf("vuole anche l' acqua ? (0 per no, 1 per si): ");
		scanf("%d",&acqua);
		
		if(acqua==1){
			nbott=random()%8+2;
			totbott = totbott + nbott;
		}
		
		printf("consegna a domicilio ? (1 per no, 2 per si): ");
		scanf("%d", &consegna);

		if(consegna==1){
			consegne = consegne + 1;
		}
	}
	
	SPESA = ((scelta1*prezzo1) + (scelta2*prezzo2) + (scelta3*prezzo3) + (scelta4*prezzo4) + (totbott*pbott) + (consegne*pconsegne));
	printf("il ricavato totale della pizzeria è di: %d € \n", SPESA);	

	printf("in tot %d persone hanno scelto il menù 2 \n", scelta2);
	
	if((scelta1 > scelta2) && (scelta1 > scelta3) && (scelta1 > scelta4)){
		printf("la scelta maggiore è la 1 \n");
	}
	else{
		if((scelta2 > scelta1) && (scelta2 > scelta3) && (scelta2 > scelta4)){
			printf("la scelta maggiore è la 2 \n");
		}
		else{
			if((scelta3 > scelta1) && (scelta3 > scelta2) && (scelta3 > scelta4)){
				printf("la scelta maggiore è la 3 \n");
			}
			else{
				printf("la scelta maggiore è la 4 \n");
			}
		}
	}

	perc = ((consegne * 100) / persone);
	printf("percentuale di consegne: %.2f \n", perc);

return 0;
}
