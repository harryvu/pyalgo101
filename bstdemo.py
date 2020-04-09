from ds.bst import BST, BSTNode

root = BSTNode(50)
bst = BST(root)
bst.insert(BSTNode(30))
bst.insert(BSTNode(20))
bst.insert(BSTNode(40))
bst.insert(BSTNode(70))
bst.insert(BSTNode(10))
bst.insert(BSTNode(60))
bst.insert(BSTNode(80))

bst.inorder()