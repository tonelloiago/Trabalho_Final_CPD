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


    def readDataSet(self):

        with open('datasets/minirating.csv', encoding="utf8") as input:
            playersFile = csv.reader(input, delimiter=",")

            playersFile.__next__() #Skip first line 
            
            for row in playersFile:
                userID = int(row[0])
                playerID = int(row[1])
                rating = float(row[2])
                
                self.insert(userID, playerID, rating)

        print('backend/ratings.csv DONE!')


