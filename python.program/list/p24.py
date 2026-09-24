l = []

n = int(input("Enter n: "))

for i in range(n + 1):
    l.append(int(input("Enter element: ")))

for i in range(n + 1):

    for j in range(i + 1, n + 1):

        if l[i] == l[j]:
            print("Duplicate =", l[i])
            break
