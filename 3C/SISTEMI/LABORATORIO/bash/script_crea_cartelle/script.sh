#!/bin/bash

#Bracco Mattia 3C

mkdir Esercizio
mkdir Esercizio/Corrispondenti
mkdir -p Esercizio/Corrispondenti/Amici Esercizio/Corrispondenti/Parenti Esercizio/Corrispondenti/Conoscenti
mkdir -p Esercizio/Corrispondenti/Parenti/Nonni Esercizio/Corrispondenti/Parenti/Zii Esercizio/Corrispondenti/Parenti/Cugini
mkdir -p Esercizio/Corrispondenti/Conoscenti/Mare Esercizio/Corrispondenti/Conoscenti/Montagna Esercizio/Corrispondenti/Conoscenti/Citta Esercizio/Corrispondenti/Conoscenti/Lago
mkdir -p Esercizio/Corrispondenti/Amici/Mare Esercizio/Corrispondenti/Amici/Montagna Esercizio/Corrispondenti/Amici/Citta Esercizio/Corrispondenti/Amici/Lago
mkdir -p Esercizio/Corrispondenti/Conoscenti/Mare/Livorno Esercizio/Corrispondenti/Conoscenti/Mare/Genova Esercizio/Corrispondenti/Conoscenti/Mare/Rimini Esercizio/Corrispondenti/Conoscenti/Mare/Messina
mkdir -p Esercizio/Corrispondenti/Conoscenti/Montagna/Aosta Esercizio/Corrispondenti/Conoscenti/Montagna/Stroppo Esercizio/Corrispondenti/Conoscenti/Montagna/Livigno
mkdir -p Esercizio/Corrispondenti/Conoscenti/Citta/Torino Esercizio/Corrispondenti/Conoscenti/Citta/Roma
mkdir -p Esercizio/Corrispondenti/Conoscenti/Lago/Como Esercizio/Corrispondenti/Conoscenti/Lago/Verbania
mkdir -p Esercizio/Corrispondenti/Amici/Mare/Livorno Esercizio/Corrispondenti/Amici/Mare/Genova Esercizio/Corrispondenti/Amici/Mare/Rimini Esercizio/Corrispondenti/Amici/Mare/Messina
mkdir -p Esercizio/Corrispondenti/Amici/Montagna/Aosta Esercizio/Corrispondenti/Amici/Montagna/Stroppo Esercizio/Corrispondenti/Amici/Montagna/Livigno
mkdir -p Esercizio/Corrispondenti/Amici/Citta/Torino Esercizio/Corrispondenti/Amici/Citta/Roma
mkdir -p Esercizio/Corrispondenti/Amici/Lago/Como Esercizio/Corrispondenti/Amici/Lago/Verbania

touch Esercizio/Corrispondenti/Conoscenti/Montagna/Stroppo/elencoAmici.txt
echo "Matteo Giorgio Paolo Luca" > Esercizio/Corrispondenti/Conoscenti/Montagna/Stroppo/elencoAmici.txt

cp -f Esercizio/Corrispondenti/Conoscenti/Montagna/Stroppo/elencoAmici.txt Esercizio/Corrispondenti/Amici/Montagna/Stroppo/elencoAmici.txt

echo "Marco Gabriele Francesco Pietro" >> Esercizio/Corrispondenti/Amici/Montagna/Stroppo/elencoAmici.txt

mv Esercizio/Corrispondenti/Amici/Montagna/Stroppo/elencoAmici.txt Esercizio/Corrispondenti/Amici/Montagna/Stroppo/elencoAmiciAmici.txt

touch Esercizio/Corrispondenti/Conoscenti/Lago/Como/inutile.txt

rm -r Esercizio/Corrispondenti/Conoscenti/Lago

touch Esercizio/Corrispondenti/Parenti/Cugini/indirizzi.txt

echo "Via delle Pietre Via dei Boschi Via Envie Via San Pietro" > Esercizio/Corrispondenti/Parenti/Cugini/indirizzi.txt

cp -f Esercizio/Corrispondenti/Parenti/Cugini/indirizzi.txt Esercizio/Corrispondenti/Parenti/Nonni/indirizzi.txt

echo "Via Staffarda Via Saluzzo Via Torino Via Roma" > Esercizio/Corrispondenti/Parenti/Nonni/indirizzi.txt

cat Esercizio/Corrispondenti/Parenti/Cugini/indirizzi.txt Esercizio/Corrispondenti/Parenti/Nonni/indirizzi.txt >> Esercizio/Corrispondenti/Parenti/indirizzi.txt

more Esercizio/Corrispondenti/Parenti/indirizzi.txt

cd Esercizio/Corrispondenti/Parenti
ls -laX
