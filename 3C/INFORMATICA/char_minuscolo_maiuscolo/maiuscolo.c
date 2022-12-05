/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	char c;
	
	printf("inserire una lettera minuscola: ");
	scanf("%c", &c);

	while((c < 'a') || (c > 'z')) {
		printf("la lettera deve essere minuscola !: ");
		scanf("%c", &c);
	}
	printf("%c \n", c-32);
	
return 0;
}

