class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   

class BinaryTree:
    def __init__(self):
        self.root = None  

    def add(self, value):
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

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value
    
    def find_max(self):
        if self.root is None:
            return None  
        current = self.root
        while current.right:
            current = current.right
        return current.value

bst = BinaryTree()
prices = [85, 70, 95, 60, 75, 90, 100]

for price in prices:
    bst.add(price)

print("Nota mínima:", bst.find_min())
print("Nota máxima:", bst.find_max())