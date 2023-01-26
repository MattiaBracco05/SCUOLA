#4C Bracco Mattia - passare parametri tramite linea di comando eseguendo il file

import sys

lato = int(sys.argv[1])
print("Perimetro:", (lato*4))

print("Secondo parametro:", sys.argv[2])
