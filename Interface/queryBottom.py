from queryTop import lista_quicksort

'''
queryBottom
Recebe uma 'HashTablePLayers' e uma 'tag' (posição) no formato:
    tag: string
A função verifica se, para todo jogador na hash table, tem mais de 1000
avaliações e joga na mesma posição indicada pelo parâmetro. Se sim, anexar
na lista 'found' o seu 'id' e a sua 'avaliação global'.
Logo após, organizar essa lista em ordem crescente de 'avaliação global' e devolver.
'''

def queryBottom(table, tag):
    found = []

    for player in table:

        try:
            if player[3][0] >= 500:
                for player_tag in player[2]:
                    if tag == player_tag:
                        elem_1 = player[0]
                        elem_2 = player[3][1]
                        elem = [elem_1, elem_2]
                        found.append(elem)
        except:
            pass

    lista_quicksort(found, len(found))

    return found