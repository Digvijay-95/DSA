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
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return True

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


dll = DoublyLinkedList(95)
dll.append(96)
dll.append(97)
dll.append(98)
dll.pop()
dll.pop()
dll.pop()
print(dll.pop())
# print(dll.pop())
dll.prepend(69)
dll.print_list()