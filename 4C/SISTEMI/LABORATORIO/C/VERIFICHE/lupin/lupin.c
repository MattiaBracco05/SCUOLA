//Bracco Mattia 4C - Aresnio Lupin

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <sys/wait.h>
#define MIN_BOTTINO 25
#define MAX_BOTTINO 100
#define MIN_NUM 1
#define MAX_NUM 6
#define INCREMENTO 10
#define RIDUZIONE 20

//PROTOTIPI
int chiediN();
int insNum();

int main() {
	
	int bottino, uscita=0, val, num, num1, num2, somma, i=0, stato_wait;
	pid_t chiSono, pid;
	srand(time(NULL));
	
	printf("Il gioco consiste nel sottrarre il bottino di Lupin, l'ispettore vince se la somma dei numeri sono pari mentre Lupin vince se la somma dei numeri è dispari\n");
	printf("\n");
	bottino = chiediN();
	printf("Il valore iniziale del bottino è di: %d\n", bottino);
	
	//ciclo finche l'utente non decide di smettere di giocare
	while (uscita == 0) {
		printf("\e[0;94m");
		printf(" __________________________ \n");
		printf("|                          |\n");
		printf("|Round: %d                  |\n", i+1);
		printf("|__________________________|\n");
		printf("\e[0m");
		//creo il processo figlio
		if ((chiSono = fork()) < 0) {
			printf("Errore nella creazione della fork()!\n");
			exit(-1);
		}
		if (chiSono == 0) {
			num = insNum();
			printf("Processo figlio (PID: %d), numero inserito: %d\n", getpid(), num);
			exit(num);
		}
		//chiudo il processo figlio
		pid = wait(&stato_wait);
		num1 = (stato_wait >> 8);
		num2 = rand()%(MAX_NUM - MIN_NUM + 1) + MIN_NUM;
		printf("Numero generato da Lupin: %d\n", num2);
		//determino chi vince il round
		somma = num1 + num2;
		if ((somma % 2) == 0) {
			printf("\n\e[0;92mLa somma dei numeri (%d) è pari, vince l'ispettore! (-%d al bottino di Lupin)\e[0m\n", somma, RIDUZIONE);
			bottino = bottino - RIDUZIONE;
		}
		else {
			printf("\n\e[0;91mLa somma dei numeri (%d) è dispari, vince Lupin! (+%d al bottino di Lupin)\e[0m\n", somma, INCREMENTO);
			bottino = bottino + INCREMENTO;
		}
		if (bottino <= 0) {
			printf("Lupin ha esaurito il suo bottino!, VINCE L'ISPETTORE!\n");
			uscita = 1;
		}
		else {
			printf("Il nuovo bottino è di: %d\n", bottino);
		}
		
		//chiedo se l'utente vuole continuare a giocare (1) o se vuole uscire (0)
		if (uscita != 1) { //controllo che l'uscita non sia già impostata a 1 (a causa del bottino <= 0) --> in questo caso salto la richiesta all'utente
			printf("\n\e[0;94mInserisci 0 per teminare, 1 per continuare a giocare: \e[0m");
			scanf("%d", &val);
			if (val == 0) {
				printf("Termino di giocare!\n\e[0;93mIl bottino finale di Lupin è di: %d\e[0m\n", bottino);
				uscita = 1;
			}
			else {
				system("clear"); //pulisco lo schermo dopo ogni round
			}
		}
		i++;
	}

return 0;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int chiediN() {
	int val=0;
	while (val < MIN_BOTTINO || val > MAX_BOTTINO)	 {
		printf("Quanto grande vuoi che sia il tuo bottino di partenza? (%d-%d): ", MIN_BOTTINO, MAX_BOTTINO);
		scanf("%d", &val);
	}
return val;
}
//-----------------------------------------------------------------------------------------------------------------------------------
int insNum() {
	int val=0;
	while (val < MIN_NUM || val > MAX_NUM)	 {
		printf("Inserire un numero da giocare (%d-%d): ", MIN_NUM, MAX_NUM);
		scanf("%d", &val);
	}
return val;
}
