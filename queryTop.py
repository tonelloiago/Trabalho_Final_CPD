'''
queryTOP
Recebe uma 'HashTablePLayers' e uma 'tag' (posição) no formato:
    tag: string
A função verifica se, para todo jogador na hash table, tem mais de 1000
avaliações e joga na mesma posição indicada pelo parâmetro. Se sim, anexar
na lista 'found' o seu 'id' e a sua 'avaliação global'.
Logo após, organizar essa lista em ordem decrescente de 'avaliação global' e devolver.
'''

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


''' 
lista_quicksort
Recebe uma lista e um número no formato:
    lista: list - lista de listas com 2 números inteiros
    número: número inteiro - tamanho da lista
Essa função chama a função 'lista_quick_sort'.
'''
def lista_quicksort(array, tamanho: int):
    lista_quick_sort(array, 0, tamanho-1)

    
''' 
lista_quick_sort
Recebe uma lista e dois números no formato:
    lista: list - lista de listas com 2 números inteiros
    número 1: número inteiro - índice de início da lista
    número 2: número inteiro - índice de fim de lista
A função faz, enquanto o 'número 2' for maior do que o 'número 1',
duas chamadas recursivas com as duas metades da lista.
'''
def lista_quick_sort(array, inicio, fim):
    if fim>inicio:
        p = particionamento(array, inicio, fim)
        lista_quick_sort(array, inicio, p-1)
        lista_quick_sort(array, p+1, fim)

''' 
particionamento
Recebe uma lista e dois números no formato:
    lista: list - lista de listas com 2 números inteiros
    número 1: número inteiro - índice de início da lista
    número 2: número inteiro - índice de fim de lista
A função faz o particionamento com o segundo índice de cada elemento da lista,
deixando os elementos menores que o particionador (número 2) à sua esquerda
e os elementos maiores à sua direita. A função retorna o índice do elemento particionador
(particionamento de Lomuto).
'''
        
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
