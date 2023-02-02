#4C Bracco Mattia - Classi rettangolo calcolo area

class rettangolo(object):
	
	def __init__(self, base, altezza):
		self.setBase(base)
		self.setAltezza(altezza)
	
	def setBase(self, b):
		self.__base = b
		
	def setAltezza(self, a):
		self.__altezza = a
	
	def getBase(self):
		return self.__base
		
	def getAltezza(self):
		return self.__altezza
		
	def calcolaArea(self):
		return (self.getBase() * self.getAltezza())
		
print("RETTANGOLO 1")
mioRettangolo = rettangolo(3, 5)
print("Valore base:", mioRettangolo.getBase())
print("Valore altezza:", mioRettangolo.getAltezza())
print("Valore area:", mioRettangolo.calcolaArea())

print("\nRETTANGOLO 2")
mioRettangolo2 = rettangolo(4, 7)
print("Valore base:", mioRettangolo2.getBase())
print("Valore altezza:", mioRettangolo2.getAltezza())
print("Valore area:", mioRettangolo2.calcolaArea())

if (mioRettangolo.calcolaArea() > mioRettangolo2.calcolaArea()):
	print("\nRettangolo 1 ha l'area maggiore")
else:
	print("\nRettangolo 2 ha l'area maggiore")
