#!/bin/bash

#Bracco Mattia 3C, Esercizio 2

cd ~/Scrivania/Bracco
mkdir Esercizio2
cd Esercizio2/
touch economico.txt medio.txt caro.txt

echo -n "inserisci il nome di un prodotto: "
read prodotto
echo -n "inserisci il suo prezzo: "
read prezzo

caro=21
eco=10

if [[ prezzo -ge caro ]]
	then
		echo $prodotto >> caro.txt
		echo $prezzo >> caro.txt
	
elif [[ prezzo -le eco ]]
	then
		echo $prodotto >> economico.txt
		echo $prezzo >> economico.txt
	else 
		echo $prodotto >> medio.txt
		echo $prezzo >> medio.txt
fi
