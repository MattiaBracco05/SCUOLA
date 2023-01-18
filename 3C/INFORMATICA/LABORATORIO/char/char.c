/*
Bracco Mattia 3C
*/

#include <stdio.h>

int main() {
	
	char c;
	//stampo la lettera MAIUSCOLA poi quella minuscola
	for (c='A'; c<='Z'; c++){
		printf("%c %c \n", c, c+32);
	}
	
return 0;
}

