n = int(input("Enter matrix size: "))

matrix = []

for i in range(n):

    row = []

    for j in range(n):
        row.append(int(input("Enter element: ")))

    matrix.append(row)

# Transpose
for i in range(n):

    for j in range(i + 1, n):

        matrix[i][j], matrix[j][i] = \
        matrix[j][i], matrix[i][j]

# Reverse rows
for i in range(n):
    matrix[i].reverse()

print("Rotated matrix:")

for row in matrix:
    print(row)
