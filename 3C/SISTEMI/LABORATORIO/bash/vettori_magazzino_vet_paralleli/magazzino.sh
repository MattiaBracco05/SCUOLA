#!/bin/bash

#Bracco Mattia 3C


N=0
#--------------------------------------------------------------------------------------------------------------------------------------
chiediN() {
	clear
	while [[ $N -lt 5 ]] || [[ $N -gt 10  ]]
	do
		echo -n "Quanti prodotti vuoi registrare ? (5-10): "
		read N
	done
}
#--------------------------------------------------------------------------------------------------------------------------------------
caricaVettore() {
	clear
	for (( i=0;i<N;i++ ))
	do
		echo "--PRODOTTO n. $(( i+1 ))--"
		echo -n "Inserisci il codice del prodotto: "
		read Codice[i]
		echo -n "Inserisci la descrizione del prodotto: "
		read Descrizione[i]
		echo -n "Inserisci il costo del prodotto €: "
		read Costo[i]
	done
}
#--------------------------------------------------------------------------------------------------------------------------------------
stampaVettore() {
	clear
	echo "PRODOTTI CARICATI:"
	for (( i=0;i<N;i++ ))
	do
		echo "--PRODOTTO n. $(( i+1 ))--"
		echo -n "Codice: "
		echo -n "${Codice[i]} "
		echo -n "Descrizione: "
		echo -n "${Descrizione[i]} "
		echo -n "Costo: "
		echo -n "${Costo[i]} "
		echo " "
	done
}
#--------------------------------------------------------------------------------------------------------------------------------------
ordinaCodice() {
	clear
	echo "Ordino in base al codice..."
	
	J=${#Codice[*]}
	flag="true"

	while [[ $flag == "true" ]]
	do
		flag="false"
		for (( i=0;i<J-1;i++ ))
		do
			if [[ ${Codice[i]} -gt ${Codice[i+1]} ]]
			then
				TMP=${Codice[i]}
				Codice[i]=$(( Codice[i+1] ))
				Codice[i+1]=$TMP
				flag="true"
			fi
		done
		j=$(( j-1 ))
	done
}
#--------------------------------------------------------------------------------------------------------------------------------------
ordinaDescrizione() {
	local J
	local flag
	local TMP
	clear
	echo "Ordino in base alla descrizione..."
	
	J=${#Descrizione[*]}
	flag="true"

	while [[ $flag == "true" ]]
	do
		flag="false"
		for (( i=0;i<J-1;i++ ))
		do
			if [[ ${Descrizione[i]} -gt ${Descrizione[i+1]} ]]
			then
				TMP=${Descrizione[i]}
				Descrizione[i]=$(( Descrizione[i+1] ))
				Descrizione[i+1]=$TMP
				flag="true"
			fi
		done
		j=$(( j-1 ))
	done
	echo "${Descrizione[*]}"
}
#--------------------------------------------------------------------------------------------------------------------------------------
ordinaCosto() {
	local J
	local flag
	local TMP
	clear
	echo "Ordino in base al prezzo..."
	
	J=${#Costo[*]}
	flag="true"

	while [[ $flag == "true" ]]
	do
		flag="false"
		for (( i=0;i<J-1;i++ ))
		do
			if [[ ${Costo[i]} -gt ${Costo[i+1]} ]]
			then
				TMP=${Costo[i]}
				Costo[i]=$(( Costo[i+1] ))
				Costo[i+1]=$TMP
				flag="true"
			fi
		done
		j=$(( j-1 ))
	done
	echo "${Costo[*]}"
}
#--------------------------------------------------------------------------------------------------------------------------------------
chiediOrdine() {
	local exit=0
	local scelta
	echo "Premi invio per continuare..."
	read
	clear
	while [[ exit -eq 0 ]]
	do
		clear
		echo " ____________________________________________________"
		echo "|                OPZIONI DISPONIBILI                 |"
		echo "|ORDINA PER:                                         |"
		echo "|____________________________________________________|"
		echo "| C - Ordina in base al codice                       |"
		echo "| D - Ordina in base alla descrizione                |"
		echo "| P - Ordina in base al prezzo                       |"
		echo "|____________________________________________________|"
		echo
		echo -n "Inserisci una scelta: "
		read scelta
		case $scelta in
			'c'|'C')
				ordinaCodice
				exit=1
				;;
			'd'|'D')
				ordinaDescrizione
				exit=1
				;;
			'p'|'P')
				ordinaCosto
				exit=1
				;;
			*)
				echo "Operatore non valido !"
		esac
	done
}
#--------------------------------------------------------------------------------------------------------------------------------------
declare -a Codice
declare -a Descrizione
declare -a Costo
chiediN
caricaVettore
stampaVettore

exit=0
while [[ $exit -eq 0 ]]
do
	chiediOrdine
	echo -n "Vuoi uscire ? (S/N): "
	read scelta
	case $scelta in
		's'|'S')
			clear
			echo "Esco dal programma !"
			exit=1
			;;
		'n'|'N')
			echo "OK..."
			;;
		*)
			echo "Operatore non valido !"
	esac
done



