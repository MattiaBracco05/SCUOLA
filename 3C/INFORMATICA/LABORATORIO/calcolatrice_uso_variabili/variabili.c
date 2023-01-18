/*
Bracco Mattia 3C
dati 2 numeri, calcolare e stampare a video: somma, differenza, moltiplicazione, divisione con resto, divisione con virgola, N1 cambiato di segno, N2 cambiato di segno, potenza N1^N2
*/

#include <stdio.h>

int main() {
	//dichiarazioni delle variabili
	int N1, N2, Somma, Differenza, Moltiplicazione, Divisione, Resto, n1, n2, Potenza, potenza, contatore;
	
	
	printf("Inserire il primo numero: \n");
	scanf("%d",&N1);
	
	printf("Inserire il secondo numero: \n");
	scanf("%d",&N2);
	
	Somma=N1+N2;
	Differenza=N1-N2;
	Moltiplicazione=N1*N2;
	Divisione=N1/N2;
	
	float c = 0.0; c = (float)N1/N2;
	
	Resto=N1-(Divisione*N2);
	n1=-(N1);
	n2=-(N2);
	Potenza = 1;
	contatore = 0;

/*
utilizzo un ciclo while per calcolare la potenza dove finche la variabile contatore è minore di N2 (l' esponente) stabilisce il valore di Potenza come N1 (base) *Potenza e aumenta la variabile contatore di 1 (contatore=contatore+1)
*/

	while(contatore < N2)
	{
	Potenza=N1*Potenza;
	contatore=contatore+1;
	}
	
	printf("risultato somma: %d\n", Somma);
	printf("risultato differenza: %d\n", Differenza);
	printf("risultato moltiplicazione: %d\n", Moltiplicazione);
	printf("risultato divisione: %d\n", Divisione);
	printf("valore resto: %d\n", Resto);
	printf("valore divisione in decimale: %f\n", c);
	printf("variabile N1 cambiata di segno: %d\n", n1);
	printf("variabile N2 cambiata di segno: %d\n", n2);
	printf("risultato potenza: %d\n", Potenza);
return 0;
}
