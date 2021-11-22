'''
queryRandom
Recebe uma 'table', uma 'position' e uma 'tags' no formato:
    table: HashTablePlayers
    position: string, que representa a posição do jogador
    tag: lista de strings, que representa as tags
A função procura na 'table' todos os jogadores que satisfazem a position e as tags. Se satisfaz, junta o 'id' do
jogador com a lista de saída.
'''

def queryRandom(table, position, tags):
    found = []

    for player in table:
        try:
            for pos in player[2]:
                if pos == position:
                    for tag in tags:
                        try:
                            if tag in player[4]:
                                flag = True
                            else:
                                flag = False
                                break
                        except:
                            pass

                    if flag:
                        found.append(player[0])
                        flag = False
        except:
            pass
    return found