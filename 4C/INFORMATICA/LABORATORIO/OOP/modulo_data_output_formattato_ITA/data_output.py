#4C Bracco Mattia - Output formattato per le date

from datetime import date
import locale
locale.setlocale(locale.LC_ALL, '')

nascita = date(2005, 2, 8)

#STAMPARE IN CIFRE:

#	%d --> giorno del mese
# %m --> numero del mese
# %y --> anno con 2 cifre
#	%Y --> anno con 4 cifre

#STAMPARE IN LETTERE:
#	%a --> nome del giorno abbreviato
# %A --> nome del giorno completo
#	%b --> nome del mese abbreviato
# %B --> nome del mese completo

print("----- Esempio output 1 -----")
print(nascita.strftime("%d-%m-%y"))
print("----- Esempio output 2 -----")
print(nascita.strftime("%A %d %B %Y"))
