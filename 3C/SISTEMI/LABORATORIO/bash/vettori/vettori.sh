#!/bin/bash

#Bracco Mattia 3C

#METODO 1----------------------------------------------------------------------------------------------------------------------------
#dichiaro elementi e ne aggiungo in seguito

#se il nome è composto da più parole devo metterla tra virgolette (es. falco pellegrino)
rapaci=(aquila "falco pellegrino" gufo gheppio barbagianni 111 999)
#rapaci di 0         di 1         di 2   di 3     di 4    di 5 di 6
clear
echo " ____________________________________________________"
echo "|            METODO 1 - Dichiaro e aggiungo          |"
echo "|____________________________________________________|"
echo ""
echo "----------------------CELLA [0]---------------------"
echo "${rapaci[0]}" #stampa il contenuto della cella 0 del vettore rapaci (in questo caso aquila)

echo ""
echo "----------------------CELLA [1]---------------------"
echo "${rapaci[1]}" #stampa il contenuto della cella 1 del vettore rapaci (in questo caso falco pellegrino)

echo ""
echo "-----------------TUTTE LE CELLE [*]-----------------"
echo "${rapaci[*]}" #stampo il contenuto di tutte le celle del vettore mettendo "*" al posto del numero

echo ""
echo "-------------------$ rapaci [0]----------------------"
echo "$rapaci" #restituisce SOLO il contenuto della cella 0 !

echo ""
echo "----------------------DIMENSIONE---------------------"
dimensione=${#rapaci[*]} #salvo la dimensione del vettore "rapaci" mettendo "#" davanti al nome dell' array
echo "La dimensione dell' arrey rapaci è: $dimensione" #stampo la dimensione dell' array
dim2=${#rapaci[2]} #salvo la dimensione (numero di lettere) del contenuto della cella 2 (in questo caso gufo)
echo "La dimensione di ${rapaci[2]} è: $dim2" #stampo la dimensione della cella 2 (3° cella)

echo ""
echo "------------------------SOMMA------------------------"
echo "La somma di ${rapaci[1]} e ${rapaci[4]} vale: $(( ${#rapaci[1]} + ${#rapaci[4]} ))" #stampo la somma di rapaci[1] e rapaci[4]

echo ""
echo "-----------AGGIUNGO 'allocco' E RI-STAMPO------------"
rapaci[12]=allocco #aggiunogo "allocco" all' array rapaci ri-stampo tutti gli elementi è la dimensione
echo "${rapaci[*]}"
echo "La dimensione dell' array rapaci è: ${#rapaci[*]}"

echo ""
echo "-----SOVRASCRIVO LA CELLA [6] '999' => 'POIANA'------"
rapaci[6]=poiana #sovrascrivo la cella 6
echo "${rapaci[*]}"
echo "La dimensione dell' array rapaci è: ${#rapaci[*]}"

echo ""
echo "----------AGGIUNGO 'piccione' ALLA CELLA 8-----------"
rapaci[8]="piccione brutto e cattivo"
echo "Cosa c'è nella cella 8 ? ${rapaci[8]}"
echo "${rapaci[*]}"
echo "La dimensione dell' array rapaci è: ${#rapaci[*]}"


#METODO 2----------------------------------------------------------------------------------------------------------------------------
#dichiaro tutti gli elementi

echo " ____________________________________________________"
echo "|            METODO 2 - Dichiaro tutto subito        |"
echo "|____________________________________________________|"
echo ""
echo "-----------------------COLORI-------------------------"
colori[0]=rosso
colori[1]="blu cobalto"
colori[2]="giallo limone"
colori[3]="arcobaleno peppa pig"
echo "${colori[*]}"
echo "La dimensione dell' array \"colori\" è: ${#colori[*]} "

#METODO 3----------------------------------------------------------------------------------------------------------------------------
#vettore vuoto da riempire in seguito

echo " ____________________________________________________"
echo "|          METODO 3 - Array vuoto e ne aggiungo      |"
echo "|____________________________________________________|"
echo ""
echo "------------------------CIBO---------------------------"
declare -a cibo
for (( i=0;i<5;i++ ))
do
	echo -n "Inserisci il $(( i+1 ))° cibo: "
	read cibo[i]
done
echo "${cibo[*]}"

#METODO 4----------------------------------------------------------------------------------------------------------------------------
#inserisco con lo spazio termino con INVIO

echo " ____________________________________________________"
echo "|          METODO 4 - Inserisco spaziati             |"
echo "|____________________________________________________|"
echo ""
echo "------------------------AUTO---------------------------"
echo -n "Inserisci nomi auto spaziati: "
read -a auto
echo "${auto[*]}"

#METODO 5----------------------------------------------------------------------------------------------------------------------------
#dichiaro in disordine

echo " ____________________________________________________"
echo "|          METODO 5 -  DICHIARO IN DISORDINE         |"
echo "|____________________________________________________|"
echo ""
echo "------------------------GATTI---------------------------"
gatti=([4]=pallino [2]="ciuppi muppi" [0]=alfredo [6]=silvestro)
echo "${gatti[*]}"

#ELIMINARE DAL VETTORE-------------------------------------------------------------------------------------------------------------
echo " ____________________________________________________"
echo "|             ELIMINARE UNA CELLA - unset            |"
echo "|____________________________________________________|"
echo ""
echo "------------------------GATTI---------------------------"
echo "${gatti[*]}"
unset gatti[4]
echo "${gatti[*]}"

#ELIMINARE VETTORI------------------------------------------------------------------------------------------------------------
echo " ____________________________________________________"
echo "|             ELIMINARE UN ARRAY - unset             |"
echo "|____________________________________________________|"
echo ""
echo "------------------------COLORI---------------------------"
echo "Prima: ${colori[*]}"
unset colori
echo "Dopo: ${colori[*]}"
