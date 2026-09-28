class Node:
    def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True

    def pop(self):
        if not self.head:
            return None
        temp = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
        return True

    def pop_first(self):
        if not self.head:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length-=1
        return temp

    def get(self,index):

        if index <0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1 - index): # can also be written as range(self.length-1,index,-1)
                temp = temp.prev
        return temp

    def set_value(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        
        node =self.get(index - 1)
        new_node = Node(value)

        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        new_node.next.prev = new_node

        self.length +=1
        return True






dll = DoublyLinkedList(95)
dll.append(96)
dll.append(97)
dll.append(98)
# dll.pop()
# dll.pop()
# dll.pop()
# print(dll.pop())
# print(dll.pop())
dll.prepend(69)
# print(dll.pop_first().value)
dll.set_value(0,143)
dll.print_list()
print(dll.get(4).value)
