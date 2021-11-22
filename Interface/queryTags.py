def queryTags(table, tags):
    found = []
    flag = False

    #Para cada jogador na tabela
    for player in table:
        for tag in tags:    #Para cada tag em tags

            try:            #Tenta, caso a lista esteja vazia passa
                if tag in player[4]:    #Se a tag existem na lista de tags
                    flag = True          
                else:
                    flag = False
                    break
            except:
                pass

        if flag:   #Caso todas as tags sejam encontradas, salva o id do jogador
            found.append(player[0])
            flag = False

    return found