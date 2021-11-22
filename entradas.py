from random import randint
from queryTags import queryTags
from queryTrie import *
from queryUserRatings import queryUserRatings
from queryTop import queryTOP
from queryRandom import queryRandom
from queryBottom import queryBottom

def entrada(word:str, players:object, ratings:object, root):

    if word[0:7] == 'players':

        try:
            word = word.replace(" ", "")
            comm = word[0:7]
            prefix = word[7:]
            print(comm)
            print(prefix)

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
            '''
            word = word.replace(" ", "")
            
            
            comm = word[4:].replace("''", '*')
            comm = comm.replace("'", "")
            tags = comm.split("*")
            '''
            comm = word[6:len(word) - 1].replace("''", '*')
            comm = comm.replace("' '", "*")
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

            ratingslist = queryTOP(players.table, position)

            for elemento in ratingslist:
                if N != 0:
                    print(players.query(elemento[0]))
                    N -= 1

        except:
            print("erro")
  
    #pesquisas extras:
    #Formato: bottom<N> ‘<position>’
    elif word[0:6] == 'bottom':

        try:
            word = word.replace("'", "")
            comm = word.split(" ")
            N = int(comm[0][6:])
            position = comm[1]

            rtngslist = queryBottom(players.table, position)

            for elemento in rtngslist:
                if N != 0:
                    print(players.query(elemento[0]))
                    N -= 1

        except:
            print("erro")    

    #Formato: random<N> ‘<position>’ - <list of tags>
    elif word[0:6] == 'random':

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

            if N>len(randlist):
                for id in randlist:
                    print(players.query(id))
            else:
                while N != 0:
                    x = randint(0, len(randlist))
                    print(players.query(randlist[x]))
                    randlist.remove(randlist[x])
                    N -= 1

        except:
            print("erro")


