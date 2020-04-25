# Consider this min heap
#         5
#       /   \
#     7       6
#    / \     / \
#  10   15 17   12
#
# the above heap can be presented using the following array
# [5, 7, 6, 10, 15, 17, 12]

#         5
#       /   \
#     7       6
#    / \     / 
#  10   15 17   
#
# the above heap can be presented using the following array
# [5, 7, 6, 10, 15, 17]

# arr[5] = 17 => (5-1)/2 = 2 => arr[2] = 6 is the parent of 17
# how to check a node is leaf node?
# arr[4] = 15 => parent = (4-1)/2 = 1 => arr[1] = 7
# 15.left = 2 * 4 + 1 = 9 out of range => no left child
# 15.right = 2 * 4 + 2 = 10 out of range => no right child

# Mapping
#   parent -> (childIndex - 1) / 2
#   left child -> 2 * parentIndex + 1
#   right child -> 2 * parentIndex + 2
#
# Implement min heap with the following operations:
# For all operations make sure the following conditions are met:
# - your heap is a complete binary tree
# - max element is the root node for max heap
# - min element is the root node if min heap
# is_empty(): returns True if the heap is empty, False otherwise
# peek(): returns the minimum item in the heap without removing it, 
#   returns -1 if the heap is empty
# remove(): returns the minimum item in the heap after removing it, 
#   returns -1 if the heap is empty
# add(value): Inserting a new key at the end of the tree. O(1) to O(Log n) time.
#   If new key is larger than its parent, then we don’t need to do anything. 
#   Otherwise, we need to traverse up to fix the violated heap property.

class MinHeap:
    def __init__(self):
        self.tarr = []

    def is_empty(self):
        if len(self.tarr) == 0:
            return True
        return False

    def peek(self):
        if len(self.tarr) == 0:
            return -1

        return self.tarr[0]
        
    def add(self, value):
        if len(self.tarr) == 0:
            self.tarr += [value]
        elif len(self.tarr) == 1:
            if value > self.tarr[0]:
                self.tarr[1] = value
            else:
                # value will become root node, root node will become left node
                tmp = self.tarr[0]
                self.tarr[0] = value
                self.tarr += [tmp]

    def remove(self):
        pass

    # def _is_leaf(self, pos):
    #     parent_pos = (pos - 1) / 2
    #     left_pos = 2 * pos + 1
    #     right_pos = 2 * pos + 2

    #     if pos > 0:
            
            


mh = MinHeap()
mh.add(5)
print(mh.is_empty())
print(mh.peek())
mh.add(4)
print(mh.peek())