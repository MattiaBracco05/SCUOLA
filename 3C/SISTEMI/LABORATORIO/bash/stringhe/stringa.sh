#!/bin/bash

#Bracco Mattia 3C

#operatori per le stringhe
#	si = s2 (confronta se sono uguali)
#	s1 != s2 (confronta se sono diversi)
#	s1 < s2 (confronta se s1 è minore alfabeticamente rispetto s2, (confronta la prima lettera se uguale passa alla 2 e così via)) 
#	s1 > s2 (confronta se s1 è maggiore alfabeticamente rispetto s2, (confronta la prima lettera se uguale alla 2 e così via))
#	-n s1 (confronta che s1 NON sia vuota)
#	-z s1 (confronta che s1 sia vuota)

pass1="qualcosa"
while [[ -n $pass1 ]]
do
	echo "inserisci la tua password: "
	read pass1
	echo "reinserisci la tua password: "
	read pass2
	if [[ $pass1 = $pass2 ]]
	then
		echo "password verificata !"
		pass1=""
	else
		echo "le password non coincidono !"
	fi
done
