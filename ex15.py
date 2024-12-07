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

    def get_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def get_max(self, current):
        while current.right is not None:
            current = current.right
        return current

if __name__ == "__main__":
    tree = BinaryTree()

    # Inserindo valores
    for value in [85,70,95,60,75,90,100]:
        tree.insercao(value)

    print(f'Menor nota: {tree.get_min(tree.root).value}')  # 60
    print(f'Maior nota: {tree.get_max(tree.root).value}')  # 100


