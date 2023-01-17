#!/bin/bash

#Bracco Mattia 3C, Esercizio 3

echo -n "inserire nome (persona 1): "
read nome1
echo -n "inserire età (persona 1): "
read eta1
echo -n "inserire sesso (0 = M, 1 = f) (persona 1): "
read sesso1

echo -n "inserire nome (persona 2): "
read nome2
echo -n "inserire età (persona 2): "
read eta2
echo -n "inserire sesso (0 = M, 1 = f) (persona 2): "
read sesso2

echo -n "inserire nome (persona 3): "
read nome3
echo -n "inserire età (persona 3): "
read eta3
echo -n "inserire sesso (0 = M, 1 = f) (persona 3): "
read sesso3

echo -n "inserire nome (persona 4): "
read nome4
echo -n "inserire età (persona 4): "
read eta4
echo -n "inserire sesso (0 = M, 1 = f) (persona 4): "
read sesso4

TOTF=0
TOTM=0

if [[ sesso1 -eq 0 ]]
	then
		TOTM=$(( TOTM+1 ))
	else
		TOTF=$(( TOTF+1 ))
fi

if [[ sesso2 -eq 0 ]]
	then
		TOTM=$(( TOTM+1 ))
	else
		TOTF=$(( TOTF+1 ))
fi

if [[ sesso3 -eq 0 ]]
	then
		TOTM=$(( TOTM+1 ))
	else
		TOTF=$(( TOTF+1 ))
fi

if [[ sesso4 -eq 0 ]]
	then
		TOTM=$(( TOTM+1 ))
	else
		TOTF=$(( TOTF+1 ))
fi

if [[ TOTM -eq 4 ]]
	then 
		echo "siamo tutti uomini"
elif [[ TOTF -eq 4 ]]
	then
		echo "siamo tutte donne"
	else
		echo "siamo $TOTM uomini e $TOTF donne"
fi

TOTmag=0

if [[ eta1 -ge 18 ]]
	then
		TOTmag=$(( TOTmag+1 ))
fi

if [[ eta2 -ge 18 ]]
	then
		TOTmag=$(( TOTmag+1 ))
fi

if [[ eta3 -ge 18 ]]
	then
		TOTmag=$(( TOTmag+1 ))
fi

if [[ eta4 -ge 18 ]]
	then
		TOTmag=$(( TOTmag+1 ))
fi

echo "il numero di maggiorenni è di: $TOTmag"

cd ~/Scrivania/Bracco
mkdir Es3
cd Es3/
touch conteggi.txt

echo PERSONA 1 >> conteggi.txt
echo $nome1 >> conteggi.txt
echo $eta1 >> conteggi.txt
echo $sesso1 >> conteggi.txt

echo PERSONA 2 >> conteggi.txt
echo $nome2 >> conteggi.txt
echo $eta2 >> conteggi.txt
echo $sesso2 >> conteggi.txt

echo PERSONA 3 >> conteggi.txt
echo $nome3 >> conteggi.txt
echo $eta3 >> conteggi.txt
echo $sesso3 >> conteggi.txt

echo PERSONA 4 >> conteggi.txt
echo $nome4 >> conteggi.txt
echo $eta4 >> conteggi.txt
echo $sesso4 >> conteggi.txt

echo numero maggiorenni: >> conteggi.txt
echo $TOTmag >> conteggi.txt
echo persona più giovane: >> conteggi.txt

if [[ eta1 -lt eta2 ]]
	then
		if [[ eta1 -lt eta3 ]]
			then
				if 	[[ eta1 -lt eta4 ]]
					then
						echo $nome1 >> conteggi.txt
						echo $eta1 >> conteggi.txt
					else
						echo $nome4 >> conteggi.txt
						echo $eta4 >> conteggi.txt
				fi
		elif [[ eta3 -lt eta4 ]]
			then
				echo $nome3 >> conteggi.txt
				echo $eta3 >> conteggi.txt
			else
				echo $nome4 >> conteggi.txt
				echo $eta4 >> conteggi.txt
		fi
elif [[ eta2 -lt eta3 ]]
	then
	 	if [[ eta2 -lt eta4 ]]
	 		then
	 			echo $nome2 >> conteggi.txt
				echo $eta2 >> conteggi.txt
			else
				echo $nome4 >> conteggi.txt
				echo $eta4 >> conteggi.txt
		fi
elif [[ eta3 -lt eta4 ]]
	then
		echo $nome3 >> conteggi.txt
		echo $eta3 >> conteggi.txt
	else
		echo $nome4 >> conteggi.txt
		echo $eta4 >> conteggi.txt
fi
