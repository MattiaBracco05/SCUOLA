#!/bin/bash

#Bracco Mattia 3C

scelta=1
SOMMA=0

while [[ $scelta -ne 0 ]]
do
	echo -n "inserisci una scelta (0 = EXIT, 1 = +, 2 = -, 3 = *, 4 = /): "
	read scelta
	case $scelta in
		0) echo "esco dal programma !" ;;
		1)
			echo -n "quanti numeri vuoi sommare ?: "
			read numeri
			for (( i=0; i<$numeri; i++ ))
			do
				num=$(( RANDOM % 11 ))
				echo "$num"
				SOMMA=$(( $SOMMA + $num ))
			done
			echo "la somma dei $numeri numeri vale: $SOMMA"
			;;
		2)
			echo -n "inserire num1: "
			read num1
			echo -n "inserire num2: "
			read num2
			if [[ $num1 -gt $num2 ]]
			then
				DIFFERENZA=$(( $num1 - $num2 ))
				echo "la differenza di $num1 e $num2 vale: $DIFFERENZA"
			else
				DIFFERENZA=$(( $num2 - $num1 ))
				echo "la differenza di $num2 e $num1 vale: $DIFFERENZA"
			fi
			;;
		3)
			echo -n "inserire num1: "
			read num1
			echo -n "inserire num2: "
			read num2
			MOLTIPLICAZIONE=$(( $num1 * $num2 ))
			echo "la moltiplicazione di $num1 e $num2 vale: $MOLTIPLICAZIONE"
			;;
		4)
			echo -n "inserire num1: "
			read num1
			echo -n "inserire num2: "
			read num2
			while [[ $num2 -eq 0 ]]
			do
				echo "impossibile dividere per 0"
				echo -n "reinserisci il secondo numero: "
				read num2
			done
			DIVISIONE=$(( $num1 / $num2 ))
			echo "la divisione tra $num1 e $num2 vale: $DIVISIONE"
			;;
		*) 
			echo "operatore non valido !"
			;;
	esac
done
