from ds.binarytree import BinaryNode

one = BinaryNode("One")
two = BinaryNode("Two")
three = BinaryNode("Three")
four = BinaryNode("Four")
five = BinaryNode("Five")
six = BinaryNode("Six")
seven = BinaryNode("Seven")
eight = BinaryNode("Eight")

one.leftchild = two
one.rightchild = three
two.leftchild = four
two.rightchild = five
three.leftchild = six
three.rightchild = seven
four.leftchild = eight

#print(one.traverse_preorder())
print(one.traverse_levelorder(one))
print(one.levelorder)