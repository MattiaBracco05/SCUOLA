#4C Bracco Mattia - Modulo data utilizzato per calcolare distanza fra 2 date

from datetime import date

data1 = date(2000, 1, 1)
data2 = date(2005, 2, 8)

distanza = data2 - data1
print("Distanza (data di nascita - anno 2000):", distanza)
print("Distanza in giorni:",distanza.days)
