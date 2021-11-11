import time
from HashPlayersTable import *  
from HashRatingTable import *
from Trie import *
from threading import Thread

inicio = time.time()

players = HashTablePlayers()
ratings = HashRatingTable()

##Inicializa arvore trie
root = TrieNode('*')
players.readDataSet(root)

t1 = Thread(target=ratings.readDataSet)
t2 = Thread(target=players.ratingCount)
t1.start()
t2.start()
t1.join()
t2.join()


##Tabela Hash <name, player_positions, rating, count>
# players.readDataSet(root) 
# print(time.time() - inicio)
# players.ratingCount()
# players.average()
# print(time.time() - inicio)

# #Tabela Hash de avaliações
# ratings = HashRatingTable()
# ratings.readDataSet()

print(time.time() - inicio)

print(ratings.query(24379))




#Tempo de execução







