/*
Bracco Mattia 3C
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//AREA DEI PROTOTIPI
int creaRandom(int, int);
int chiediN();
void quanti(int, int);
void mediaDonne(int, int, int);
void mediaTempo(int, int);
void vincitore(int, int);
void ultimo(int, int);

//MAIN
int main () {

	int N, i, exit=0, insGenere, scelta; //variabili di gestione del main 
	int Npettorale, eta, tempo, donne=0, uomini=0, pettorale1, tempo1=151, pettoraleUltimo, tempoUltimo=79, tempoTOT=0, tempoDonne=0, etaDonne=0;
	char genere;
			
	srand(time(NULL));	

	N = chiediN();
	for (i=0; i<N; i++) {
		printf("\e[0;34m--Partecipante %d-- \n", i+1);

		//numero pettorale
		Npettorale=0;
		while (Npettorale < 1 || Npettorale > 50) {
			printf("\e[0mInserire numero pettorale (1 - 50): ");
			scanf("%d", &Npettorale);
		}

		//età
		eta = creaRandom(10, 50);
		printf("Età (calcolata random): %d \n", eta);
		
		//tempo
		tempo = creaRandom(80, 150);
		printf("Tempo (calcolato random): %d \n", tempo);

		//genere
		insGenere=0;
		while (insGenere == 0) {
			printf("\e[0mInserire il genere (m = Maschio, f = Femmina): ");
			while(getchar()!='\n');
			scanf("%c", &genere);

			if (genere == 'm' || genere == 'M'){
				uomini = uomini + 1;
				tempoTOT = tempoTOT + tempo;
				insGenere = 1;
			}
			else if (genere == 'f' || genere == 'F'){
				donne = donne + 1;
				tempoTOT = tempoTOT + tempo;
				tempoDonne = tempoDonne + tempo;
				etaDonne = etaDonne + eta;
				insGenere = 1;
			}
			else {
				printf("\e[1;31m Operatore non valido ! \n");
				printf("\a");
			}
		}
			
		//verifico se è il 1°
		if (tempo < tempo1) {
			tempo1 = tempo;
			pettorale1 = Npettorale;
		}
		
		//verifico se è l' ultimo
		if (tempo > tempoUltimo) {
			tempoUltimo = tempo;
			pettoraleUltimo = Npettorale;
		}
	}
	
	while(exit==0) {
		printf("\e[0;94m");
		printf(" ________________________________________________________________________\n");
		printf("|                          MENU DEGLI OPERATORI                          |\n");
		printf("|COMANDO          CHE COSA FA                                            |\n");
		printf("|________________________________________________________________________|\n");
		printf("| 0) ESCI                                                                |\n");
		printf("| 1) QUANTI                                                              |\n");
		printf("| 2) VINCITORE                                                           |\n");
		printf("| 3) MEDIA TEMPI                                                         |\n");
		printf("| 4) MEDIA DONNE                                                         |\n");
		printf("| 5) ULTIMO                                                              |\n");
		printf("|________________________________________________________________________|\n");
		printf("Inserire una scelta: ");
		scanf("%d", &scelta);
		
		switch(scelta) {
			case 0:
				printf("\e[1;93m\e[0;100mEsco dal programma ! \e[0m\n");
				printf("\a");  //suono buzzer
				exit=1;
				break;
			case 1:
				quanti(uomini, donne);
				break;
			case 2:
				vincitore(pettorale1, tempo1);
				break;
			case 3:
				mediaTempo(tempoTOT, N);
				break;
			case 4:
				mediaDonne(donne, tempoDonne, etaDonne);
				break;
			case 5:
				ultimo(pettoraleUltimo, tempoUltimo);
				break;
			default:
				printf("\e[1;31mOperatore non valido ! \n");
				printf("\a");
		}
	}
	
return 0;
}

//----------------------------------------------------------------------------------------------------------------------------------
int creaRandom (int min, int max) { return rand()%(max-min+1)+min; }

//----------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int persone=0;
	while(persone < 1 || persone > 50) {
		printf("\e[0mInserire il numero di partecipanti (1 - 50): ");
		scanf("%d", &persone);
	}
return persone;
}
		
//------------------------------------------------ ---------------------------------------------------------------------------------
void quanti(int M, int F ) {
    printf("\e[0mIn totale hanno partecipato %d atleti uomini e %d atlete donne \n", M, F);
}

//------------------------------------------------ ---------------------------------------------------------------------------------
void mediaTempo(int sommaTempo, int atleti) {
    float media;
    media = sommaTempo / atleti;
    printf("\e[0mIl tempo medio è di %.2f minuti \n", media);
}

//----------------------------------------------------------------------------------------------------------------------------------
void mediaDonne(int donne, int tempoDonne, int etaDonne) {
    float etaMedia, tempoMedio;
    tempoMedio = tempoDonne / donne;
    etaMedia = etaDonne / donne;
    printf("\e[0mIl tempo medio delle donne è %.2f minuti, l' età media è: %.2f \n", tempoMedio, etaMedia);
}

//----------------------------------------------------------------------------------------------------------------------------------
void vincitore(int p1, int t1) {
    printf("\e[0mIl vincitore ha il pettorale n° %d ed ha concluso la gara con un tempo di %d minuti \n", p1, t1);
}

//----------------------------------------------------------------------------------------------------------------------------------
void ultimo(int pU, int tU) {
    printf("\e[0mL' ultimo atleta ha il pettorale n° %d ed ha concluso la gara con un tempo di %d minuti \n", pU, tU);
}
