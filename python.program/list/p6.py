l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

pos = 0

for i in range(len(l)):

    if l[i] != 0:
        l[pos], l[i] = l[i], l[pos]
        pos += 1

print("Result:", l)
