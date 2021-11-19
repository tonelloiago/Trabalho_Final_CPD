from preprocessing import *
from entradas import *

players, ratings, root = preProcessing()

i_want = True

while i_want:

    print()
    command = str(input("Comando:"))
    print()
    
    entrada(command, players, ratings, root)
