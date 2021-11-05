import csv
from Trie import *

class HashTablePlayers(object):

    #Constructor
    def __init__(self):

        self.size = 258970 + 1

        #Initialize table
        self.table = [[] for _ in range(self.size)]

    def insertIntoTable(self, playerID:int, name:str, positions:list):
        self.table[playerID] = [playerID, name, positions, [0, 0.0]]


    def query(self, playerId:int):
        return self.table[playerId]


    def readDataSet(self, root):

        with open('backend/datasets/players.csv', encoding="utf8") as input:
            playersFile = csv.reader(input, delimiter=",")

            playersFile.__next__() #Skip first line 
            
            for row in playersFile:
                playerID = int(row[0])
                name = str(row[1])
                positions = str(row[2]).split(", ")
                
                self.insertIntoTable(playerID, name, positions)
                insertIntoTrie(root, name, playerID)


        print(self.table[135507])
        #print(self.table[int(20801)])
        #print(self.table[int(241461)])

        print('backend/players.csv DONE!')


    def ratingCount(self):
        
        with open('backend/datasets/rating.csv', encoding="utf8") as input:
            rating = csv.reader(input, delimiter=",")

            rating.__next__() #Skip first line 
            
            for row in rating:
                userID = int(row[0])
                playerID = int(row[1])
                userRating = float(row[2])
                
                #self.insertIntoTable(playerID, userID, userRating)
                self.table[playerID][3][0] += 1
                self.table[playerID][3][1] += userRating

        
    def average(self):
        for i in range(self.size):
           
           #Tenta calcular media, se a entrada estiver vazia, entao pass
            try:

                count = self.table[i][3][0]
                sum = self.table[i][3][1]
                self.table[i][3] = round(sum / count, 6)

            except:
                pass


        print(self.table[int(158023)])
        print(self.table[int(20801)])
        print(self.table[int(241461)])


        print('backend/ratings.csv DONE!')
            