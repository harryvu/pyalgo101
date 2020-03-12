class Node:
    """A singly linked list node."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, data):
        """Insert new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if not (self.head and self.tail):
            self.tail = new_node
        
        self.count += 1

    def append(self, data):
        """Append new node at the end of the list."""
        new_node = Node(data)

        if self.tail: # the list is not empty
            self.tail.next = new_node
            self.tail = new_node
        else: # the list is an empty
            self.head = new_node
            self.tail = new_node

        self.count += 1

    def find(self, data):
        """Find a node by its value."""
        # start from the beginning
        current = self.head

        # iterate through the list
        while current:
            if current.data == data:
                return current

            current = current.next


            

    def iter(self):
        """Iterate through the list"""
        current = self.head

        i = 0
        while current:
            val = current.data
            current = current.next
            yield i, val
            i += 1

