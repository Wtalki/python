matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])
print(matrix[1][2])
print(matrix[2][1])

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"element a [{i}][{j}] is {matrix[i][j]}")

# common 2d list operations 

rows,cols = 3,3
zero_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

print(zero_matrix)

#finding the dimensions of a 2d list
rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0

print("rows:", rows)
print("cols:", cols)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element
    
print("sum of all elements:", total_sum)

second_row = matrix[1]
print(second_row)

first_column = [row[0] for row in matrix]
print(first_column)



# 5 Transposing a 2d list (switchin rows and columns)


transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)

#example a tic-tac-toe board 

tic_tac_toe_board = [
    ["X","O","X"],
    ["0","X","O"],
    ["","X",""]
]
cell=" "
for row in tic_tac_toe_board:
    print(" | ".join([cell if cell != "" else " " for cell in row]))
    print("-" * 9)

