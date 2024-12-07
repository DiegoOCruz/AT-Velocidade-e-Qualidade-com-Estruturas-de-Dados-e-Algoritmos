class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None    
        self.right = None   

class BinaryTree:
    def __init__(self):
        self.root = None 

    def insercao(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, current, value):
        if value < current.value: 
            if current.left is None:
                current.left = Node(value)
            else:
                self._add(current.left, value)
        else: 
            if current.right is None:
                current.right = Node(value)
            else:
                self._add(current.right, value)

    def busca(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if current.value == value: 
            return True
        if value < current.value: 
            return self._search(current.left, value)
        else: 
            return self._search(current.right, value)

if __name__ == "__main__":
    tree = BinaryTree()

    # Inserindo valores
    for value in [100,50,150,30,70,130,170]:
        tree.insercao(value)
        
    # Buscar valores
print("Buscar 70:", "valor disponível" if tree.busca(70) else "valor não disponível")  # Saída: valor disponível
print("Buscar 20:", "valor disponível" if tree.busca(20) else "valor não disponível")  # Saída: valor não disponível

