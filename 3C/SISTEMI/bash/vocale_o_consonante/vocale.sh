#!/bin/bash

#Bracco Mattia 3C

lettera=a

while [[ $lettera != "f" ]]
do
	echo -n "inserire una lettera (f per terminare):  "
	read lettera
	case $lettera in
		a) echo "Vocale a" ;;
		e) echo "Vocale e" ;;
		i) echo "Vocale i" ;;
		o) echo "Vocale o" ;;
		u) echo "Vocale u" ;;
		f) echo "Hai scelto di uscire !" ;;
		*) echo "Consonante" ;;
	esac
done
