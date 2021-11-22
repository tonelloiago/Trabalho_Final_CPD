import csv
from HashPlayersTable import *
from HashRatingTable import *

        #Le o arquivo rating.csv e insere as avaliaçoes
def readRatingsFile(players:object, ratings:object):
    
    with open('datasets/rating.csv', encoding="utf8") as input:
        rating = csv.reader(input, delimiter=",")

        rating.__next__() #Skip first line 
        
        for row in rating:
            userID = int(row[0])
            playerID = int(row[1])
            userRating = float(row[2])
            
            #self.insertIntoTable(playerID, userID, userRating)
            players.table[playerID][3][0] += 1             #Incrementa o contador de avaliações
            players.table[playerID][3][1] += userRating    #Soma o rating

            ratings.insert(userID, playerID, userRating)

    #print(ratings.table)
    print('datasets/rating.csv DONE!')
