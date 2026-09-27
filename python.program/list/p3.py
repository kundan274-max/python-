l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

visited = []

for i in range(len(l)):

    if l[i] in visited:
        continue

    count = 0

    for j in range(len(l)):
        if l[i] == l[j]:
            count += 1

    print(l[i], "appears", count, "times")

    visited.append(l[i])
