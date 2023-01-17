#!/bin/bash

#Bracco Mattia 3C

declare -a NomAlunni
indice=0
exit=0
found=0

#inserisco i nomi
while [[ $exit -eq 0 ]]
do
	clear
	echo -n "Inserisci il nome dell' alunno n. $(( indice+1 )): "
	read NomAlunni[indice]
	echo -n "Premi 0 per continuare: "
	read exit
	indice=$(( indice+1 ))
done
#stampo i nomi
echo "${NomAlunni[*]}"
#chiedo il nome da cercare
echo -n "Inserisci un nome da cercare: "
read nome
#lo cerco nel vettore
for (( i=0;i<$indice;i++ ))
do
	if [[ ${NomAlunni[i]} == $nome ]]
	then
		found=$(( found+1 ))
	fi
done
#stampo l' esito della ricerca
if [[ $found -gt 0 ]]
then
	echo "Ho trovato il nome $nome nel vettore (è presente $found volte)"
else
	echo "Nel vettore non è presente il nome $nome"
fi
