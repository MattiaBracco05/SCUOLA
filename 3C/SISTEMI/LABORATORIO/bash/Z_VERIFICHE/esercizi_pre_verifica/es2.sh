#!/bin/bash

#Bracco Mattia 3C

mkdir Esercizio2
cd Esercizio2/

echo -n "inserisci il primo numero: "
read n1

echo -n "inserisci il secondo numero: "
read n2

echo -n "inserisci il terzo numero: "
read n3

echo -n "inserisci il quarto numero: "
read n4

totminore=0
totmaggiore=1

somma=$(( n1+n2+n3+n4 ))
echo "la somma vale: $somma"

if [[ n1 -lt 10 ]]
then
	totminore=$(( totminore+n1 ))
else
	totmaggiore=$(( totmaggiore*n1 ))
fi

if [[ n2 -lt 10 ]]
then
	totminore=$(( totminore+n2))
else
	totmaggiore=$(( totmaggiore*n2))
fi

if [[ n3 -lt 10 ]]
then
	totminore=$(( totminore+n3))
else
	totmaggiore=$(( totmaggiore*n3))
fi

if [[ n4 -lt 10 ]]
then
	totminore=$(( totminore+n4))
else
	totmaggiore=$(( totmaggiore*n4))
fi

echo "totminore: $totminore"
echo "totmaggiore: $totmaggiore"

touch risultati.txt
echo $somma >> risultati.txt
echo $totminore >> risultati.txt
echo $totmaggiore >> riusltati.txt
	
