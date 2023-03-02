import readline
import os

from Ospedale import Ospedale
from Reparto import Reparto
from Paziente import Paziente
from Personale import Personale
from xterminal_text_decoration import *
#-----------------------------------------------------------------------------------------------------------------------------------
def stampaOspedale(osp: Ospedale):
	os.system("clear")
	reparti = osp.getReparti()

	osp_dec = xterm_text_decorator(RGB(255), FOREGROUND, {BOLD})
	rep_dec = xterm_text_decorator(RGB(green=255), FOREGROUND, {BOLD, UNDERLINE})
	pers_dec = xterm_text_decorator(RGB(61, 120, 248), FOREGROUND, {BOLD, UNDERLINE})
	paz_dec = xterm_text_decorator(RGB(168, 45, 138), FOREGROUND, {BOLD, UNDERLINE})

	n = 5

	print(f"{osp_dec}{'OSPEDALE':>50}{RESET}{osp_dec - BOLD}{osp.getNome():>20}{RESET}")
	print()
	
	#Ciclo per i reparti
	for reparto in reparti:
		print()
		print(f"{rep_dec}{'Reparto':<48}{RESET}  {pers_dec}{'Personale':<50}{RESET}{paz_dec}{'Pazienti':<50}{RESET}")
		a = stampaReparto(reparto, n)
		b = stampaPersonale(reparto.visualizzaPersonale(), n)
		c = stampaPazienti(reparto.visualizzaPazienti(), n)
		n = max(a, b, c) + 2
#-----------------------------------------------------------------------------------------------------------------------------------
def stampaPazienti(pazienti: List[Paziente], n):
	t = n
	key_dec = xterm_text_decorator(RGB(255, 255, 255), FOREGROUND, {BOLD})

	#Ciclo per i pazienti
	for paz in pazienti:
		print(f"\x1b[{t};102H{key_dec}{'Nome':<30}{RESET}{paz.getNome(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};102H{key_dec}{'Cognome':<30}{RESET}{paz.getCognome(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};102H{key_dec}{'Codice fiscale':<30}{RESET}{paz.getCodicefiscale(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};102H{key_dec}{'Data di nascita':<30}{RESET}{paz.getDataNascita(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};102H{key_dec}{'Motivo ricovero':<30}{RESET}{paz.getMotivoRicovero(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};102H{key_dec}{'Data ricovero':<30}{RESET}{paz.getDataRicovero(): <20}", sep="")
		t += 2

	return t
#-----------------------------------------------------------------------------------------------------------------------------------
def stampaReparto(rep: Reparto, n: int):
	t = n
	key_dec = xterm_text_decorator(RGB(255, 255, 255), FOREGROUND, {BOLD})

	#Stampo i dati del reparto
	print(f"\x1b[{t};1H{key_dec}{'Nome': <30}{RESET}{rep.getDenominazione():<20}", sep="")
	t += 1
	print(f"\x1b[{t};1H{key_dec}{'Max Letti': <30}{RESET}{rep.getNLetti():<20}", sep="")
	t += 1
	print(f"\x1b[{t};1H{key_dec}{'Letti occupati': <30}{RESET}{rep.getLetti():<20}", sep="")
	t += 2

	return t
#-----------------------------------------------------------------------------------------------------------------------------------
def stampaPersonale(pers: List[Personale], n: int):
	t = n
	key_dec = xterm_text_decorator(RGB(255, 255, 255), FOREGROUND, {BOLD})

	#Ciclo per il personale
	for per in pers:
		print(f"\x1b[{t};52H{key_dec}{'Nome':<30}{RESET}{per.getNome(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};52H{key_dec}{'Cognome':<30}{RESET}{per.getCognome(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};52H{key_dec}{'Codice fiscale':<30}{RESET}{per.getCodicefiscale(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};52H{key_dec}{'Data di nascita':<30}{RESET}{per.getDataNascita(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};52H{key_dec}{'Matricola':<30}{RESET}{per.getMatricola(): <20}", sep="")
		t += 1
		print(f"\x1b[{t};52H{key_dec}{'Liv Qualifica':<30}{RESET}{per.getLivelloQualifica(): <20}", sep="")
		t += 2

	return t
#-----------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

	ospedale = Ospedale("Regina Margherita")
	
	#Creo i reparti
	medicina = Reparto("Medicina", 12)
	chirurgia = Reparto("Chirurgia", 12)
	ortopedia = Reparto("Ortopedia", 12)

	#Creo il personale
	p1 = Personale("Mario", "Rossi", "sadfasff", "12/12/2012", "dsfafsd", 3, medicina)
	p2 = Personale("c", "d", "sadfasff", "12/12/2012", "dsfafsd", 3, chirurgia)
	p3 = Personale("e", "f", "sadfasff", "12/12/2012", "dsfafsd", 3, ortopedia)

	#Creo i pazienti
	paz1 = Paziente("g", "h", "sddfasfd", "13/12/2012", "sadfsad", "12/12/2022")
	paz2 = Paziente("g", "h", "sddfasfd", "13/12/2012", "sadfsad", "12/12/2022")
	paz3 = Paziente("g", "h", "sddfasfd", "13/12/2012", "sadfsad", "12/12/2022")

	#Aggiungo il personale ai reparti
	medicina.addPersonale(p1)
	chirurgia.addPersonale(p2)
	ortopedia.addPersonale(p3)

	#Registro i pazienti
	medicina.registraPaziente(paz1)
	chirurgia.registraPaziente(paz2)
	ortopedia.registraPaziente(paz3)

	medicina.registraPaziente(paz1)
	chirurgia.registraPaziente(paz2)
	ortopedia.registraPaziente(paz3)

	#Setto i reparti dell'ospedale
	ospedale.setReparti([medicina, chirurgia, ortopedia])

	#Stampo l'ospedale
	stampaOspedale(ospedale)
