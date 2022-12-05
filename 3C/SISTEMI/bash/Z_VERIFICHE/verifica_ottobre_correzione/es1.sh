#!/bin/bash

#Bracco Mattia 3C, correzione es.1

mkdir Hardware
touch input.txt
mv input.txt Hardware/
echo -n "insierisci un dispositivo di input: "
read dispositivo
echo $dispositivo >> Hardware/input.txt
echo "mouse tastiera" >> Hardware/input.txt
more Hardware/input.txt
echo "monitor casse stampante" > output.txt
mv output.txt Hardware
ls -la Hardware/output.txt
chmod 600 Hardware/output.txt
cat Hardware/input.txt Hardware/output.txt > Hardware/dispositivi.txt
