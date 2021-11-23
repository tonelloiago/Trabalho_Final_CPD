'''NÃO É UMA CLASSE'''

import csv

#Insere as tags na tabelas hash de players
def insertTagsOnPlayers(playersTable, sofifa_id, tag):
    
    playersTable[sofifa_id][4].append(tag)

    return playersTable


#Le as tags do arquivo tags.csv
def readTags(playersTable):

        with open('datasets/tags.csv', encoding="utf8") as input:
            tagsFile = csv.reader(input, delimiter=",")

            tagsFile.__next__() #Skip first line 
            
            for row in tagsFile:
                
                sofifa_id = int(row[1])
                tag = str(row[2])
                
                playersTable = insertTagsOnPlayers(playersTable, sofifa_id, tag)

        input.close()

        print('tags.csv DONE!')
        return playersTable
        