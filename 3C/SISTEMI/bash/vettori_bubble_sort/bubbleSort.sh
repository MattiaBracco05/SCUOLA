#!/bin/bash

#Bracco Mattia 3C

numeri=(10 20 30 70 60 40 50)
echo "${numeri[*]}"

J=${#numeri[*]}
flag="true"

while [[ $flag == "true" ]]
do
	flag="false"
	for (( i=0;i<J-1;i++ ))
	do
		if [[ ${numeri[i]} -gt ${numeri[i+1]} ]]
		then
			TMP=${numeri[i]}
			numeri[i]=$(( numeri[i+1] ))
			numeri[i+1]=$TMP
			flag="true"
		fi
	done
	j=$(( j-1 ))
done
echo "${numeri[*]}"
