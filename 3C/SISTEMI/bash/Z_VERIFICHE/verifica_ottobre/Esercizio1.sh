#!/bin/bash

#Bracco Mattia 3C, Esercizio 1

mkdir Hardware
touch input.txt
mv -f input.txt ~/Scrivania/Bracco/Hardware

echo -n "inserisci un dispositivo di input: "
read dispositivo1
cd Hardware/
echo $dispositivo1 >> input.txt
echo mouse >> input.txt
echo tastiera >> input.txt

more input.txt

cd ..
touch output.txt
echo monitor >> output.txt
echo stampante >> output.txt
echo cuffie >> output.txt
mv -f output.txt ~/Scrivania/Bracco/Hardware
ls -l output.txt
cd Hardware/
chmod +w+r-x output.txt
cat input.txt output.txt >> dispositivi.txt

