from Persona import Persona

class Personale(Persona):
	def __init__(self, nome: str, cog: str, cf: str, ds: str, m: str, lq: int, r):
		super().__init__(nome, cog, cf, ds)

		self.__matricola: str = None
		self.__livelloQualifica: int = None
		self.__reparto = None

		self.setMatricola(m)
		self.setLivelloQualifica(lq)
		self.setReparto(r)

	def getMatricola(self) -> str:
		return self.__matricola
	
	def getLivelloQualifica(self) -> int:
		return self.__livelloQualifica
	
	def getReparto(self):
		return self.__reparto
	
	def setReparto(self, r):
		self.__reparto = r

	def setMatricola(self, m: str):
		if not isinstance(m, str):
			raise TypeError("Parameter m of method setMatricola() must be an instance of class str")
		
		self.__matricola = m

	def setLivelloQualifica(self, q: int):
		if not isinstance(q, int):
			raise TypeError("Parameter q of method setLivelloQualifica() must be an instance of class int")
		
		self.__livelloQualifica = q