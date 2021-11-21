def queryTOP(table, tag):
    found = []

    for player in table:

        try:
            if player[3][0] >= 1000:
                for player_tag in player[2]:
                    if tag == player_tag:
                        elem_1 = player[0]
                        elem_2 = player[3][1]
                        elem = [elem_1, elem_2]
                        found.append(elem)
        except:
            pass

    lista_quicksort(found, len(found))
    found.reverse()

    return found


def lista_quicksort(array, tamanho: int):
    lista_quick_sort(array, 0, tamanho-1)

def lista_quick_sort(array, inicio, fim):
    if fim>inicio:
        p = particionamento(array, inicio, fim)
        lista_quick_sort(array, inicio, p-1)
        lista_quick_sort(array, p+1, fim)

def particionamento(array, inicio, fim):
    x = array[fim][1]
    i = inicio-1
    for j in range(inicio, fim):
        if array[j][1] <= x:
            i += 1
            aux=array[i][1]
            array[i][1]=array[j][1]
            array[j][1]=aux
            aux=array[i][0]
            array[i][0]=array[j][0]
            array[j][0]=aux

    aux = array[i+1][1]
    array[i+1][1] = array[fim][1]
    array[fim][1] = aux
    aux = array[i + 1][0]
    array[i + 1][0] = array[fim][0]
    array[fim][0] = aux

    return (i+1)
