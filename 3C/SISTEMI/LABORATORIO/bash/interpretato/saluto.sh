#!/bin/bash

#questo è un commento

echo "Hello World"
touch paperino.txt
touch ~/Scrivania/topolino.txt

echo "Ciao sono paperino !" > paperino.txt
echo "Ciao sono topolino !" > ~/Scrivania/topolino.txt

cat ~/Scrivania/topolino.txt paperino.txt > amici.txt
