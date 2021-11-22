from HashPlayersTable import HashTablePlayers
from HashRatingTable import HashRatingTable
from Trie import TrieNode
from hashTagsTable import *
from threading import Thread
import time



def preProcessing(players, ratings, root):
    inicio = time.time()


    players.readDataSet(root)

    #Inicializa as threads para realizar as duas leituras de rating
    t1 = Thread(target=ratings.readDataSet)
    t2 = Thread(target=players.ratingCount)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    #tentar juntar as inserções na players
    players.average()
    players.table = readTags(players.table)

    print(time.time() - inicio)


    return players, ratings, root    




