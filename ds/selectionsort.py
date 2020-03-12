def find_smallest(arr):
    # stores the smallest value
    smallest = arr[0]

    # stores the index of the smallest value
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
        
        return smallest_index

def selection_sort(arr):
    """Sort the array using selection sort algorithm, O(n*n)"""
    new_arr = []

    for i in range(len(arr)):
        # find the smallest element
        # then add it to new_arr
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr
