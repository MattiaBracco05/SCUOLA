#!/bin/bash

#Bracco Mattia 3C

echo -n "inserire il numero dei sacchi di cemento: "
read cemento

echo -n "inserire il prezzo complessivo dei 30 sacchi di ghiaia: "
read ghiaia

echo -n "inserire il numero di cariole: "
read cariole

echo -n "inserire il prezzo complessivo di 20 caschi di sicurezza: "
read caschi

echo -n "inserire il prezzo complessivo di 15 bidoni di vernice: "
read bidoni

pcemento=5
pcariole=50
totale=$(( cemento*pcemento+ghiaia+cariole*pcariole+caschi+bidoni+50 ))
echo "il totale senza iva è di: $totale €"

