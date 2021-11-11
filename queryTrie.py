#Pesquisa player <prefix>
found = []
tupla = (findPrefix(root, 'Lionel'))
if tupla[0] == True:
    findId(tupla[1], found)

#Transforma em set para ignorar os repetidos
found = set(found)          

#Pesquisa os id's na tabela hash
for id in found:
    print(players.query(id))