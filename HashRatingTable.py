import csv
from Trie import *

class HashRatingTable(object):

    #Constructor
    def __init__(self):

        self.size = 138493 + 1          #Maior id + 1

        #Inicializa a tabela
        self.table = [[] for _ in range(self.size)]


    def insert(self, userId:int,  playerID:int, rating:float):
        self.table[userId].append([playerID, rating])


    def query(self, userID:int):
        return self.table[userID]





