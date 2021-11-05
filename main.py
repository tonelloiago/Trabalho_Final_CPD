import time
from HashTable import *  
from Trie import *
from threading import Thread

inicio = time.time()

players = HashTablePlayers()

#Inicializa arvore trie
root = TrieNode('*')    

#Tabela Hash <name, player_positions, rating, count>
players.readDataSet(root)
players.ratingCount()
players.average()


#Pesquisa player <prefix>
found = []
tupla = (findPrefix(root, 'Lionel'))
if tupla[0] == True:
    findId(tupla[1], found)

#Transforma em set para ignorar os repetidos
found = set(found)          

#Pesquisa os id's na tabela hash
for id in found:
    print(players.query(id))

#Pesquisa top<N> ‘<position>’
#Procurar por posição, ordenar, retornar os <N> melhores

#Tempo de execução
fim = time.time()
print(fim - inicio)






