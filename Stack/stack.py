class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def push(self,value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.length+=1
        return True
    
    def pop(self):
        if not self.top:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -=1
        return temp
    
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    

my_stack = Stack(4)
my_stack.push(3)
print("popped -->",my_stack.pop().value)
my_stack.print_stack()