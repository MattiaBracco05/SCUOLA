#!/bin/bash

#Bracco Mattia 3C

function alto {
	echo "La persona più alta è $nomeMax, alta $altezzaMax cm"
}
#-------------------------------------------------------------------------------------------------------------------------------------
function altezzaMedia {
	local media
	media=$(( altezzaTOT/N ))
	echo "L'altezza media è di $media cm"
}
#-------------------------------------------------------------------------------------------------------------------------------------
function giovane {
	echo "La persona più giovane è $nomeGiovane, di $etaGiovane anni"
}
#-------------------------------------------------------------------------------------------------------------------------------------
function etaMedia {
	local media
	media=$(( etaTOT/N ))
	echo "L'età media è di $media anni"
}
#-------------------------------------------------------------------------------------------------------------------------------------
function maschiFemmine {
	echo "I maschi sono $maschi e le femmine sono $femmine"
}
#-------------------------------------------------------------------------------------------------------------------------------------
function percentuale {
	local m f tot 
	m=$maschi
	f=$femmine
	tot=$N
	pM=$(( (m*100)/tot ))
	pF=$(( (f*100)/tot ))
	echo "La percentuale dei maschi è $pM%, quella delle femmine è $pF%"
}
#-------------------------------------------------------------------------------------------------------------------------------------
function inserisciDati {
	local i nome statura sesso eta exit numPers
	maschi=0 femmine=0 altezzaTOT=0 etaTOT=0 altezzaMax=-1 etaGiovane=999
	
	while [[ $N -lt 1 ]]
	do
		echo -n "Quante persone vuoi inserire ?: "
		read N
	done
	
	for ((i=0; i<N; i++))
	do
		statura=0 eta=0 sesso=A exit=0
		numPers=$(( i+1 ))
		echo "-- Persona $numPers --" #numero persona inserita
		echo -n "Inserisci il nome: " #nome
		read nome
		while [[ $statura -lt 1 ]] #altezza
		do
			echo -n "Inserisci la statura in cm: "
			read statura
		done
		altezzaTOT=$(( altezzaTOT+statura ))
		while [[ $eta -lt 1 ]] #età
		do
			echo -n "Inserisci l' età: "
			read eta
		done
		etaTOT=$(( etaTOT+eta ))
		while [[ $exit -eq 0 ]]
		do
			echo -n "Inserisci il sesso (M o F): "
			read sesso
			case $sesso in
				'm' | 'M')
					maschi=$(( maschi+1 ))
					exit=1
					;;
				'f' | 'F')
					femmine=$(( femmine+1 ))
					exit=1
					;;
				*)
					echo "Operatore non valido !"
			esac
		done
		if [[ $statura -gt $altezzaMax ]]
		then
			altezzaMax=$statura
			nomeMax=$nome
		fi

		if [[ $eta -lt $etaGiovane ]]
		then
			etaGiovane=$eta
			nomeGiovane=$nome
		fi
	done
}

inserisciDati
exit=0
while [[ exit -eq 0 ]]
do
	echo " ____________________________________________________"
	echo "|                OPZIONI DISPONIBILI                 |"
	echo "|COMANDO:         CHE COSA FA:                       |"
	echo "|____________________________________________________|"
	echo "| 1 - Persona più alta                               |"
	echo "| 2 - Statura media                                  |"
	echo "| 3 - Persona più giovane                            |"
	echo "| 4 - Età media                                      |"
	echo "| 5 - Numero maschi e femmine                        |"
	echo "| 6 - Percentuale maschi e femmine                   |"
	echo "| 7 - Inserisci nuovi dati                           |"
	echo "| 8 - Exit                                           |"
	echo "|____________________________________________________|"
	echo 
	echo -n "inserire una scelta: "
	read scelta
	case $scelta in
		1)
			alto $nomeMax $altezzaMax
			;;
		2)
			altezzaMedia $altezzaTOT $N
			;;
		3)
			giovane $nomeGiovane $etaGiovane
			;;
		4)
			etaMedia $etaTOT $N
			;;
		5)
			maschiFemmine $maschi $femmine
			;;
		6)
			percentuale $maschi $femmine $N
			;;
		7)
			inserisciDati
			;;
		8)
			echo "Esco dal programma !"
			exit=1
			;;
		*)
			echo "Operatore non valido !"
	esac
done

