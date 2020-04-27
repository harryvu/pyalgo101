class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self, node):
        self.root = node
        self.pq = Queue()
        self.seen = [] # save processed nodes here

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
            self.pq.enqueue(node)

        result = []
        while not self.pq.isEmpty():
            # dequeue a node then process each node
            dnode = self.pq.dequeue()
            result.append(dnode.key.key)

            if dnode.key.left != None:
                # enqueue the left node for later processing
                self.pq.enqueue(dnode.key.left)
            
            if dnode.key.right != None:
                # enqueue the right node for later processing
                self.pq.enqueue(dnode.key.right)

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

    def find_nodes_at_distance(self, node, k, stopAt):
        """
        find node at k distance from a specified node
        both down/up the tree
        """

        class Bucket:
            """
            This Bucket will be used as a container
            to put node + the step in the same bucket
            before enqueue to a processing queue (pq)
            """
            def __init__(self, node, step):
                self.node = node
                self.step = step

        results = [] # save all results here, starts with an empty list
        #k is the number of steps from the specified node
        if k == 0 and node != None:
            # we are at the start node
            self.pq.clear()
            self.seen.clear()
            self.pq.enqueue(Bucket(node,0))

        while not self.pq.isEmpty():
            bucket = self.pq.dequeue()
            self.seen.append(bucket.key.node.key)
            step = bucket.key.step
            
            if step < stopAt:
                if (bucket.key.node.left != None) and (bucket.key.node.left.key not in self.seen):
                    self.pq.enqueue(Bucket(bucket.key.node.left,step+1))
                if (bucket.key.node.right != None) and (bucket.key.node.right.key not in self.seen):
                    self.pq.enqueue(Bucket(bucket.key.node.right,step+1))
                if (bucket.key.node.parent != None) and (bucket.key.node.parent.key not in self.seen):
                    self.pq.enqueue(Bucket(bucket.key.node.parent,step+1))
            if step == stopAt:
                results.append(bucket.key.node.key)

        return results    

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
    
    def clear(self):
        self.front = self.rear = None


# Driver code
one = Node("One")
two = Node("Two")
three = Node("Three")
four = Node("Four")
five = Node("Five")
six = Node("Six")
seven = Node('Seven')
nine = Node('Nine')

#one.parent == None
one.left = two
one.right = three

two.parent = one
two.left = four
two.right = five

three.parent = one
three.left = six

four.parent = two

five.parent = two
five.left = seven

seven.parent = five
seven.left = nine

nine.parent = seven

six.parent = three



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

print('find_node_at_distance(two,0,1):')
print(my_tree.find_node_at_distance(two,0,3))
