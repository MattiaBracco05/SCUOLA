from __future__ import annotations
from Paziente import Paziente
from Personale import Personale
from typing import List
import utilities
#-----------------------------------------------------------------------------------------------------------------------------------
class Reparto():
	def __init__(self, den: str, nl: int, per=None, paz=None):
		if per is None:
			per = []
		if paz is None:
			paz = []
		self.__denominazione: str = None
		self.__nLetti: int = None
		self.__personale: List[Personale] = None
		self.__pazienti: List[Paziente] = None
		self.__letti: int = 0

		self.setDenominazione(den)
		self.setNLetti(nl)
		self.setPazienti(paz)
		self.setPersonali(per)

	#Setter
	def setPazienti(self, paz: List[Paziente]) -> bool | None:
		if not utilities.isCollectionOf(paz, Paziente):
			raise ValueError("Il paraemtro deve essere un istanza della classe paziente")
		if self.__setLetti(-(len(paz))) != None:
			return False
		self.__pazienti = paz

	def setPersonali(self, per: List[Personale]):
		if not utilities.isCollectionOf(per, Personale):
			raise ValueError("Il parametro deve essere un istanza della classe Personale")
		self.__personale = per

	def __setLetti(self, n: int) -> bool | None:
		if self.getNLetti() is None:
			raise ValueError("nLetti non inizializzato")
		if not isinstance(n, int):
			raise TypeError("Il parametro n deve essere di tipo int")
		if n + self.__letti < 0:
			return False
		self.__letti += n 

	def setNLetti(self, nl: int):
		if not isinstance(nl, int):
			raise TypeError("Il parametro deve essere di tipo int")
		self.__nLetti = nl

	def setDenominazione(self, den: str):
		if not isinstance(den, str):
			raise TypeError("Il parametro deve essere di tipo str")
		self.__denominazione = den

	#Getter
	def getLetti(self) -> int:
		return self.__letti
	
	def getDenominazione(self) -> str:
		return self.__denominazione
	
	def getNLetti(self) -> int:
		return self.__nLetti
	
	#Add
	def addPersonale(self, per: Personale):
		if not isinstance(per, Personale):
			raise TypeError("Il parametro deve essere un istanza della classe Personale")
		self.__personale.append(per)
		
	def __addLetto(self) -> None | bool:
		if self.getNLetti() is None:
			raise ValueError("nLetti non inizializzato")
		if self.getLetti() > self.getNLetti():
			return False
		self.__letti += 1
	
	#Del
	def __delLetto(self) -> None | bool:
		if self.getLetti() == 0:
			return False
		self.__letti -= 1

	#Visualizza	
	def visualizzaPersonale(self) -> List[Personale]:
		return self.__personale
	
	def visualizzaPazienti(self) -> List[Paziente]:
		return self.__pazienti
	
	#Registra paziente
	def registraPaziente(self, paz: Paziente):
		if not isinstance(paz, Paziente):
			raise TypeError("Parameter paz of method registraPaziente() must be an instance of class Paziente")
		self.__pazienti.append(paz)
	
	#Dimetti paziente
	def dimettiPaziente(self, paz: Paziente) -> Paziente | None:
		if paz in self.__pazienti:
			self.__delLetto()
			return self.__pazienti.pop(self.__pazienti.index(paz))
