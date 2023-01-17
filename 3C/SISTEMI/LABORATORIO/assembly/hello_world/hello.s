//commento su riga vuota con "//" o con  "/*...*/" (come in #c), se devo scrivere un commento in linea al codice scrivo "#" (come in bash)

/*
Bracco Mattia 3C
Primo programma in assembly
*/

.data
	//inseriremo qui le variabili globali e le costanti (come il #DEFINE in #c)
hello: .string "Hello World\n"

.text
	.global main

main:

	//----PREPARO I REGISTRI e STAMPO A VIDEO----
	movl $4,%eax #tipi di move: -movb --> 1 byte, -movw --> 2 byte, -movl --> 4 byte, "$4" per richimare la write
	movl $1,%ebx #1 --> collegamento "standard output" per stampare a video (-standard input --> valore 0, -standard output --> valore 1, -standard error --> valore 2)
	movl $hello,%ecx
	movl $13,%edx #13 è la lunghezza del mio testo (conto anche il "\n")
	int $0x80 #richiamo l'interrupt

	//----RETURN 0----
	movl $1,%eax #"$1" per richiamare la exit
	movl $0,%ebx
	int $0x80
