class Node:
    """A singly linked list node."""
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def prepend(self, data):
        node = Node(data)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.count += 1

    def append(self, data):
        node = Node(data)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.count += 1

    def print_list(self):
        if self.count > 0:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next
                print('{} :: '.format(curr.data))