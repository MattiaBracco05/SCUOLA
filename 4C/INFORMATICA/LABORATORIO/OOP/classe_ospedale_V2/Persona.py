class Persona():
	#Costruttore
	def __init__(self, nome: str, cog: str, cf: str, ds: str):
		self.__nome: str = None
		self.__cognome: str = None
		self.__codiceFiscale: str = None
		self.__dataNascita: str = None
		self.setNome(nome)
		self.setCognome(cog)
		self.setCodiceFiscale(cf)
		self.setDataNascita(ds)

	#Setter
	def setNome(self, n: str):
		if not isinstance(n, str):
			raise TypeError("Il parametro deve essere di tipo str")
		self.__nome = n
		
	def setCognome(self, c):
		if not isinstance(c, str):
			raise TypeError("Il parametro deve essere di tipo str")
		self.__cognome = c
		
	def setCodiceFiscale(self, c):
		if not isinstance(c, str):
			raise TypeError("Il parametro deve essere di tipo str")
		self.__codiceFiscale = c
		
	def setDataNascita(self, d):
		if not isinstance(d, str):
			raise TypeError("Il parametro deve essere di tipo str")
		self.__dataNascita = d

	#Getter
	def getNome(self) -> str:
		return self.__nome
		
	def getCognome(self) -> str:
		return self.__cognome
		
	def getCodicefiscale(self) -> str:
		return self.__codiceFiscale
		
	def getDataNascita(self) -> str:
		return self.__dataNascita
