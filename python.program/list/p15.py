l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

current = l[0]
maximum = l[0]

start = 0
best_start = 0
best_end = 0

for i in range(1, n):

    if l[i] > current + l[i]:
        current = l[i]
        start = i
    else:
        current += l[i]

    if current > maximum:
        maximum = current
        best_start = start
        best_end = i

print("Maximum sum =", maximum)
print("Subarray =", l[best_start:best_end + 1])
