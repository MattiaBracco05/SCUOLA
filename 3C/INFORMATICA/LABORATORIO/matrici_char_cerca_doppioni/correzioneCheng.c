#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#include<stdbool.h>
#include<ctype.h>

#define MAX 23

int getInput(int, int, char[]);
void randomAlfaFill(char[][MAX], int, int);
void printMat(char[][MAX], int, int);
void cercad(char[][MAX], int, int);

int main()
{

	char mat[MAX][MAX] = { 0 };

	int col = 0,
		row = 0;

	srand(time(NULL));

	row = getInput(7, 23, "riga");
	col = getInput(7, 23, "colona");

	randomAlfaFill(mat, row, col);
	printMat(mat, row, col);

	cercad(mat, row, col);
	printf("\n");
	printMat(mat, row, col);


	return 0;

}

void cercad(char mat[][MAX], int row, int col) {
int x;

	for (int i = 0; i < row; i++)	{
		for(int j = 0; j < col; j++) 	{
					if(mat[i][j] != '0') {
						bool found = false;			// flag per vedere se ho trovato una corrispondenza 
																				// nella cornice attorno al carattere di partenza
						for(int x = i -1; x <= i +1; x++) {				// ciclo della matrice attorno al caratt.
							if(x >= 0 && x < row) {
								for(int y = j -1; y <= j+1; y++) {
									if(y >= 0 && y < col) {
										if(y != j || x != i) {
											if(mat[i][j] == mat[x][y]) {
												found = true;
											}
										}
									}
								}
							}
						}
						if(found)	{
							for(x = i -1; x <= i +1; x++) {
								if(x >= 0 && x < row) {
									for(int y = j -1; y <= j+1; y++) {							
										if(y >= 0 && y < col) {
											if(y != j || x != i) {
													mat[x][y] = '0';	
											}
										}
									}
								}
							}
						}
					} // chiudo il test se il carattere di partenza != '0'
				} // chiudo qui il ciclo sulle colonne
			} // chiudo qui il ciclo sulle righe
}

void printMat(char mat[][MAX], int row, int col) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			mat[i][j] == '0' ? printf("\x1b[0;30m\x1b[47m[%c]\x1b[0m", mat[i][j]) : printf("[%c]", mat[i][j]);
		}

		printf("\n");

	}

}



void randomAlfaFill(char mat[][MAX], int row, int col) {
	int f, t;
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			f = rand() % 2;
			t = rand() % ('z' - 'a' + 1) + 'a';
			// mat[i][j] = f < 50 ? t : toupper(t);
			if(f==0){
				mat[i][j] = t;
			} else {
				mat[i][j] = toupper(t);
			}
		}
	}
}


int getInput(int min, int max, char t[])
{

	int result = 0;

	printf("Inserisci il valore di %s: ", t);
	scanf("%d", &result);

	while (result > max || result < min)
	{

		if (result > max)
		{

			printf("Il valore di %s non deve essere maggiore di %d, rinserisci: ", t, max);

		}
		else
		{

			printf("Il valore di %s non deve essere minore di %d, rinserisci: ", t, min);

		}

		scanf("%d", &result);

	}

	return result;

}
