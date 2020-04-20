def trap(heights):

    left = [0]
    right = 0
    total = 0

    for i in range(len(heights)):
        if i > 0:
            left.append(max(left[i-1],heights[i-1]))

    j = len(heights) - 2
    for j in range(j, 0, -1):
        right = max(right,heights[j+1])
        sum = min(right,left[j]) - heights[j]
        if sum >= 0:
            total += sum
    
    return total


map = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(map))