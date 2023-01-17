#!/bin/bash

#Bracco Mattia 3C

declare -a cognomi
declare -a voti
declare -a suff
#-------------------------------------------------------------------------------------------------------------------------------------
creaRandom() {
	local num
		num=$(( RANDOM %($max-$min+1)+$min ))
return $num
}
#-------------------------------------------------------------------------------------------------------------------------------------
chiediN() {
	local min=3 max=12
	N=0
	while [[ $N -lt $min ]] || [[ $N -gt $max ]]
	do
		echo -n "Quanti alunni sono presenti nella classe? ($min-$max): "
		read N
	done
}
#-------------------------------------------------------------------------------------------------------------------------------------
caricaVettore() {
	for (( i=0;i<$N;i++ ))
	do
		echo -n "Inserisci il cognome del $((i+1)) studente: "
		read cognomi[i]
		min=2
		max=10
		creaRandom $min $max
		voti[i]=$?
	done
}
#-------------------------------------------------------------------------------------------------------------------------------------
stampaVettore() {
	for (( i=0;i<$N;i++ ))
	do
		echo "----ALUNNO $((i+1))----"
		echo "Cognome: ${cognomi[i]}"
		echo "Voto: ${voti[i]}"
	done
}
#-------------------------------------------------------------------------------------------------------------------------------------
ordinaCognomi() {
	echo "Premi INVIO per continuare..."
	read
	clear
	echo "Ordino i cognomi..."
	J=${#cognomi[*]}
	flag="true"

	while [[ $flag == "true" ]]
	do
		flag="false"
		for (( i=0;i<J-1;i++ ))
		do
			if [[ ${cognomi[i]} < ${cognomi[i+1]} ]]
			then
				TMP=${cognomi[i]}
				cognomi[i]=$(( cognomi[i+1] ))
				cognomi[i+1]=$TMP
				flag="true"
			fi
		done
		j=$(( j-1 ))
	done
	echo "${cognomi[*]}"
}
#-------------------------------------------------------------------------------------------------------------------------------------
votiSufficienti() {
	echo "Premi INVIO per continuare..."
	read
	clear
	echo "Stampo solo i voti sufficenti..."
	for (( i=0;i<$N;i++ ))
	do
		if [[ ${voti[i]} -ge 6 ]]
		then
			echo "Cognome: ${cognomi[i]} Voto: ${voti[i]}"
			suff[i]=${voti[i]} 
		fi
	done
	echo "Elenco voti sufficienti: ${suff[*]}"
}
#-------------------------------------------------------------------------------------------------------------------------------------
cercaCognome() {
	local ins flag=0
	echo "Premi INVIO per continuare..."
	read
	clear
	echo -n "Inserisci un cognome da cercare: "
	read ins
	for (( i=0;i<$N;i++ ))
	do
		if [[ $ins == ${cognomi[i]} ]]
		then
			echo "Voto di ${cognomi[i]}: ${voti[i]}"
			flag=$(( flag+1 ))
		fi
	done
	if [[ $flag -eq 0 ]]
	then
		echo "Il cognome $ins non è stato trovato all' interno della classe!"	
	fi
}
#-------------------------------------------------------------------------------------------------------------------------------------
votiInsufficienti() {
	echo "Premi INVIO per continuare..."
	read
	clear
	echo "Conto i voti insufficienti..."
	local tot=0
	for (( i=0;i<$N;i++ ))
	do
		if [[ ${voti[i]} -lt 6 ]]
		then
			tot=$(( tot+1 ))
		fi
	done
	if [[ $tot -eq 0 ]]
	then
		echo "Non sono presenti voti insufficienti!"
	else
		echo "In totale ci sono $tot voti insufficienti!"	
	fi
}
clear
chiediN
caricaVettore
stampaVettore
ordinaCognomi
votiSufficienti
cercaCognome
votiInsufficienti
echo "Premi INVIO per continuare..."
read
clear

