#!/bin/bash

#Bracco Mattia 3C

#metodo 1 - function NomeDellaFunzione {...
function saluta {
	echo -n "Come ti chiami ? "
	read nome
	echo "Ciao $nome !"
}

#metodo 2 - NomeDellaFunzione() {...
sommaValori() {
	echo -n "Inserisci il primo numero: "
	read num1
	echo -n "Inserisci il secondo numero: "
	read num2
	somma=$(( num1+num2 ))
	echo "La somma di $num1 + $num2 vale $somma"
}

#VALORE DI RITORNO - return $VariabileRitorno

function moltiplica {

	local moltiplicazione=1 #local serve per "confinare" la variabile in quella funzione
	for (( i=0; i<5; i++ ))
	do
		echo -n "Inserisci il valore (moltiplicatore): "
		read valore
		moltiplicazione=$(( moltiplicazione*valore ))
	done

return $moltiplicazione
}

#scrivo solo il nome della funzione per richiamarla, posso richiamare anche all' interno di un' altra funzione ad es. scrivendo "sommaValori" nella funzione "saluta" (la funzione richiamata deve essere messa prima di quella in cui la stiamo richiamando !)

saluta
sommaValori
moltiplica
m=$?
echo "Il risultato della moltiplicazione vale $m"


