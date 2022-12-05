#!/bin/bash

#Bracco Mattia 3C

Contatore=0

while [[ $Contatore -lt 10 ]]
do
	echo "il valore della varibile è: $Contatore"
	(( Contatore++ )) #forma abbreviata di 	"Contatore=$(( Contatore+1 ))"
done
