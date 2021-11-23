import csv
from Trie import *

class HashTablePlayers(object):

    #Construtor
    def __init__(self):

        self.size = 258970 + 1  #tamanho é o maior id + 1 -> sem colisões

        #Inicializa a tabela com uma lista
        self.table = [[] for _ in range(self.size)]

    #Função que insere na tabela
    def insertIntoHash(self, playerID:int, name:str, positions:list):
        self.table[playerID] = [playerID, name, positions, [0, 0.0], []]

    #Consulta um player
    def query(self, playerId:int):
        return self.table[playerId]

    #Le o data set e realiza as inserções
    def readDataSet(self, root):

        with open('datasets/players.csv', encoding="utf8") as input:
            playersFile = csv.reader(input, delimiter=",")

            playersFile.__next__() #Skip first line 
            
            for row in playersFile:
                playerID = int(row[0])
                name = str(row[1])
                positions = str(row[2]).split(", ")
                
                self.insertIntoHash(playerID, name, positions)      #Insere dados na tabela
                insertIntoTrie(root, name, playerID)        #Insere nome e id na arvore
        
        input.close()

        print('players.csv DONE!')
        

    #Calcula as medias
    def average(self):
        for i in range(self.size):
           
           #Tenta calcular media, se a entrada estiver vazia, entao pass
            try:

                count = self.table[i][3][0]
                sum_ = self.table[i][3][1]
                self.table[i][3][1] = round(sum_ / count, 6)

            except:
                pass

        print('rating.csv DONE!')
            