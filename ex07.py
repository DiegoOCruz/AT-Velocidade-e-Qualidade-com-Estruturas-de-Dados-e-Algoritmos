def verifica_itens(lista):
    hashtable = {} 
    for item in lista:
        if item in hashtable:  
            return True
        hashtable[item] = True  
        #print(hashtable)
    return False

lista = ['Maria', 'João', 'Carlos']
print(verifica_itens(lista))  

lista = ['Maria', 'João', 'Carlos', 'Maria']
print(verifica_itens(lista))  

