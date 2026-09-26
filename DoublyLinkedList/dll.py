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

dll = DoublyLinkedList(95)

dll.print_list()