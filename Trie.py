class TrieNode():

    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.sofifa_id = 0
        self.wordEnd = False
        self.counter = 1
        self.leaf = False

#Percorre a arvore e insere o novo nodo
def insertIntoTrie(root, word: str, sofifa_id: int):

    node = root
    for char in word:
        found_in_child = False

        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child

                if node.leaf == True:
                    node.leaf = False

                found_in_child = True
                break
        
        #Cria um novo nodo
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)

            node = new_node

    #Testa se é um nodo folha
    if len(node.children) == 0:
        node.leaf = True

    # Adiciona o campo sofifa_id no ultimo caracter adicionado na arvore trie
    node.sofifa_id = sofifa_id 
    #Seta como final da palavra
    node.wordEnd = True

#Retorna Verdadeiro caso o caminho corresponda ao prefixo
def findPrefix(root, prefix: str):

    node = root

    if not root.children:
        return False, 0

    for char in prefix:
        char_not_found = True

        for child in node.children:
            if child.char == char:

                char_not_found = False

                node = child
                break

        if char_not_found:
            return False, 0

    return True, node

#Retorna os id's correspondentes aos nomes encontrados
def findId (node, found):
    #print(node.char)
    if (node.sofifa_id != 0):
        found.append(node.sofifa_id)
        if (node.leaf == True):
            return

    for child in node.children:
        #print(child.char, child.wordEnd, child.counter, child.leaf)
        if (child.leaf == True):
            found.append(child.sofifa_id)
            break

        if (child.counter != 0 ):
            aux = findId(child, found)
            if aux != 0:
                found.append(aux)
                

    return child.sofifa_id
