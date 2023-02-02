import copy
#-----------------------------------------------------------------------------------------------------------------------------------------------
class punto():

	#costruttore
	def __init__(self, x=0, y=0):
		self.set_x(x)
		self.set_y(y)

	#setter --> usati per l'incapsulamento
	def set_x(self, val):
		self.__x = val
	
	def set_y(self, val):
		self.__y = val
	
	#getter
	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y
		
	#str --> usata per la stampa dell'oggetto
	def __str__(self):
		return "(" + str(self.get_x()) + "," + str(self.get_y()) + ")"
#-----------------------------------------------------------------------------------------------------------------------------------------------
class rettangolo():

	#costruttore
	def __init__(self, altezza, larghezza, oggettoPunto):
		self.set_altezza(altezza)
		self.set_larghezza(larghezza)
		self.set_verticeAS(oggettoPunto)

	#setter --> usati per l'incapsulamento
	def set_altezza(self, val):
		self.__altezza = val

	def set_larghezza(self, val):
		self.__larghezza = val
		
	def set_verticeAS(self, obj):
		self.__verticeAS = obj
	
	#getter	
	def get_altezza(self):
		return self.__altezza

	def get_larghezza(self):
		return self.__larghezza

	def get_verticeAS(self):
		return self.__verticeAS

	#str --> usata per la stampa dell'oggetto
	def __str__(self):
		return "Altezza: " + str(self.get_altezza()) + "\nLarghezza: " + str(self.get_larghezza()) + "\nVertice AS: " + str(self.get_verticeAS())
#-----------------------------------------------------------------------------------------------------------------------------------------------

#CREO UN PUNTO
print("Creo mioPunto")
mioPunto = punto(3,4)
print(mioPunto)

#CREO UN RETTANGOLO CHE HA COME VERTICE AS IL PUNTO APPENA CREATO
print("\nCreo un rettangolo con mioPunto come vertice AS")
rettangolo1 = rettangolo(200, 100, mioPunto)
print(rettangolo1)

#CREO UN SECONDO RETTANGOLO COME ALIAS DEL PRIMO
print("\nCreo rettangolo2 come alias di rettangolo1")
rettangolo2 = rettangolo1
print(rettangolo2)

#IMPOSTO A 7 LA COORDINATA X DEL PUNTO CREATO IN PRECEDENZA --> STAMPO RETTANGOLO 2 (avra come x del punto 7)
print("\nImposto a 7 la coordinata x di mioPunto")
mioPunto.set_x(7)
print(rettangolo2)

#CREO RETTANGOLO 3 COME COPIA INDIPENDENTE DEL PRIMO RETTANGOLO
print("\nCreo rettangolo3 come copia clone indipendente di rettangolo1")
rettangolo3 = copy.copy(rettangolo1)
print(rettangolo3)

#IMPOSTO A 333 L'ALTEZZA DEL PRIMO RETTANGOLO
print("\nImposto a 333 l'altezza di rettangolo1")
rettangolo1.set_altezza(333)
#IMPOSTO A 13 LA COORDINATA Y DEL PUNTO
print("Imposto a 13 la coordinata y di mioPunto")
mioPunto.set_y(13)

#STAPO RETTANGOLO 3 --> (avrà come y del punto 13)
print("\nRettangolo3:")
print(rettangolo3)

#STAMPO RETTANGOLO 1 --> (avrà sia come y del punto 13 sia 333 come valore dell'altezza)
print("\nStampo rettangolo1:")
print(rettangolo1)

