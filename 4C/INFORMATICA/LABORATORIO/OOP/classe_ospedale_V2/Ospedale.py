from typing import List
from Reparto import Reparto
import utilities
#-----------------------------------------------------------------------------------------------------------------------------------
class Ospedale():
	#Costruttore
	def __init__(self, nome: str, rep: List[Reparto] = []):
		self.__nome: str = None
		self.__reparti: List[Reparto] = None
		self.setNome(nome)
		self.setReparti(rep)

	#Setter
	def setNome(self, n: str):
		self.__nome = n	
	
	def setReparti(self, rep: List[Reparto]):
		if not utilities.isCollectionOf(rep, Reparto):
			raise ValueError("Il parametro deve essere una lista di istanze della classe Reparto!")
		self.__reparti = rep
		
	#Getter
	def getNome(self) -> str:
		return self.__nome
	
	def getReparti(self) -> List[Reparto]:
		return self.__reparti

	#Add
	def aggiungiReparti(self, rep: Reparto) -> None:
		if not isinstance(rep, Reparto):
			raise TypeError("Il parametro deve essere una lista di istanze della classe Reparto!")
		self.__reparti.append(rep)
	
	#Rapporto
	def rapporto(self, rep: Reparto) -> float:
		return len(rep.visualizzaPersonale()) / len(rep.visualizzaPazienti())
