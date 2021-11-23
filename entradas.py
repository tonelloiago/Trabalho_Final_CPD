from random import randint
from queryTags import queryTags
from queryTrie import *
from queryUserRatings import queryUserRatings
from queryTop import queryTOP
from queryRandom import queryRandom
from queryBottom import queryBottom
from queryBest import queryBest

def entrada(word:str, players:object, ratings:object, root):
    
    if word[0:7] == 'players':

        queryId = 0

        try:
            word = word.replace(" ", "")
            comm = word[0:7]
            prefix = word[7:]
            print(comm)
            print(prefix)
            
            found = queryOnTrie(root, prefix)
            
            toReturnPlayers = []

            #Pesquisa os id's na tabela hash
            for playerId in found:
                toReturnPlayers.append(players.query(playerId))    

            return queryId, toReturnPlayers

        except:
            pass
        
    elif word[0:4] == 'user':
        
        queryId = 1

        try:
            userId = int(word[4:])
            
            userRtgsList = queryUserRatings(ratings.table, userId)
            userRtgs20 = userRtgsList[:20]
            
            return queryId, userRtgs20
        
        except:
            pass


    elif word[0:3] == 'top':

        queryId = 2

        try:
            word = word.replace("'", "")
            comm = word.split(" ")
            N = int(comm[0][3:])
            position = comm[1]

            ratingslist = queryTOP(players.table, position)

            topPlayers = []

            for elemento in ratingslist:

                if N != 0:
                    topPlayers.append(players.query(elemento[0]))
                    N -= 1
                else:
                    break
            
            print(topPlayers)

            return queryId, topPlayers

        except:
            pass


    elif word[0:4] == 'tags':

        queryId = 3

        try:

            comm = word[6:len(word) - 1].replace("''", '*')
            comm = comm.replace("' '", "*")
            tags = comm.split("*")
            
            tagsList = queryTags(players.table, tags)

            playersWithTags = []

            for playerId in tagsList:
                playersWithTags.append(players.query(playerId))
            
            return queryId, playersWithTags

        except:
            pass

        
  
    #pesquisas extras:
    #Formato: bottom<N> ‘<position>’
    elif word[0:6] == 'bottom':

        queryId = 4

        try:
            word = word.replace("'", "")
            comm = word.split(" ")
            N = int(comm[0][6:])
            position = comm[1]

            bottomList = queryBottom(players.table, position)

            bottomPlayers = []

            for elemento in bottomList:
                if N != 0:
                    bottomPlayers.append(players.query(elemento[0]))
                    N -= 1

            print(bottomPlayers)

            return queryId, bottomPlayers

        except:
            pass  

    #Formato: random<N> ‘<position>’ - <list of tags>
    elif word[0:6] == 'random':

        queryId = 5

        try:

            word2 = word
            word = word[0:word.find("-")].replace("'", "")
            comm = word[0:word.find("-")].split(" ")
            N = int(comm[0][6:])
            position = comm[1]

            word2 = word2[word2.find("-") + 3:len(word2) - 1].replace("''", '*')
            word2 = word2.replace("' '", "*")
            taglist = word2.split("*")

            randlist = queryRandom(players.table, position, taglist)
            randPlayers = []

            if N >= len(randlist):
                for id in randlist:
                    randPlayers.append(players.query(id))
            else:
                while N != 0:
                    x = randint(0, len(randlist))
                    randPlayers.append(players.query(randlist[x]))
                    randlist.remove(randlist[x])
                    N -= 1

            return queryId, randPlayers

        except:
            pass
        
    #Formato: best<N> '<position>' - <list of tags>
    elif word[0:4] == 'best':

        queryId = 6

        try:

            word2 = word
            word = word[0:word.find("-")].replace("'", "")
            comm = word[0:word.find("-")].split(" ")
            N = int(comm[0][4:])
            position = comm[1]

            word2 = word2[word2.find("-") + 3:len(word2) - 1].replace("''", '*')
            word2 = word2.replace("' '", "*")
            taglist = word2.split("*")

            bestlist = queryBest(players.table, position, taglist)
            bestPlayers = []

            for elemento in bestlist:
                if N != 0:
                    bestPlayers.append(players.query(elemento[0]))
                    N -= 1
                else:
                    pass

            return queryId, bestPlayers

        except:
            pass


    else:

        return -1

