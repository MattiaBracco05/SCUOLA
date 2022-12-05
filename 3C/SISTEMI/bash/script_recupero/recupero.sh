#!/bin/bash

#Bracco Mattia 3C

exit=0
#-----------------------------------------------------------------------------------------------------------------------------------
function perimetro {
	local perimetro=0 Nlati Vlato
	clear
	echo -n "Quanti lati vuoi inserire ?: "
	read Nlati
	if [[ $Nlati -lt 3 ]]
	then
		echo "Poligono non previsto"
	else
		echo -n "Inserisci valore lato: "
		read Vlato
		perimetro=$(( Vlato*Nlati ))
		echo "Il perimetro vale: $perimetro"
	fi
}
#-----------------------------------------------------------------------------------------------------------------------------------
function calcolaMedia {
	mediaPari=$(( sommaPari/contaPari ))
	mediaDispari=$(( sommaDispari/contaDispari ))
	if [[ $mediaPari -gt $mediaDispari ]]
	then
		echo "La media maggiore è quella dei numeri pari e vale $mediaPari"
	else
		echo "La media maggiore è quella dei numeri dispari e vale $mediaDispari"
	fi
}
#-----------------------------------------------------------------------------------------------------------------------------------
function mediaMaggiore {
	contaPari=0
	contaDispari=0
	sommaPari=0
	sommaDispari=0
	local N num resto
	clear
	echo -n "Quanti numeri vuoi inserire ?: "
	read N
	for ((i=0; i<N; i++))
	do
		echo -n "Inserisci un numero: "
		read num
		resto=$(( num%2 ))
		if [[ $resto -eq 0 ]]
		then
			contaPari=$(( contaPari+1 ))
			sommaPari=$(( sommaPari+num ))
		else
			contaDispari=$(( contaDispari+1 ))
			sommaDispari=$(( sommaDispari+num ))
		fi
	done
	calcolaMedia
}
#-----------------------------------------------------------------------------------------------------------------------------------
function studenti {
local exit=0 scelta studenti=0 studentesse=0 altezza over=0 standard=170
while [[ exit -eq 0 ]]
do
	clear
	echo " ____________________________________________________"
	echo "|                OPZIONI DISPONIBILI                 |"
	echo "|COMANDO:         CHE COSA FA:                       |"
  echo "|____________________________________________________|"
  echo "| M - Studente                                       |"
  echo "| F - Studentessa                                    |"
  echo "| 0 - Termina inserimento                            |"
  echo "|____________________________________________________|"
  echo 
  echo -n "inserire una scelta: "
  read scelta
	case $scelta in
		'm' | 'M')
			studenti=$(( studenti+1 ))
			echo -n "Inserisci l' altezza in cm: "
			read altezza
			;;
		'f' | 'F')
			studentesse=$(( studentesse+1 ))
			echo -n "Inserisci l' altezza in cm: "
			read altezza
			;;
		'0')
			echo "Termino l' inserimento !"
			exit=1
			;;
		*)
			echo "Operatore non valido !"
	esac
	if [[ $altezza -gt $standard ]]
	then
		over=$(( over+1 ))
	fi
done
echo "Hai registrato l' altezza di $studenti studenti e $studentesse studentesse"
echo "In $over superano l' altezza standard di 170cm"
}
#-----------------------------------------------------------------------------------------------------------------------------------
while [[ exit -eq 0 ]]
do
	echo " ____________________________________________________"
	echo "|                OPZIONI DISPONIBILI                 |"
	echo "|COMANDO:         CHE COSA FA:                       |"
  echo "|____________________________________________________|"
  echo "| 1 - PERIMETRO                                      |"
  echo "| 2 - MEDIA MAGGIORE                                 |"
  echo "| 3 - QUANTI                                         |"
  echo "| 4 - EXIT                                           |"
  echo "|____________________________________________________|"
  echo 
  echo -n "inserire una scelta: "
  read scelta
	case $scelta in
		'1')
			perimetro
			;;
		'2')
			mediaMaggiore
			;;
		'3')
			studenti
			;;
		'4')
			clear
			echo "Esco dal programma !"
			exit=1
			;;
		*)
			echo "Operatore non valido !"
	esac
done
