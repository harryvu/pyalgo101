# Given a string s and an integer value rows
# return the "zigzag" encoding of s read off row-by-row.
# Example 1:
# s = "YELLOWPINK"
# rows = 4
# Output: "YPEWILONLK"
# Explanation:
# Y     P    (row 1: "YP")
# E   W I    (row 2: "EWI")
# L O   N    (row 3: "LON")
# L     K    (row 4: "LK")

def zigzag(s, rows):
    arr = [""] * rows

    isDown = False
    row = 0    
    for char in s:
        arr[row] += char
        if (row == 0) or (row == rows - 1):
            isDown = not isDown
        if isDown:
            row += 1
        else:
            row -= 1
    
    print(arr)
        

zigzag("YELLOWPINK", 4)