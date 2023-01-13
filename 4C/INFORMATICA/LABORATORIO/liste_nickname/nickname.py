#Bracco Mattia 4C - Creare nickname con i dati inseriti dall'utente

print("Benvenuto nel programma per la creazione dei nickname")

cognome = input("Inserisci il tuo cognome: ")
nome = input("Inserisci il tuo nome: ")
anno = input("Inserisci il tuo anno di nascita: ")
classe = input("Inserisci la tua classe: ")
specializzazione = input("Inserisci la tua specializzazione: ")

nickname = cognome[:3]+nome[:3]+anno[-2:]+"_"+classe+"-"+specializzazione[:3] 
print("Il tuo nickanme è:",nickname)
