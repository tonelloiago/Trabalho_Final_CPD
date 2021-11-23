from queryTop import lista_quicksort

def queryBest(table, position, tags):
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
                        elem_1 = player[0]
                        elem_2 = player[3][1]
                        pl = [elem_1, elem_2]
                        found.append(pl)
                        flag = False
        except:
            pass

    lista_quicksort(found, len(found))
    found.reverse()

    return found