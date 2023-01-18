/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	int nCARAMELLE, nBARRETTE, nGELATO;
	float pCARAMELLE, pBARRETTE, pGELATO, TOTALE, SOLDI, RESTO;
	
	printf("inserire il numero di caramelle \n");
	scanf("%d", &nCARAMELLE);
	
	printf("inserire il numero di barrette al cioccolato \n");
	scanf("%d", &nBARRETTE);
	
	printf("inserire il numero di gelati \n");
	scanf("%d", &nGELATO);
	
	pCARAMELLE = 0.50;
	pBARRETTE = 2.50;
	pGELATO = 3.00;
	
	TOTALE = (nCARAMELLE * pCARAMELLE) + (nBARRETTE * pBARRETTE) + (nGELATO * pGELATO);
	
	if (TOTALE == 0){
		printf("Luigino !, Non hai comprato niente, ritorna dentro ! \n");
	}
	
	else{
    	printf("inserire i soldi che Luigino ha in tasca \n");
    	scanf("%f", &SOLDI);
    	
        if (TOTALE > SOLDI){
        printf("Lugino, hai comprato troppa roba, non hai abbastanza soldi\n");
        }
        
        else{
        RESTO = SOLDI - TOTALE;
        printf("a Luigino restano € : %.2f\n", RESTO);
        }
	}

return 0;
}
