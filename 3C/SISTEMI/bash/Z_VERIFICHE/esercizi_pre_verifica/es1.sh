#!/bin/bash

#Bracco Mattia 3C

mkdir Esercizio1

echo -n "inserire una parola che verra inserita in File1: "
read parola1

echo -n "inserire una parola che verra inserita in File2: "
read parola2

echo -n "inserire una parola che verra inserita in File3: "
read parola3

echo $parola1 > File1.txt
echo $parola2 > File2.txt
echo $parola3 > File3.txt

cp File1.txt Esercizio1
cp File2.txt Esercizio1
cp File3.txt Esercizio1

cat File1.txt File2.txt File3.txt > unione.txt
cat unione.txt

rm -f File1.txt
rm -f File2.txt
rm -f File3.txt

echo -n "inserisci il tuo nome : "
read nome

echo -n "inserisci il tuo cognome: "
read cognome

echo -n "inserisci la tua classe: "
read classe

echo $nome >> unione.txt
echo $cognome >> unione.txt
echo $classe >> unione.txt

cat unione.txt

cd Esercizio1/
ls

