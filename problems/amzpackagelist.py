"""
Write an algorithm to merge these two lists together

l1 = [2,5,8,11,14]
l2 = [1,3,5,7]
result = [1,2,3,5,5,7,8,11,14]
"""

# Merges two sub-arrays of arr[]
# First sub-array is arr[1..m]
# Second sub-array is arr[m+1..r]

def merge(left, right):
    result = []
    idxLeft = 0
    idxRight = 0

    while (idxLeft < len(left) and idxRight < len(right)):
        if left[idxLeft] < right[idxRight]:
            result.append(left[idxLeft])
            idxLeft += 1
        else:
            result.append(right[idxRight])
            idxRight += 1

    return left + right

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    # get the middle item of the arr
    middle = len(arr) // 2
    left = arr[:middle+1]
    right = arr[middle+1:]

    return merge(left,right)

l1 = [2,5,8,11,14]
l2 = [1,3,5,7]

l12 = merge(l1,l2)
print(l12)
print(sorted(l12))

# l3 = [2,5,1,3,7,4,2,3,9,8,6,3]
# print(merge_sort(l3))

# l3_l = l3[:5]
# l3_r = l3[5:]
# print(l3_l)
# print(l3_r)