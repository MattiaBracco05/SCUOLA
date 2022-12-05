#!/bin/bash

#Bracco Mattia 3C

echo -n "inserisci il primo numero: "
read num1
echo -n "inserisci il secondo numero: "
read num2

if [[ $num1 -eq $num2 ]]
then 
	echo "i numeri sono uguali"
	
elif [[ $num1 -gt $num2 ]] #"elif" forma contratta di else --> if
then
	echo "il numero $num1 è maggiore di $num2"
else
	echo "il numero $num2 è maggiore di $num1"
fi
