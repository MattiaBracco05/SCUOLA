/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	float PREZZO, TOTALE, sconto1, sconto2, SPESA;
	int PEZZI;
	
	printf("inserire prezzo prodotto \n");
	scanf("%f", &PREZZO);
	
	printf("inserire numero pezzi \n");
	scanf("%d", &PEZZI);
	
	sconto1=5;
	sconto2=10;
	
	TOTALE = PREZZO * PEZZI;
	
	if(PEZZI>10){
		SPESA = TOTALE - ((TOTALE * sconto2) / 100);
	}
    
    else{
    	SPESA = TOTALE -((TOTALE * sconto1) / 100);
    }
    
    printf("spesa totale: %.2f €\n", SPESA);
return 0;
}

