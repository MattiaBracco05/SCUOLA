#!/bin/bash

#Bracco Mattia 3C

sommap=0
somman=0
positivi=0
negativi=0
numero=1

while [[ $numero -ne 0 ]]
do
	echo -n "inserire un numero (0 per terminare): "
	read numero
	if [[ $numero -ge 0 ]]
	then
		positivi=$(( $positivi+1 ))
		sommap=$(( $sommap+$numero ))
	else
		negativi=$(( $negativi+1 ))
		somman=$(( $somman+$numero ))
	fi
done
positivi=$(( $positivi-1 )) #tolgo 1 ai numeri positivi per togliere il "+1" dello 0 inserito per terminare
echo "la somma dei positivi vale: $sommap"
echo "la somma dei negativi vale: $somman"
echo "tot positvi: $positivi"
echo "tot negativi: $negativi"
