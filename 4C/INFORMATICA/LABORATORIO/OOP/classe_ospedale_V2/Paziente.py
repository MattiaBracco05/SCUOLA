from Persona import Persona
#-----------------------------------------------------------------------------------------------------------------------------------
class Paziente(Persona):
	#Costruttore
	def __init__(self, nome: str, cog: str, cf: str, ds: str, mr: str, dr: str):
		super().__init__(nome, cog, cf, ds)
		self.__motivoRicovero: str = None
		self.__dataRicovero: str = None
		self.setMotivoRicovero(mr)
		self.setDataRicovero(dr)
	
	#Setter
	def setMotivoRicovero(self, m: str):
		if not isinstance(m, str):
			raise TypeError("Il parametro deve essere di tipo str")
		self.__motivoRicovero = m
	
	def setDataRicovero(self, m: str):
		if not isinstance(m, str):
			raise TypeError("Il parametro deve essere di tipo str")
		self.__dataRicovero = m
	
	#Getter
	def getMotivoRicovero(self) -> str:
		return self.__motivoRicovero
	
	def getDataRicovero(self) -> str:
		return self.__dataRicovero
