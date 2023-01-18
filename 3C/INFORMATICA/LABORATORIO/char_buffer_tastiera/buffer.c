/*
Bracco Mattia 3C
*/

#include <stdio.h>

//------------------------------------------------------------------------------------------------------------------------------------
//prototipi
void chiediFrase();
int numero(char,int);
int vocale(char,int);
int consonante(char,int);
int spazio(char,int);
int speciale(char,int);

//------------------------------------------------------------------------------------------------------------------------------------
int main() {
	
	chiediFrase();
	
return 0;
}

//------------------------------------------------------------------------------------------------------------------------------------
void chiediFrase() {
	
	char carattere;	
	int num=0, voc=0, con=0, spa=0, alt=0;
	
	printf("Inserisci una frase: \n");
	
	//finche il carattere è diverso dall' invio prendo il carattere (1 per volta)
	while (carattere != '\n') {
		scanf("%c", &carattere);
	
		//controllo se è un numero
		int numero (char carattere, int num) {

			if (carattere >= '0' && carattere <= '9') {
				num++;
			} 
			
		return num;
		}
	
		//controllo se è una vocale
		int vocale (char carattere, int voc) {
		
			if (carattere == 'a' || carattere == 'e' || carattere == 'i' || carattere == 'o' || carattere == 'u' || carattere == 'A' || carattere == 'E' || carattere == 'I' || carattere == 'O' || carattere == 'U') {
				voc++;
			}
		
		return voc;
		}
		
		//controllo se è una consonante
		int consonante (char carattere, int con) {
			
			if ( (carattere >= 'a' && carattere <= 'z') || (carattere >= 'A' && carattere <= 'Z') ) {
			
				//dopo aver verificato se era una lettera verifico se è una consonante
				if (carattere != 'a' || carattere != 'e' || carattere != 'i' || carattere != 'o' || carattere != 'u') {
					con++;
				}
			}
		return con;
	 	}
	 	
	 	//controllo se è uno spazio
	 	int spazio (char carattere, int spa) {
	 		
	 		if (carattere == ' ') {
	 			spa++;
	 		}
	 		
	 	return spa;
	 	}
	 	
	 	//controllo se è un carattere sepciale
	 	int speciale (char carattere, int alt) {
	 	
	 		if (carattere >= 'a' && carattere <= 'Z' || carattere >= '0' && carattere <= '9' || carattere == ' ') {
	 			//è gia stato classificato
	 		} 
	 		else {
	 			alt++;
	 		}
	 	
	 	return alt;
	 	}
	 	
	 }
	 
	printf("In totale ci sono %d cifre \n", num);
	printf("In totale ci sono %d vocali \n", voc);
	printf("In totale ci sono %d consonanti \n", con);
	printf("In totale ci sono %d spazi \n", spa);
	printf("In totale ci sono %d altri caratteri \n", alt);
}
