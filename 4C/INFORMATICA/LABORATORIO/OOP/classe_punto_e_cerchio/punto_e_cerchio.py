#4C Bracco Mattia - Classi punto e cerchio

import math
import copy
#----------------------------------------------------------------------------------------------------------------------------------------------
class punto():

	#costruttore
	def __init__(self, x=0, y=0):
		self.set_x(x)
		self.set_y(y)

	#setter
	def set_x(self, val):
		self.__x = val
	
	def set_y(self, val):
		self.__y = val
	
	#getter
	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y
		
	#str
	def __str__(self):
		return "(" + str(self.get_x()) + "," + str(self.get_y()) + ")"
#----------------------------------------------------------------------------------------------------------------------------------------------		
class cerchio():

	#costruttore
	def __init__(self, puntoCentro, raggio):
		self.setCentro(puntoCentro)
		self.setRaggio(raggio)
		
	#setter
	def setCentro(self, obj):
		self.__centro = obj
	
	def setRaggio(self, val):
		self.__raggio = val
		
	#getter
	def getCentro(self):
		return self.__centro
		
	def getRaggio(self):
		return self.__raggio
		
	#str
	def __str__(self):
		return "Centro: " + str(self.getCentro()) + "\nRaggio: " + str(self.getRaggio())
#----------------------------------------------------------------------------------------------------------------------------------------------
class rettangolo():

	#costruttore
	def __init__(self, altezza, larghezza):
		self.setAltezza(altezza)
		self.setLarghezza(larghezza)

	#setter
	def setAltezza(self, val):
		self.__altezza = val

	def setLarghezza(self, val):
		self.__larghezza = val
	
	#getter	
	def getAltezza(self):
		return self.__altezza

	def getLarghezza(self):
		return self.__larghezza

	#str
	def __str__(self):
		return "Altezza: " + str(self.getAltezza()) + "\nLarghezza: " + str(self.getLarghezza())
#----------------------------------------------------------------------------------------------------------------------------------------------		
def puntoNelCerchio(cerchio, punto):
	print("\nFUNZIONE PUNTO NEL CERCHIO")
	p1 = punto
	p2 = cerchio.getCentro()
	print("Punto: " + str(p1))
	print("Centro: " + str(p2))
	distanza = math.dist(p1, p2)
#----------------------------------------------------------------------------------------------------------------------------------------------
def rettangoloNelCerchio(cerchio, rettangolo):
	print("\nFUNZIONE RETTANGOLO NEL CERCHIO")
#----------------------------------------------------------------------------------------------------------------------------------------------
def rettangoloSovrapposto(cerchio, rettangolo):
	print("\nFUNZIONE RETTANGOLO SOVRAPPOSTO AL CERCHIO")
#----------------------------------------------------------------------------------------------------------------------------------------------
#PUNTO CENTRO DEL CERCHIO
print("mioPunto:")
mioPunto = punto(150, 100)
print(mioPunto)

#CREO UN CERCHIO CHE HA "mioPunto" COME CENTRO
print("\nmioCerchio:")
mioCerchio = cerchio(mioPunto, 75)
print(mioCerchio)

#CREO UN RETTANGOLO
print("\nmioRettangolo:")
mioRettangolo = rettangolo(10, 10)
print(mioRettangolo)

#CREO UN SECONDO PUNTO
print("mioPunto:")
mioPunto2 = punto(100, 100)
print(mioPunto2)

puntoNelCerchio(mioCerchio, mioPunto2)
