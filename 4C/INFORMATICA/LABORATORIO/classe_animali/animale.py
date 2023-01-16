#4C Bracco Mattia

class animale(object):
	#costruttore
	def __init__(self, nome = 0, peso = 0, sesso = 0, verso = 0):
		self.setNome(nome)
		self.setPeso(peso)
		self.setSesso(sesso)
		self.setVerso(verso)
		
	#setter
	def setNome(self, a):
		self.__nome = a
	
	def setPeso(self, b):
		self.__peso = b
		
	def setSesso(self, c):
		self.__sesso = c
		
	def setVerso(self, d):
		self.__verso = d
	
	#getter
	def getNome(self):
		return self.__nome
		
	def getPeso(self):
		return self.__peso	
		
	def getSesso(self):
		return self.__sesso
		
	def getVerso(self):
		return self.__verso
		
	#interrogazione	
	def interrogazione(self):
		print("Nome:", self.getNome(), "\nPeso:", str(self.getPeso()), "\nSesso:", self.getSesso(), "\nVerso:", self.getVerso())
		
#----------------------------------------------------------------------------------------------------------------------------------------------
for i in range(4):
	mioAnimale = animale()
	mioAnimale.setNome(input("Inserisci il nome dell'animale: "))
	peso = "a"
	while peso.isalpha():
		peso = (input("Inserisci il peso dell'animale: "))
	mioAnimale.setPeso(int(peso))
	mioAnimale.setSesso(input("Inserisi il sesso dell'animale: "))
	mioAnimale.setVerso(input("Inserisci il verso dell'animale: "))
	mioAnimale.interrogazione()
