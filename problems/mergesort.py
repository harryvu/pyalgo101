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
    # base case
    if len(arr) == 1:
        return arr

    # get the middle item of the arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    return merge(merge_sort(left), merge_sort(right))

# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

        return arr

l1 = [2,5,8]
l2 = [1,3,]

l12 = merge(l1,l2)
# print(l12)
# print(sorted(l12))
print(mergeSort(l12))

# l3 = [2,5,1,3,7,4,2,3,9,8,6]
# print(merge_sort(l3))

# l3_l = l3[:5]
# l3_r = l3[5:]
# print(l3_l)
# print(l3_r)