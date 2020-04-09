class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self, node):
        self.root = node
    
    def insert(self, node):
        self._insert(self.root, node)

    def _insert(self, atNode, newNode):
        if atNode is None:
            atNode = newNode
        else:
            if atNode.value < newNode.value:
                if atNode.right is None:
                    atNode.right = newNode
                else:
                    self._insert(atNode.right, newNode)
            else:
                if atNode.left is None:
                    atNode.left = newNode
                else:
                    self._insert(atNode.left, newNode)
    
    # DFS traversals

    def inorder(self):
        """LNR-retrieves the keys in accending sorted order"""
        self._inorder(self.root)

    def reverseinorder(self):
        """RNL-retrieves the keys in decending sorted order"""
        pass

    def preorder(self):
        """NLR"""
        pass

    def postorder(self):
        """LRN"""
        pass

    # BFS Traversal / Level Order

    def levelorder(self):
        pass

    def _inorder(self, atNode):
        if atNode:
            self._inorder(atNode.left)
            print(atNode.value)
            self._inorder(atNode.right)
            

# A utility function to search a given key in BST
def search(root, key):
    # base cases: root is null or key is present at root
    if root is None or root.value == key:
        return root

    # key is greater that root's key
    if root.value < key:
        return search(root.right, key)

    # key is smaller than root's key
    else:
        return search(root.left, key)