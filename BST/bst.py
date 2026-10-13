class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == value:
                return False
            if value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp= temp.right

tree = BST()
tree.insert(2)
tree.insert(1)
tree.insert(3)

print("root-->",tree.root.value)
print("left-->",tree.root.left.value)
print("right-->",tree.root.right.value)
