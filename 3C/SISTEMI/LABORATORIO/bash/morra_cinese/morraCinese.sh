#!/bin/bash

#Bracco Mattia 3C

function creaNumero {
local num
	num=$(( RANDOM %($max-$min+1)+$min ))
return $num
}

#-------------------------------------------------------------------------------------------------------------------------------------
function partita {
	clear
	local round input inputU inputC PC UT
	PC=0 UT=0 #azzero i parziali
	partite=$(( partite+1 )) #incremeno il contatore delle partite

	#creo il numero di round
	min=3 max=8
	creaNumero $min $max
	N=$?
	echo "Preparati a giocare una partita di $N round"
	echo "Sei pronto ? premi INVIO per continuare..."
	read

	#giro per tutti i round
	for (( i=0; i<N; i++ ))
	do
		#numero round attuale
		round=$(( i+1 ))
		echo "Round $round di $N PC $PC - $UT UTENTE"
		#INSERIMENTO UTENTE
		echo " ____________________________________________________"
		echo "| C - Carta                                          |"
		echo "| F - Forbici                                        |"
		echo "| S - Sasso                                          |"
		echo "|____________________________________________________|"
		echo -n "Inserire una scelta: "
		read input
		case $input in
			'C' | 'c')
				inputU=1
				echo "Hai scelto CARTA"
				;;
			'F' | 'f')
				echo "Hai scelto FORBICI"
				inputU=2
				;;
			'S' | 's')
				echo "Hai scelto SASSO"
				inputU=3
				;;
		esac
		#INSERIMENTO PC
		min=1 max=3
		creaNumero $min $max
		inputC=$?
		case $inputC in
			1)
				echo "Il pc ha scelto CARTA"
				;;
			2)
				echo "Il pc ha scelto FORBICI"
				;;
			3)
				echo "Il pc ha scelto SASSO"
				;;
		esac
		#determino se è un pareggio
		if [[ $inputU -eq $inputC ]]
		then
			echo "Pareggio !"
		else
			#determino se vince il pc
			if [[ (($inputC -eq 1) && ($inputU -eq 3)) || (($inputC -eq 2) && ($inputU -eq 1)) || (($inputC -eq 3) && ($inputU -eq 2)) ]]
			then
				echo "Questo round lo vince il computer !"
				PC=$(( PC+1 ))
				#determino se vince l' utente
			else
				echo "Hai vinto questo round !"
				UT=$(( UT+1 ))
			fi
		fi
		#invio per continuare
		echo "Premi invio per continuare..."
		read
		clear
	done
	#determino la vincita della partita
		if [[ $PC -eq $UT ]]
		then
			echo "Partita pareggiata !"
			pareggiate=$(( pareggiate+1 ))
		elif [[ $PC -gt $UT ]]
		then
			echo "Partita vinta dal PC !"
			perse=$(( perse+1 ))
		else
			echo "Partita vinta dall' UTENTE !"
			vinte=$(( vinte+1 ))
		fi
		echo "Premi invio per continuare..."
		read
		clear
}
#-------------------------------------------------------------------------------------------------------------------------------------
function statistiche {
	clear
	echo " ____________________________________________________"
	echo "|            MORRA CINESE - STATISTICHE              |"
	echo "|____________________________________________________|"
	echo "Partite giocate: $partite"
	echo "Vinte: $vinte"
	echo "Pareggiate: $pareggiate"
	echo "Perse: $perse"
	echo "Premi invio per continuare..."
	read
}
#-------------------------------------------------------------------------------------------------------------------------------------
exit=0 partite=0 vinte=0 pareggiate=0 perse=0
while [[ $exit -eq 0 ]]
do
		clear
		echo " ____________________________________________________"
		echo "|          MORRA CINESE - OPZIONI DISPONIBI          |"
		echo "|COMANDO:         CHE COSA FA:                       |"
		echo "|____________________________________________________|"
		echo "| 1 - Nuova partita                                  |"
		echo "| 2 - Statistiche                                    |"
		echo "| 3 - EXIT                                           |"
		echo "|____________________________________________________|"
		echo -n "Inserire una scelta: "
		read scelta
		case $scelta in
			1)
				partita
				;;
			2)
				statistiche
				;;
			3)
				echo -n "Sei sicuro di volere uscire ? (S/N): "
				read conferma
				if [[ $conferma == 's' || $conferma == 'S' ]]
				then
					echo "OK, è stato bello giocare con te ;)"
					exit=1
				fi
				;;
			*)
				echo "Operatore non valido !"
		esac
done	
