/*
Bracco Mattia 3C
calcolo spesa edilizia
*/
#include <stdio.h>
int main(){

	int	nGhiaia, nCaschi, nBidoni, nCariole;
	float GHIAIA, CASCHI, BIDONI, pCariole, CARIOLE, TOTCARIOLE, SCONTO, IVA, CONSEGNA, SPESA, SPESAIVA;
	
	nGhiaia = 30;
	nCariole = 2;
	nCaschi = 20;
	nBidoni = 15;
	
	pCariole = 50;
	
	CONSEGNA = 50;
	IVA = 22;
	SCONTO = 5;
	
	printf("inserire prezzo totale di n: %d sacchi di ghiaia \n", nGhiaia);
	scanf("%f", &GHIAIA);
	
	printf("inserire prezzo totale di n: %d caschi di sicurezza \n", nCaschi);
	scanf("%f", &CASCHI);
	
	printf("inserire prezzo totale di n: %d bidoni di vernice \n", nBidoni);
	scanf("%f", &BIDONI);
	
	CARIOLE = (nCariole * pCariole);
	TOTCARIOLE = CARIOLE - ((CARIOLE * SCONTO) / 100);
	
	SPESA = (GHIAIA + CASCHI + BIDONI + TOTCARIOLE + CONSEGNA);
	SPESAIVA = SPESA + ((SPESA * IVA) / 100);
	
	printf("la spesa complessiva inclusa di IVA e costo per la consegna è di: %.2f € \n", SPESAIVA);

return 0;
}
