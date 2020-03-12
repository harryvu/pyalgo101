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

    def _find_prev(self,data):
        """Find the node before (previous)."""
        
        # set the stage
        previous = None
        current = self.head

        # iterate through the list
        while current:
            # if found then return the previous node
            if current.data == data:
                return previous
            
            # set the previous to current node
            # then move the current to the next node
            previous = current
            current = current.next

        # could not find the node, so return None
        return None

    def delete(self, data):
        """Delete a node by its value."""

        prev = self._find_prev(data)
        node_tobe_deleted = prev.next

        # point the prev node to the node after the node_tobe_deleted
        prev.next = node_tobe_deleted.next
        # point the node_tobe_deleted to None
        node_tobe_deleted.next = None
        # then free
        node_tobe_deleted = None
        # if you want to totally delete the variable use del
        # del node_tobe_deleted
        # https://andreasbergstrom.com/posts/python-del-vs-assign-none/

        # decrease node count by one
        self.count -= 1
    
    def iter(self):
        """Iterate through the list"""
        current = self.head

        i = 0
        while current:
            val = current.data
            current = current.next
            yield i, val
            i += 1

