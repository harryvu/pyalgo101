def RepeatingNumbers(arr, n):    
    # Store elements and  
    # their counts in 
    # hash table 
    mp = [0] * 100
    for i in range(0, n): 
        mp[arr[i]] += 1
  
    # Since we want elements  
    # in same order, we  
    # traverse array again  
    # and print those elements  
    # that appear more than once. 
    for i in range(0, n): 
        if (mp[arr[i]] > 1): 
            print(arr[i], end = " ") 
              
            # This is tricky, this  
            # is done to make sure  
            # that the current element  
            # is not printed again 
            mp[arr[i]] = 0
      
# Driver code 
arr = [12, 10, 9, 45,  
       2, 10, 10, 45]  
n = len(arr) 
print(RepeatingNumbers(arr, n))