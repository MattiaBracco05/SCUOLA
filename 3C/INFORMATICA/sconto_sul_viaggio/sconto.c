/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	int PERSONE;
	float QUOTA, TOTALE, IMPORTO, DIFFERENZA, sconto1, sconto2, sconto3;
	
	printf("inserire prezzo quota \n");
	scanf("%f", &QUOTA);
	
	printf("inserire numero persone \n");
	scanf("%d", &PERSONE);
	
	TOTALE = QUOTA * PERSONE;
	
	sconto1 = 10;
	sconto2 = 7;
	sconto3 = 2;
	
	if(QUOTA > 500){
		IMPORTO = TOTALE - ((TOTALE * sconto1) / 100);
		DIFFERENZA = TOTALE - IMPORTO;
		printf("ho fatto uno sconto del %.2f %% e quindi ho scalato %.2f € \n", sconto1, DIFFERENZA);
		printf("l' importo totale è di: %.2f € \n", IMPORTO);
	}
	
	else{
	
		if(QUOTA > 300){
			IMPORTO = TOTALE - ((TOTALE * sconto2) / 100);
			DIFFERENZA = TOTALE - IMPORTO;
			printf("ho fatto uno sconto del %.2f %% e quindi ho scalato %.2f € \n", sconto2, DIFFERENZA);
			printf("l' importo totale è di: %.2f € \n", IMPORTO);
		}
		
		else{
			IMPORTO = TOTALE - ((TOTALE * sconto3) / 100);
			DIFFERENZA = TOTALE - IMPORTO;
			printf("ho fatto uno sconto del %.2f %% e quindi ho scalato %.2f € \n", sconto3, DIFFERENZA);
			printf("l' importo totale è di: %.2f € \n", IMPORTO);
		}
	}
	
return 0;
}
