/*
Bracco Mattia 3C
correzzione verifica FILA B (esercizio foto a colori e bianco e nero)
*/

#include <stdio.h>
int main(){
	float prezzoBN, prezzoC, X, Y, CostoFoto, TotaleAlbum, CostoBN, CostoC, CostoMedio, Risparmio;

	printf("inserire numero foto in bianco e nero \n");
	scanf("%f", X);
	
	printf("inserire numero foto a colori \n");
	scanf("%f", Y);
	
	Costo_BN = 0.15;
	Costo_C = 0.80;
	
	CostoFoto= ((X * prezzoBN)(Y * prezzoC));
	CostoBN = (X * prezzoBN);
	CostoC = (Y* prezzoC);
	TotaleAlbum = (10 + CostoFoto);
	CostoMedio = (CostoFoto / (X + Y));
	Risparmio = (CostoFoto(X + Y) * 0.15));
	
	printf("costo totale delle foto: %f\n", CostoFoto);
	printf("costo foto in bianco e nero: %f\n", CostoBN);
	printf("costo foto a colori: %f\n", CostoC);
	printf("costo totale album: %f\n", TotaleAlbum);
	printf("costo medio delle foto: %f\n", CostoMedio);
	printf("risparmio con tutte le foto in bianco e nero: %f\n", Risparmio);

return 0;
}
