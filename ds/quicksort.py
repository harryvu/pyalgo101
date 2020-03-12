def quick_sort(arr):
    if len(arr) < 2:
        # base case: arrays with 0 or 1 element don't need to sort at all
        return arr
    else:
        # recursive case
        
        # select the pivot
        pivot = array[0]

        # sub-array of all the elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]

        # sub-array of all the elements greater than the pivot
        greater = [i for i in arr[1:] if i >  pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)



