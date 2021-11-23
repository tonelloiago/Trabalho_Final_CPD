from HashPlayersTable import *
from HashRatingTable import *
from Trie import *
from hashTagsTable import *
from readRatings import *
import time


def preProcessing(players:object, ratings:object, root):
    inicio = time.time()

    #Cria a tabela de players
    players.readDataSet(root)

    #Faz a leitura do ratings.csv
    readRatingsFile(players, ratings)
    
    #Calcula as medias
    players.average()

    #faz a leitura das tags
    players.table = readTags(players.table)

    print(time.time() - inicio)





