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
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    

my_stack = Stack(4)
my_stack.push(3)
my_stack.print_stack()