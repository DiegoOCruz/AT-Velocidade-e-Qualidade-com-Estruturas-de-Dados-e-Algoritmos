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

    def remover_nos(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, current, value):
        if current is None:  
            return current
        if value < current.value:  
            current.left = self._remove(current.left, value)
        elif value > current.value:  
            current.right = self._remove(current.right, value)
        else:  
            if current.left is None and current.right is None:
                return None
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            min_larger_node = self._get_min(current.right)  
            current.value = min_larger_node.value  
            current.right = self._remove(current.right, min_larger_node.value) 
        return current

    def _get_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current is not None:
            self._inorder(current.left, result) 
            result.append(current.value)        
            self._inorder(current.right, result) 

# Exemplo de uso
if __name__ == "__main__":
    tree = BinaryTree()
  # Inserindo valores
    for value in [45,25,65,20,30,60,70]:
        tree.insercao(value)

    tree.remover_nos(20)
    print("Inorder:", tree.inorder())
    tree.remover_nos(25)
    print("Inorder:", tree.inorder())
    tree.remover_nos(45)
    print("Inorder:", tree.inorder())


