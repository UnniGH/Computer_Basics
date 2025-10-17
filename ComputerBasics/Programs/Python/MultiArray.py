# Example of a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing with nested loops
print("Printing a 2D list:")
for row in matrix:
    for element in row:
        print(element, end=" ") # Print elements of a row on the same line
    print() # Move to the next line after each row