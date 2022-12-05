/*
Bracco Mattia 3C
*/

.data
	hello: .string "Come ti chiami?\n"
	lText= .-hello
	stringa: .space 128
	lString: .long 0
.text
	.global main

main:

	//----PREPARO I REGISTRI e STAMPO A VIDEO----
	movl $4,%eax
	movl $1,%ebx
	movl $hello,%ecx
	movl $lText,%edx
	int $0x80
	
	//----PRENDO IN INPUT LA STRINGA (dimensione MAX 128 --> ".space 128")
	movl $3, %eax
	movl $0, %ebx
	movl $stringa, %ecx
	movl $128, %edx
	int $0x80

	//----SALVO IL CONTENUTO DI "eax" DENTRO A "lString"----
	movl %eax, lString

	//----STAMPO A VIDEO----
	movl $4, %eax
	movl $1, %ebx
	movl $stringa, %ecx
	movl $lString, %edx
	int $0x80
	
	//----RETURN 0----
	movl $1, %eax
	movl $0, %ebx
	int $0x80
