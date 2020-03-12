def binary_search(list, item):
    low = 0
    high = len(list) -1

    # while you haven't narrowed it down to one element...
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        # found the item
        if guess == item:
            return mid

        # the guess was too high
        if guess > item:
            high = mid - 1
        
        # the guess was too low
        else:
            low = mid + 1

    # item doesn't exist
    return None
