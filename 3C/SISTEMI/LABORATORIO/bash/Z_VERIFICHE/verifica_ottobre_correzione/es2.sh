#!/bin/bash

#Bracco Mattia 3C, correzzione es.2

mkdir Es2
touch Es2/economico.txt Es2/medio.txt Es2/caro.txt
ls -laX Es2/*.txt

echo -n "inserire il nome del prodotto: "
read nome
echo -n "inserire il prezzo del prodotto: "
read prezzo

if [[ $prezzo -lt 0 ]]
then
	echo "Hai inserito un numero negativo !"
elif [[ $prezzo -le 10 ]]
	then
		echo "$nome $prezzo" >> Es2/economico.txt
	elif [[ prezzo -le 20 ]]
		then
			echo "$nome $preozzo" >> Es2/medio.txt
	else
		echo "$nome $prezzo" >> Es2/medio.txt
fi
	
