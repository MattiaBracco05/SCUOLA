#!/bin/bash

#Bracco Mattia 3C

exit=0

function somma {

	local N
	local num

	echo "Quanti numeri vuoi inserire ? "
	read N

	for (( i=0; i<N; i++ ))
	do
		echo -n "Inserisci un numero: "
		read num
		somma=$(( somma+num ))
	done

return $somma
}

function sottrazione {

	local N
	local num

	echo -n "Quanti numeri vuoi inserire ? "
	read N
	
	echo -n "Inserisci un numero: "
	read num
	sottrazione=$num

	for (( i=0; i<N-1; i++ ))
	do
		echo -n "Inserisci un numero: "
		read num
		sottrazione=$(( sottrazione-num ))
	done

return $sottrazione
}

function moltiplicazione {

	local N
	local num

	echo -n "Quanti numeri vuoi inserire ? "
	read N
	
	moltiplicazione=1

	for (( i=0; i<N; i++ ))
	do
		echo -n "Inserisci un numero: "
		read num
		moltiplicazione=$(( moltiplicazione*num ))
	done

return $moltiplicazione
}

function divisione {

	local num1
	local num2

	echo -n "Inserisci numero 1: "
	read num1
	echo -n "Inserisci numero 1: "
	read num2
	
	while [[ $num2 -eq 0 ]]
	do
		echo -n "Non si può dividere un numero per 0 !, inserisci numero 2: "
		read num2
	done
	
	divisione=$(( num1/num2 ))
	


return $divisione
}


while [[ exit -eq 0 ]]
do
	echo " ____________________________________________________"
	echo "|                OPZIONI DISPONIBILI                 |"
	echo "|COMANDO:         CHE COSA FA:                       |"
    echo "|____________________________________________________|"
    echo "| + - SOMMA                                          |"
    echo "| - - SOTTRAI                                        |"
    echo "| * - MOLTIPLICA                                     |"
    echo "| : - DIVIDI                                         |"
    echo "| E- EXIT                                            |"
    echo "|____________________________________________________|"
    echo
    
    echo -n "inserire una scelta: "
    read scelta
	
	case $scelta in

		'+')
			somma
			so=$?
			echo "Il risultato della moltiplicazione vale $so"
			;;
		'-')
			sottrazione
			st=$?
			echo "Il risultato della sottrazione vale $st"
			;;
		'*')
			moltiplicazione
			mo=$?
			echo "Il risultato della moltiplicazione vale $mo"
			;;
		':')
			divisione
			di=$?
			echo "Il risultato della divisione vale $di"
			;;
		'e' | 'E')
			echo "Esco dal programma !"
			exit=1
			;;
		*)
			echo "Operatore non valido !"
			;;
	esac
done
