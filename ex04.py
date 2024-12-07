#Algoritimo de busca binária

def busca_binaria(lista, item):
    primeiro_indice = 0
    ultimo_indice = len(lista) - 1

    while primeiro_indice <= ultimo_indice:
        meio = (primeiro_indice + ultimo_indice) // 2
        valor_meio = lista[meio]

        if valor_meio == item:
            return meio
        if valor_meio > item:
            ultimo_indice = meio - 1
        else:
            primeiro_indice = meio + 1
    return None

#aloritimo de busca linear
def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return None
