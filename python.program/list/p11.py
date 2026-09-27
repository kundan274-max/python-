l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

duplicates = []

for i in range(len(l)):

    count = 0

    for j in range(len(l)):

        if l[i] == l[j]:
            count += 1

    if count > 1 and l[i] not in duplicates:
        duplicates.append(l[i])

print("Duplicate elements:", duplicates)
