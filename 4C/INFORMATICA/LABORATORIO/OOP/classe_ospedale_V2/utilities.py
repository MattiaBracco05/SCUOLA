from __future__ import annotations
from collections.abc import Iterable
#------------------------------------------------------------------------------------------------------------------------------------
def getNotEmptyStr(m: str, v: str) -> str:
	s = input(m)
	while len(s.strip()) == 0:
		s = input(f"{v} inserito non deve essere vuoto, rinserisci: ")
	return s
#------------------------------------------------------------------------------------------------------------------------------------
def getPositiveNum(m: str, v: str = "Inserisci un numero positivo: ", c: type = int):
	s = input(m)

	while True:
		try:
			return c(s)
		except:
			s = input(v)
#------------------------------------------------------------------------------------------------------------------------------------
def isPositiveNum(n: int | float) -> bool:
	if isinstance(n, (int, float)):
		if n < 0:
			return False
		else:
			return True
	else:
		raise TypeError(f"Except number found {type(n)}")
#------------------------------------------------------------------------------------------------------------------------------------
def getBool(m: str, tr: str = "true", fs: str = "false") -> bool:
	s = input(m)

	while True:
		if s.lower() == tr:
			return True
		elif s.lower() == fs:
			return False
		else:
			s = input(f"Inserisci {tr} o {fs}: ")
#------------------------------------------------------------------------------------------------------------------------------------
def isEmptyStr(m: str) -> bool:
	if isinstance(m, str):
		if len(m) != 0:
			return False
		else:
			return True
	else:
		raise TypeError(f"Except str found {type(m)}")
#------------------------------------------------------------------------------------------------------------------------------------
def isCollectionOf(l: Iterable, t: type) -> bool:
	if not issubclass(type(l), Iterable):
		raise TypeError("[l] is not Iterable")

	if not isinstance(t, type):
		raise TypeError("[t] must be a type class")

	for e in l:
		if not issubclass(type(e), t):
			return False

	return True
