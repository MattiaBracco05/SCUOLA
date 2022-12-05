/*
Bracco Mattia 3C
*/

.data
	stringa: .space 128
	lungh: .long 0
.text
	.global main

main:

	//----PRENDO IN INPUT LA STRINGA (dimensione MAX 128 --> ".space 128")
	movl $3, %eax #quando viene eseguita la read, nel registro "eax" viene salvato la dimensione effettiva dei caratteri inseriti (compreso il \n dell'invio)
	movl $0, %ebx
	movl $stringa, %ecx
	movl $128, %edx
	int $0x80

	//----SALVO IL CONTENUTO DI "eax" DENTRO A "lungh"----
	movl %eax, lungh

	//----STAMPO A VIDEO----
	movl $4, %eax
	movl $1, %ebx
	movl $stringa, %ecx
	movl $lungh, %edx
	int $0x80

	//----RETURN 0----
	movl $1, %eax #"$1" per richiamare la exit
	movl $0, %ebx
	int $0x80
