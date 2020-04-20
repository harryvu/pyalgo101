class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Queue:      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def enqueue(self, item): 
        temp = Node(item) 
          
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

class BinaryNode:
    def __init__(self, name=None):
        self.name = name
        self.leftchild = None
        self.rightchild = None
        self.queue = Queue()
        self.seen = []
        self.levelorder = ""

    def traverse_preorder(self):
        """NLR"""
        
        result = self.name
        if (self.leftchild != None):
            result += " " + self.leftchild.traverse_preorder()
        
        if (self.rightchild != None):
            result += " " + self.rightchild.traverse_preorder()

        return result

    def traverse_levelorder(self, root):
        result = root.name
        self.queue.enqueue(root)

        while (self.queue.front != None):
            dnode = self.queue.dequeue()
            
            if (dnode.data.leftchild != None):
                result += " " + dnode.data.leftchild.name
                self.queue.enqueue(dnode.data.leftchild)

            if (dnode.data.rightchild != None):
                result += " " + dnode.data.rightchild.name
                self.queue.enqueue(dnode.data.rightchild)
        
        return result