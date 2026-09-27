matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

# Transpose
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Reverse every row
for row in matrix:
    row.reverse()

for row in matrix:
    print(row)
