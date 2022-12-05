/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main(){
	
	int LATO1, LATO2, LATO3;

	printf("inserire valore LATO 1: \n");
	scanf("%d", &LATO1);
	printf("inserire valore LATO 2: \n");
	scanf("%d", &LATO2);
	printf("inserire valore LATO 3: \n");
	scanf("%d", &LATO3);
		
	if( (LATO1 < (LATO2 + LATO3)) && (LATO2 < (LATO1 + LATO3)) && (LATO3 < (LATO1 + LATO2)) ){

		if( (LATO1 == LATO2) && (LATO2 == LATO3) ){
			printf("è un triangolo equilatero \n");
		}
		else{
			if( (LATO1 != LATO2) && (LATO2 != LATO3) && (LATO1 != LATO3) ){
				printf("il triangolo è scaleno \n");
			}
			else{
				printf("il triangolo è iscoscele \n");
            }
			
			//VERIFICO SE IL TRIANGOLO SCALENO O ISCOSCELE È ANCHE RETTANGOLO
			if( ((LATO1 * LATO1) < ((LATO2 * LATO2) + (LATO3 * LATO3))) && ((LATO2 * LATO2) < ((LATO1 * LATO1) + (LATO3 * LATO3))) && ((LATO3 * LATO3) < ((LATO1 * LATO1) + (LATO2 * LATO2))) ) {
				printf("il triangolo è di tipo rettangolo \n");
			}
			else{
				printf("il triangolo non è di tipo rettangolo \n");
            }
		}
	}
	else {
	printf("non è un triangolo ! \n");
	}

return 0;
}
