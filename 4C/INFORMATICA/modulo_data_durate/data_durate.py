#4C Bracco Mattia - Modulo data utilizzato per la durata

#----- Es. distanza fra 2 date -----
from datetime import date

data1 = date(2000, 1, 1)
data2 = date(2005, 2, 8)

distanza = data2 - data1
print("Distanza (data di nascita - anno 2000):", distanza)
print("Distanza in giorni:",distanza.days)

#----- Parte nuova -----
from datetime import timedelta

data3 = data2 + timedelta(days = 365)
print("Data 3 (distanza di 365 giorni da data 2):", data3)

data4 = data2 + timedelta(weeks = 3)
print("Data 4 (distanza di 3 settimane da data 2):", data4)
