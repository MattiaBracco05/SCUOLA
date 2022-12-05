#!/bin/bash

#Bracco Mattia 3C

giorni=0
merendine=0
panini=0

echo -n "quanti soldi vuoi dare come paghetta a Mario ?: "
read soldi

while [[ $soldi -gt 0 ]]
do
	echo " ____________________________________________________"
	echo "|                OPZIONI DISPONIBILI                 |"
	echo "|COMANDO:         CHE COSA FA:                       |"
    echo "|____________________________________________________|"
    echo "| A- compra una merendina (1€)                       |"
    echo "| B- compra un panino     (3€)                       |"
    echo "|____________________________________________________|"
    echo
	echo -n "inserire una scelta: "	
	read scelta
	case $scelta in

		a | A)
			echo "hai acquistato una merendina !"
			soldi=$(( soldi-1 ))
			merendine=$(( merendine+1 ))
			echo "ti rimangono $soldi €"
			giorni=$(( giorni+1))
			;;

		b | B)
			if [[ $soldi -ge 3 ]]
			then
				echo "hai acquistato un panino !"
				soldi=$(( soldi-3))
				panini=$(( panini+1 ))
				echo "ti rimangono $soldi €"
				giorni=$(( giorni+1 ))
			else
				echo "non hai abbastanza soldi per acquistare un panino !"
				echo "puoi però acquistare $soldi merendine "
			fi
			;;

	esac
done
echo "hai mangiato per $giorni giorni"
echo "hai mangiato $panini panini e $merendine merendine"
