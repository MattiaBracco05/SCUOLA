#include <stdio.h>

//prototipi
void split_time(long int, int *, int *, int *);

//main
int main() {

	long int secondiTrascorsi = 0;
	int h, m, s;
	
	printf("Inserire i secondi trascorasi dalle 00:00: ");
	scanf("%ld", &secondiTrascorsi);
	
	while(secondiTrascorsi > 86400) {
		printf("In un giorno ci sono 86400s, tu hai inserito un valore maggiore ! \n");
		printf("Inserisci i secondi trascorsi dalle 00:00: ");
		scanf("%ld", &secondiTrascorsi);
	}
	
	split_time(secondiTrascorsi, &h, &m, &s);
	printf("%dh %dm %ds \n", h, m, s);

return 0;
}

//void per calcolare l' orario
void split_time(long int input, int *ore, int *minuti, int *secondi) {
	*ore = input / 3600;
	*minuti = (input - ((*ore) * 3600)) / 60;
	*secondi = input - (((*ore) * 3600) + ((*minuti) * 60));
}
