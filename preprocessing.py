from HashPlayersTable import *  
from HashRatingTable import *
from HashTagsTable import *
from Trie import *
from threading import Thread
import time


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

players.table = readTags(players.table)

print(time.time() - inicio)

    







