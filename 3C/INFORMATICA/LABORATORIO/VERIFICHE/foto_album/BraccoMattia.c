/*
Bracco Mattia 3C 05/10/2021
Verifica di info
*/
#include <stdio.h>
int main(){

	float TOTALEFOTO, X, Y, TOTALEX, TOTALEY, TOTALEALBUM, COSTOMEDIO, RISPARMIO;
	
	printf("inserire numero foto in bianco e nero \n");
	scanf("%f", &X);
	
	printf("inseriere numero foto a colori \n");
	scanf("%f", &Y);
	
	TOTALEFOTO=((X*0.15)+(Y*0.80));
	TOTALEX=(X*0.15);
	TOTALEY=(Y*0.80);
	TOTALEALBUM=(10+TOTALEFOTO);
	COSTOMEDIO=(TOTALEFOTO/(X+Y));
	RISPARMIO=(TOTALEFOTO-((X+Y)*0.15));
	
	printf("COSTO TOTALE FOTO: %.2f\n", TOTALEFOTO);
	printf("COSTO TOTALE FOTO IN BIANCO E NERO: %.2f\n", TOTALEX);
	printf("COSTO TOTALE FOTO A COLORI: %.2f\n", TOTALEY);
	printf("COSTO TOTALE ALBUM: %.2f\n", TOTALEALBUM);
	printf("COSTO MEDIO: %.2f\n", COSTOMEDIO);
	printf("RISPARMIO CON TUTTE LE FOTO IN BIANCO E NERO: %.2f\n", RISPARMIO);

return 0;
}

