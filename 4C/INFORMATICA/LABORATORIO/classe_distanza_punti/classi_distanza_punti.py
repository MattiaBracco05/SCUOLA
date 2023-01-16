#4C Bracco Mattia - Classi rettangolo calcolo area

import math

class punti(object):
	
	def __init__(self, x1, y1, y2, x2):
		self.setX1(x1)
		self.setY1(y1)
		self.setX2(x2)
		self.setY2(y2)
	
	def setX1(self, val):
		self.__x1 = val
		
	def setY1(self, val):
		self.__y1 = val
	
	def setX2(self, val):
		self.__x2 = val
		
	def setY2(self, val):
		self.__y2 = val
	
	def getX1(self):
		return self.__x1
		
	def getY1(self):
		return self.__y1
		
	def getX2(self):
		return self.__x2
		
	def getY2(self):
		return self.__y2
		
	def calcolaDistanza(self):
		return (math.sqrt( ((self.getX2() - self.getX1())**2) + ((self.getY2() - self.getY1())**2) ))
#-----------------------------------------------------------------------------------------------------------------------------------		
def chiediPunto(testo, asse):
	val = input("Inserire coordinata " + testo + " asse " + asse + ": ")
	while (not val.isnumeric()):
		val = input("ERRORE! " + testo + " asse " + asse + ": ")
	return int(val)
#-----------------------------------------------------------------------------------------------------------------------------------
x1 = chiediPunto("punto 1", "X")
y1 = chiediPunto("punto 1", "Y")
x2 = chiediPunto("punto 2", "X")
y2 = chiediPunto("punto 2", "Y")

mieiPunti = punti(x1, y1, x2, y2)
distanza = mieiPunti.calcolaDistanza()
print("Distanza tra i 2 punti: {:2.2f}".format(distanza))

