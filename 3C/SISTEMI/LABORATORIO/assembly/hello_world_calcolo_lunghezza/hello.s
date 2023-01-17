/*
Bracco Mattia 3C
*/

.data
hello: .string "Hello World! ~ Mattia\n"
lungh= .-hello

.text
	.global main

main:

	//----PREPARO I REGISTRI e STAMPO A VIDEO----
	movl $4,%eax
	movl $1,%ebx
	movl $hello,%ecx
	movl $lungh,%edx #"lungh" è la lunghezza del mio testo (conto anche il "\n")
	int $0x80

	//----RETURN 0----
	movl $1,%eax
	movl $0,%ebx
	int $0x80
