from Trie import *
from HashPlayersTable import *
#Pesquisa player <prefix>

def queryOnTrie(players, root, prefix):
    found = []
    tupla = (findPrefix(root, prefix))
    if tupla[0] == True:
        findId(tupla[1], found)

    #Transforma em set para ignorar os repetidos
    found = set(found)          

    return found