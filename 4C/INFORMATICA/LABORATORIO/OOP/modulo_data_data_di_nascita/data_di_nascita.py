#4C Bracco Mattia - mmodulo data utilizzato per le date di nascita

from datetime import date
nascita = date(2005, 2, 8)
print("Data di Nascita: {:2d} - {:2d} - {:4d}".format(nascita.day, nascita.month, nascita.year))
