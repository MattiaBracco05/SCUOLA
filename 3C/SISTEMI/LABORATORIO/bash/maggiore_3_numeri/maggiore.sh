#!/bin/bash

#Bracco mattia 3C

echo -n "inserisci il primo numero: "
read num1

echo -n "inserisci il secondo numero: "
read num2

echo -n "inserisci il terzo numero: "
read num3

if [[ $num1 -gt $num2 ]]
then
	if [[ $num1 -gt $num3 ]]
	then
		echo "il maggiore è: $num1"
	else
		echo "il maggiore è: $num3"
	fi
elif [[ $num2 -gt $num3 ]]
then
	echo "il maggiore è: $num2"
else
	echo "il maggiore è: $num3"
fi
