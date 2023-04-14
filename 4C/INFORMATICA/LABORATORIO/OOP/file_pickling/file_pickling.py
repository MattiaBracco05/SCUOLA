#4C Bracco Mattia - File pickling

import os
import pickle

file_attributes = open("test.txt", "wb")
print("Nome del file: ", file_attributes.name)
print("File chiuso o no: ", file_attributes.closed)
print("Modalità apertura: ", file_attributes.mode)
file_attributes.close()
#----------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
#----------------------------------------------------------------------------------------------------------------------------------------------
#Scrivo un file in binario
file_write_bytes = open("test.txt", "wb")
file_write_bytes.write(bytes("Python è un linguaggio spettacolare!", 'UTF-8'))
file_write_bytes.close()

#Leggo il file binario
file_readb = open("test.txt", "rb+")
textb = file_readb.read()
print("La stringa binaria letta è: ", textb)
file_readb.close()

#Scrivo un file in puro ASCII
file_write = open("test.txt", "w")
file_write.write("Python è un linguaggio spettacolare!")
file_write.close()

#Leggo il file ASCII
file_read = open("test.txt", "r+")
text = file_read.read()
print("La stringa letta è: ", text)
file_read.close()

#Append to a file
file_append = open("test.txt", "a")
file_append .write("\nPython è un linguaggio potentissimo.")
file_append.close()

#Leggo il file ASCII
file_read = open("test.txt", "r+")
text = file_read.read()
print("La stringa letta è: ", text)
file_read.close()

#Elimino il file
#os.remove("test.txt)
#----------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
#----------------------------------------------------------------------------------------------------------------------------------------------
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)
#fh.close() #non è obbligatorio perchè chiude in automatico

#Scrivo in una stringa
varpick = pickle.dumps(mylist)
print(varpick)

#Leggo l'oggetto e lo restituisco
mylist_rit = pickle.loads(varpick)
print('Lista recuperata:', mylist_rit)
print('Lista originale: ', mylist)
pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print('Lista letta da file:', emp)
pickle_off.close()
#----------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
#----------------------------------------------------------------------------------------------------------------------------------------------
#Scrivo e leggo un dizionario su un file
#Scrivo
EmpID = {1:"Zack", 2:"53050", 3:"IT", 4:"38", 5:"Flipkart"}
print("Diz originale:", EmpID)
pickling_on = open("EmpID.pickle", "wb")
pickle.dump(EmpID, pickling_on)
pickling_on.close()
#Leggo
pickle_diz = open ("EmpID.pickle", "rb")
diz = pickle.load(pickle_diz)
print("Diz letto da file:", diz)
pickle_diz.close()
