/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	
	int CONTANTI;
	float PREZZO, TOTALE, IMPORTO, Sconto1, Sconto2;
	
	Sconto1 = 6;
	Sconto2 = 2;
	
	printf("inserire prezzo prodotto: \n");
	scanf("%f", &PREZZO);
	
	if(PREZZO > 3000){
		TOTALE = PREZZO - ((PREZZO * Sconto1) / 100);
	}
	
	else{
		TOTALE = PREZZO;
	}
	
	printf("il totale è di: %.2f € \n", TOTALE);
	
	printf("si desidera pagare in contanti ?  1 = si, 0 = no \n");
	scanf("%d", &CONTANTI);
	
	if(CONTANTI == 1){
		IMPORTO = TOTALE - ((TOTALE * Sconto2) / 100);
	}
	
	else{
		IMPORTO = TOTALE;
	}
	
	printf("l' importo totale è di : %.2f € \n", IMPORTO);
	
return 0;
}
