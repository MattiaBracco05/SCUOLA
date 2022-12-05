#!/bin/bash

#Bracco Mattia 3C

echo -n "inserisci il primo numero: "
read num1
echo -n "inserisci il secondo numero: "
read num2
echo -n "inserisci il terzo numero: "
read num3
echo -n "inserisci il quarto numero: "
read num4
echo -n "inserisci stringa 1: "
read stringa1
echo -n "inserisci stringa 2: "
read stringa2

a=""

while [[ -z $a ]]
do
	echo " ____________________________________________________"
	echo "|                OPZIONI DISPONIBILI                 |"
	echo "|COMANDO:         CHE COSA FA:                       |"
    echo "|____________________________________________________|"
    echo "| A- somma i 4 numeri                                |"
    echo "| B- calcolo media dei 4 numeri                      |"
    echo "| C- maggiore tra i 4 numeri                         |"
    echo "| D- minore tra i 4 numeri                           |"
    echo "| E- confronta le stringhe se sono uguali            |"
    echo "| F- confronta i numeri se sono uguali               |"
    echo "| G- stampa le stringe in ordine alfabetico          |"
    echo "| H- controlla se le stringhe sono vuote             |"
    echo "| R- reinserisci i dati                              |"
    echo "| Z- EXIT                                            |"
    echo "|____________________________________________________|"
    echo
    
    echo -n "inserire una scelta: "
    read scelta
    
    case $scelta in
    
        'A' | 'a')
            SOMMA=$(( num1+num2+num3+num4 ))
			echo "la somma di $num1 + $num2 + $num3 + $num4 vale $SOMMA"
        	;;
        	
        'B' | 'b')
            SOMMA=$(( num1+num2+num3+num4 ))
            MEDIA=$(( SOMMA/4 ))
            echo "la media dei 4 numeri vale $MEDIA"
        	;;
        	
        'C' | 'c')
        	if [[ $num1 -gt $num2 ]]
        	then
        		maggiore=$((num1))
       		elif [[ $num2 -gt $num3 ]]
       		then
       			maggiore=$((num2))
       		elif [[ $num3 -gt $num4 ]]
       		then
       			maggiore=$((num3))
       		else
       			maggiore=$((num4))
        	fi
        	echo "il numero maggiore è: $maggiore"
        	;;
        		
        'D' | 'd')
        	if [[ $num1 -lt $num2 ]]
        	then
       			minore=$((num1))
       		elif [[ $num2 -lt $num3 ]]
       		then
       			minore=$((num2))
       		elif [[ $num3 -lt $num4 ]]
       		then
       			minore=$((num3))
       		else
       			minore=$((num4))
       		fi
       		echo "il numero minore è: $minORE"
       		;;
        		
        'E' | 'e')
            if [[ $stringa1 == $stringa2 ]]
           	then
           		echo "le stringhe sono uguali"
           	else 
         		echo "le stringhe non sono uguali"
           	fi
        	;;
        
        'F' | 'f')
        	if [[ ($num1 -eq $num2) && ($num2 -eq $num3) && ($num3 -eq $num4) ]]
        	then
       			echo "i numeri sono tutti uguali"
       		else
       			echo "i numeri non sono tutti uguali"
       		fi
    	   	;;
    	   	
       	'G' | 'g')
       		if [[ $stringa1 > $stringa2 ]]
       		then
       			echo "$stringa1"
     			echo "$stringa2"
      		else 
       			echo "$stringa1"
      			echo "$stringa2"
   			fi
  			;;
       			
       	'H' | 'h')
      		if [[ $stringa1 == "" ]]
       		then
       			echo "la stringa 1 è vuota"
      		else
       			echo "la stringa 1 non è vuota"
       		fi
  			if [[ $stringa2 == "" ]]
      		then
       			echo "la stringa 2 è vuota"
       		else
      			echo "la stringa 2 non è vuota"
       		fi
       		;;
       		
       	'R' | 'r')
       		echo -n "inserisci il primo numero: "
			read num1
			echo -n "inserisci il secondo numero: "
			read num2
			echo -n "inserisci il terzo numero: "
			read num3
			echo -n "inserisci il quarto numero: "
			read num4
			echo -n "inserisci stringa 1: "
			read stringa1
			echo -n "inserisci stringa2 : "
			read stringa2
			;;
			
		'Z' | 'z') 
            echo "esco dal programma !" 
            a="exit"
        	;;
       	*)
       		echo "inserito operatore non valido !"
    esac
done
