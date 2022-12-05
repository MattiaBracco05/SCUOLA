/*
Bracco Mattia 3C
data la base e l' altezza di un rettangolo, calcolare e stampare a video l' area e il perimtro
*/

#include <stdio.h>

int main() {
	//dichiarazioni variabili
	int B, H, Area, Perimetro;
	
	printf("Inserire valore base: \n");
	scanf("%d",&B);
	
	printf("Inserire valore altezza: \n");
	scanf("%d",&H);
	
	Area=B*H;
	Perimetro=B+H+B+H;
	
	printf("L' area di %d e %d vale: %d\n",B, H, Area);
	printf("Il perimetro di %d e %d vale: %d\n",B, H, Perimetro);
	
return 0;
}									
