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
	local cont=0
	clear
	for (( i=0;i<N;i++ ))
	do
		echo "--PRODOTTO n. $(( i+1 ))--"
		echo -n "Inserisci il codice del prodotto: "
		read Magazzino[cont]
		cont=$(( cont+1 ))
		echo -n "Inserisci la descrizione del prodotto: "
		read Magazzino[cont]
		cont=$(( cont+1 ))
		echo -n "Inserisci il costo del prodotto €: "
		read Magazzino[cont]
		cont=$(( cont+1 ))
	done
}
#--------------------------------------------------------------------------------------------------------------------------------------
stampaVettore() {
	local cont=0
	clear
	echo "PRODOTTI CARICATI:"
	for (( i=0;i<N;i++ ))
	do
		echo "--PRODOTTO n. $(( i+1 ))--"
		echo -n "Codice: "
		echo -n "${Magazzino[cont]} "
		cont=$(( cont+1 ))
		echo -n "Descrizione: "
		echo -n "${Magazzino[cont]} "
		cont=$(( cont+1 ))
		echo -n "Costo: "
		echo -n "${Magazzino[cont]} "
		cont=$(( cont+1 ))
		echo " "
	done
}
#--------------------------------------------------------------------------------------------------------------------------------------
cercaVettore() {
	local cont=1 found=0
	echo "Premi invio per continuare..."
	read
	clear
	echo -n "Inserisci la descrizione di un prodotto per cercare nel magazzino: "
	read descrizione
	for (( i=0;i<N;i++ ))
	do
		if [[ $descrizione == ${Magazzino[cont]}  ]]
		then
			echo "Descrizione trovata nel magazzino !"
			echo "Codice prodotto: ${Magazzino[cont-1]}"
			echo "Costo prodotto: ${Magazzino[cont+1]} €"
			found=$(( found+1 ))
		fi
		cont=$(( cont+2 ))
	done
	if [[ $found -eq 0 ]]
	then
		echo "Siamo spiacenti ma nel magazzino non sono presenti prodotti con questa descrizione !"
	fi
}
#--------------------------------------------------------------------------------------------------------------------------------------
stampaDescrizione() {
	local found=0
	echo "Premi invio per continuare..."
	read
	clear
	echo "Descrizione dei prodotti > 50€"
	local cont=2
	for (( i=0;i<N;i++ ))
	do
		if [[ ${Magazzino[cont]} -gt 50 ]]
		then
			echo "Descrizione prodotto n. $(( i+1 )): ${Magazzino[cont-1]}"
			found=$(( found+1 ))
		fi
		cont=$(( cont+3 ))
	done
		if [[ $found -eq 0 ]]
	then
		echo "Nel magazzino non sono presenti prodotti con un prezzo superiore ai 50€"
	fi
	echo "Premi invio per continuare..."
	read
	clear
}
#--------------------------------------------------------------------------------------------------------------------------------------
declare -a Magazzino
chiediN
caricaVettore
stampaVettore
cercaVettore
stampaDescrizione



