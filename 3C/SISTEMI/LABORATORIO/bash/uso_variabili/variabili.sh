#!/bin/bash

#Bracco Mattia 3c

echo -n "Come ti chiami ? " #il "-n" serve a NON mandare a capo (cosa che altrimenti farebbe in automatico)
read nomeUtente #il comando "read" è l' equivalente del comando "scanf" nel linguaggio c
echo "Ti chiami $nomeUtente, Benvenuto !" #il "$" serve a far visualizzare una variabile

parola="A B C              D"
echo $parola #gli spazi consecutivi li visulaizza come un unico spazio
echo "$parola" #gli spazi consecutivi vengono mantenuti

a=12
echo $a #stampa il valore 12
echo "la variabile a vale $a" #stampa la frase con il valore di a

somma=7+5
echo $somma #stampa "7+5"

n1=7
n2=5
somma=$((n1+n2)) #esegue l' operazione della somma
somma2=$(( 8+6 ))
echo "La prima somma vale: $somma, la seconda $somma2" #stampo il valore delle 2 somme (12 e 14)

echo -n "inserisci il primo numero: "
read num1
echo -n "inserisci il secondo numero: "
read num2

if [[ $num1 -eq $num2 ]]
then 
	echo "i numeri sono uguali"
else
	echo "i numeri sono diversi"
fi #if al contrario, serve per chiudere

# "-eq" per verificare se sono uguali (equal)
# "-ne" per verificare se sono diversi (not equal)
# "-gt" maggiore di (greater than)
# "-ge" maggiore uguale di (greater equal)
# "-lt" minore di
# "-le" minore uguale
