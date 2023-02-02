class Time:
    """Classe tempo"""
#----------------------------------------------------------------------------------------------------------------------------------------------
def stampaTempo(t):
    print('%.2d:%.2d:%.2d' % (t.ore, t.minuti, t.secondi))

#----------------------------------------------------------------------------------------------------------------------------------------------
def intInTempo(secondis):
    time = Time()
    minutis, time.secondi = divmod(secondis, 60)
    time.ore, time.minuti = divmod(minutis, 60)
    return time
#----------------------------------------------------------------------------------------------------------------------------------------------
def tempoInInt(time):
    minutis = time.ore * 60 + time.minuti
    secondi = minutis * 60 + time.secondi
    return secondi
#----------------------------------------------------------------------------------------------------------------------------------------------
def aggiungiTempo(t1, t2):
    assert validaTempo(t1) and validaTempo(t2)
    secondi = tempoInInt(t1) + tempoInInt(t2)
    return intInTempo(secondi)
#----------------------------------------------------------------------------------------------------------------------------------------------
def validaTempo(time):
    if time.ore < 0 or time.minuti < 0 or time.secondi < 0:
        return False
    if time.minuti >= 60 or time.secondi >= 60:
        return False
    return True
#----------------------------------------------------------------------------------------------------------------------------------------------

#ORA DI INIZIO
mioTempo = Time()
mioTempo.ore = 12
mioTempo.minuti = 0
mioTempo.secondi = 0
print('Inzio:', end=' ')
stampaTempo(mioTempo)

#DURATA
durataFilm = 109 #durata in minuti
tempoDurata = intInTempo(durataFilm * 60) #durata trasformata
print('Esecuzione:', end=' ')
stampaTempo(tempoDurata)

#ORA DI FINE
tempoFine = aggiungiTempo(mioTempo, tempoDurata)
print('Fine:', end=' ')
stampaTempo(tempoFine)
