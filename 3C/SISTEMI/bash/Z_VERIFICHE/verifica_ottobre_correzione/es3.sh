#!/bin/bash

#Bracco Mattia 3C, correzione es.3

contadonne=0
uomini=0

echo -n "inserire nome persona 1: "
read nome1
echo -n "inserire eta persona 1: "
read eta1
echo -n "inserire sesso persona 1 (0 = F, 1 = M): "
read sesso1
if [[ $sesso1 -eq 0 ]]
then
	contadonne=$((contadonne+1))
fi

echo -n "inserire nome persona 2: "
read nome2
echo -n "inserire eta persona 2: "
read eta2
echo -n "inserire sesso persona 2 (0 = F, 1 = M): "
read sesso2
if [[ $sesso2 -eq 0 ]]
then
	contadonne=$((contadonne+1))
fi

echo -n "inserire nome persona 3: "
read nome3
echo -n "inserire eta persona 3: "
read eta3
echo -n "inserire sesso persona 3 (0 = F, 1 = M): "
read sesso3
if [[ $sesso3 -eq 0 ]]
then
	contadonne=$((contadonne+1))
fi

echo -n "inserire nome persona 4: "
read nome4
echo -n "inserire eta persona 4: "
read eta4
echo -n "inserire sesso persona 4 (0 = F, 1 = M): "
read sesso4
if [[ $sesso4 -eq 0 ]]
then
	contadonne=$((contadonne+1))
fi

if [[ $contadonne -eq 4 ]]
then
	echo "siamo tutte donne"

elif [[ $contadonne -eq o ]]
then
	echo "siamo tutti uomini"

else
	uomini=$((4-$contadonne))
	echo "siamo $contadonne donne"
	echo "siamo $uomini uomini"
fi

giovane=$(($eta1))
nomegiovane=$(($nome1))

if [[ eta2 -lt giovane ]]
then
	giovane=$(($eta2))
	nomegiovane=$(($nome2))
fi

if [[ eta3 -lt giovane ]]
then
	giovane=$(($eta3))
	nomegiovane=$(($nome3))
fi

if [[ eta4 -lt giovane ]]
then
	giovane=$(($eta4))
	nomegiovane=$(($nome4))
fi


