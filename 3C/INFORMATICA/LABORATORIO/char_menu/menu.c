/*
Bracco Mattia 3c
*/

#include <stdio.h>

int main(){

    char scelta=0, invio=0, c=0; 
    int exit=0, i, num, totPos=0;

    while(exit==0){
        printf(" ________________________________________________________________________\n");
        printf("|                          MENU DEGLI OPERATORI                          |\n");
        printf("|COMANDO          CHE COSA FA                                            |\n");
        printf("|________________________________________________________________________|\n");
        printf("| A- lettera successiva                                                  |\n");
        printf("| B- minuscolo --> MAIUSCOLO                                             |\n");
        printf("| C- vocale o consonante                                                 |\n");
        printf("| D- contare numeri positivi                                             |\n");
        printf("| E- EXIT                                                                |\n");
        printf("|________________________________________________________________________|\n");
        
        printf("inserire una scelta: ");
        scelta=getchar();
        invio=getchar();
        
        switch(scelta){
        
            case 'a':
            case 'A':
                printf("inserire una lettera: ");
                c=getchar();
                invio=getchar();
                while (c<'a' || c>'y'){
                    printf("errore di inserimento !, inserisci una lettera: ");
                    c=getchar();
                    invio=getchar();
                }
                printf("lettera inserita: %c, lettera successiva: %c \n", c, c+1);
            	break;
            	
            case 'b':
            case 'B':
                printf("inserire una lettera minuscola: ");
                c=getchar();
                invio=getchar();
    	        while (c<'a' || c>'z'){
                    printf("errore di inserimento !, inserisci una lettera minuscola: ");
                    c=getchar();
                    invio=getchar();
    	        }
                printf("lettera minuscola: %c lettera maiuscola: %c \n", c, c-32);
            	break;
            	
            case 'c':
            case 'C':
                printf("inserire una lettera: ");
                c=getchar();
                invio=getchar();
                if (c== 'A' || c== 'E' || c== 'I' || c== 'O' || c== 'U' || c== 'a' || c== 'e' || c== 'i' || c== 'o' || c== 'u'){
                    printf("la lettera è una vocale \n");
                } else{
                    printf("la lettera è una consonante \n");
                }
            	break;
            	
            case 'd':
            case 'D':
                for (i=0; i<8; i++){
                    printf("inserire il %d° numero: ", i+1);
                    scanf("%d", &num);
                    invio=getchar();
                    if (num >= 0){
                        totPos++;
                    }
                }
                printf("in totale ci sono %d numeri positivi \n", totPos);
            break;
            
            case 'e':
            case 'E':
                exit=1;
                printf("esco dal programma ! \n");
            	break;
            	
            default:
                printf("errore !, è stato inserito un operatore non valido \n");
        }
    }
return 0;
}
