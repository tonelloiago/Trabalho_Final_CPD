from queryTags import queryTags
from queryTrie import *
from queryUserRatings import queryUserRatings


def entrada(word:str, players:object, ratings:object, root):
    if word[0:6] == 'player':

        try:
            word = word.replace(" ", "")
            comm = word[0:6]
            prefix = word[6:]

            found = queryOnTrie(players, root, prefix)

                #Pesquisa os id's na tabela hash
            for id in found:
                print(players.query(id))

        
        except:
            pass
        
    elif word[0:4] == 'user':
        
        try:
            id = int(word[4:])
            
            userRtgsList = queryUserRatings(ratings.table, id)

            print(userRtgsList)

        except:
            print("erro")

    elif word[0:4] == 'tags':
    
        try:
            word = word.replace(" ", "")
            #tags'a''b'
            
            comm = word[4:].replace("''", '*')
            comm = comm.replace("'", "")
            tags = comm.split("*")

            tagsList = queryTags(players.table, tags)

            for id in tagsList:
                print(players.query(id))
                print('\n')

        except:
            pass


    elif word[0:3] == 'top':

        try:
            word = word.replace("'", "")
            comm = word.split(" ")
            N = int(comm[0][3:])
            position = comm[1]
            print(N)
            print(position)
            

        except:
            print("erro")




