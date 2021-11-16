word = input("make a research: ")
print(word)

if word[0:6] == 'player':
    comm = word[0:6]
    
elif word[0:4] == 'user':
    
    try:
        id = int(word[4:])
        print(id)
    except:
        print("erro")

elif word[0:4] == 'tags':
   
    try:
        word = word.replace("'", "")
        comm = word.split(" ")
        N = int(comm[0][4:])
        tags = comm[1:]
        print(N)
        print(tags)
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




