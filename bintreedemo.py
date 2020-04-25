class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, node):
        self.root = node
        self.queue = Queue()

    def traverse_preorder(self, node):
        """order: N-L-R"""
        result = []
        if node == None:
            return result
        else:
            result.append(node.key)
            if node.left != None:
                result += self.traverse_preorder(node.left)
            if node.right != None:
                result += self.traverse_preorder(node.right)
        return result

    def traverse_inorder(self, node):
        """order: L-N-R"""
        result = []
        if node == None:
            return result
        else:
            if node.left != None:
                result += self.traverse_inorder(node.left)
            result.append(node.key)
            if node.right != None:
                result += self.traverse_inorder(node.right)
        return result

    def traverse_postorder(self, node):
        """order: L-R-N"""
        result = []
        if node == None:
            return result
        else:
            if node.left != None:
                result += self.traverse_postorder(node.left)
            if node.right != None:
                result += self.traverse_postorder(node.right)
            result.append(node.key)
        return result

    def traverse_levelorder(self, node):
        if node == None:
            return None
        else:
            self.queue.enqueue(node)

        result = []
        while not self.queue.isEmpty():
            # dequeue a node then process each node
            dnode = self.queue.dequeue()
            result.append(dnode.key.key)

            if dnode.key.left != None:
                # enqueue the left node for later processing
                self.queue.enqueue(dnode.key.left)
            
            if dnode.key.right != None:
                # enqueue the right node for later processing
                self.queue.enqueue(dnode.key.right)

        return result

    def find_node(self, node, key):
        """
        returns a node that has node.key == key
        otherwise returns None
        """
        
        result = None

        if node == None:
            return result
        else:
            if node.key == key:
                return node
            
            if node.left != None:
                return self.find_node(node.left, key)
            if node.right != None:
                return self.find_node(node.right, key)
        return result

class Queue:        
    """
    Uses Singly Linked List to represent a queue (FIFO)
    - enqueue(item): add new item into the queue
    - dequeue(): get an item out of the queue
    - front pointer points to the front (output) of the queue
    - rear pointer points to the rear (input) of the queue
    - front == None && rear == None => empty queue
    """

    class SinglyNode:
        def __init__(self, key):
            self.key = key
            self.next = None
            
    def __init__(self): 
        # initialize an empty queue
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def enqueue(self, item): 
        temp = self.SinglyNode(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def dequeue(self):       
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None

        return temp
    

# Driver code
one = Node("One")
two = Node("Two")
three = Node("Three")
four = Node("Four")
five = Node("Five")
six = Node("Six")

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six

my_tree = BinaryTree(one)
print("\npre-order:")
prorder = my_tree.traverse_preorder(one)
print(prorder)

print("\nin-order:")
inorder = my_tree.traverse_inorder(one)
print(inorder)

print("\npost-order:")
porder = my_tree.traverse_postorder(one)
print(porder)

print("\nlevel-order:")
lorder = my_tree.traverse_levelorder(one)
print(lorder)

n2 = my_tree.find_node(one, "Two")
#print(n2.key)

print("\nlevel-order from node Two:")
lorder = my_tree.traverse_levelorder(n2)
print(lorder)
