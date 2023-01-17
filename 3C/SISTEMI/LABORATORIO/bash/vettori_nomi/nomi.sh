#!/bin/bash

#Bracco Mattia 3C

declare -a NomAlunni
indice=0
exit=0

while [[ $exit -eq 0 ]]
do
	clear
	echo -n "Inserisci il nome dell' alunno n. $(( indice+1 )): "
	read NomAlunni[indice]
	echo -n "Premi 0 per continuare: "
	read exit
	indice=$(( indice+1 ))
done
echo "${NomAlunni[*]}"
