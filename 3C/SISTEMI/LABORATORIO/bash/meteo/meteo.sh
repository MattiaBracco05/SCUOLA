#!/bin/bash

#Bracco Mattia 3C

exit=0
TOTmax=0
TOTmin=0
Vmax=4
Vmin=9
Ntemperature=0

Inserimento () {
	
	local Tmax=0
	local Tmin=10
	
	echo -n "Inserire nome città: "
	read citta

	while [[ $Tmax -lt 5 || $Tmax -gt 23  ]]
	do
		echo -n "Inserire temperatura MAX (5° - 23°): "
		read Tmax
	done

	while [[ $Tmin -lt -5 || $Tmin -gt 8 ]]
	do
		echo -n "Inserire temperatura MIN (-5° - 8°): "
		read Tmin
	done
	
	Ntemperature=$(( Ntemperature+1 )) #aumento il conteggio delle temperature registrate che mi servirà per la media
	TOTmax=$(( TOTmax+Tmax ))
	TOTmin=$(( TOTmin+Tmin ))

	if [[ $Tmax -gt Vmax ]]
	then
		Vmax=$Tmax #cambio la temperatura massima registrata
		cittaMax=$citta #assegno la città
	fi

	if [[ $Tmin -lt Vmin ]]
	then
		Vmin=$Tmin #cambio la temperatura minima registrata
		cittaMin=$citta #assegno la città
	fi

}

ValoriMedi () {

	media=$(( (TOTmax+TOTmin)/(Ntemperature*2) ))
	mediaMAX=$(( TOTmax/Ntemperature ))
	mediaMIN=$(( TOTmin/Ntemperature ))
	echo "Media T: $media°C, Media T MAX: $mediaMAX°C, Media T MIN: $mediaMIN°C"
}

while [[ exit -eq 0 ]]
do
	echo " ____________________________________________________"
	echo "|                OPZIONI DISPONIBILI                 |"
	echo "|COMANDO:         CHE COSA FA:                       |"
    echo "|____________________________________________________|"
    echo "| A - INSERISCI TEMPERATURE                          |"
    echo "| B - MEDIE TEMPERATURE                              |"
    echo "| C - TEMPERATURE MAX E MIN                          |"
    echo "| E - EXIT                                           |"
    echo "|____________________________________________________|"
    echo 
    echo -n "inserire una scelta: "
    read scelta
	case $scelta in
		'A' | 'a')
			Inserimento
			;;
		'B' | 'b')
			ValoriMedi
			;;
		'C' | 'c')
			echo "T MAX: $Vmax°C registrata a $cittaMax"
			echo "T MIN: $Vmin°C registrata a $cittaMin"
			;;
		'E' | 'e')
			echo "Esco dal programma !"
			exit=1
			;;
		*)
			echo "Operatore non valido !"
	esac
done
	
