l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

current = l[0]
maximum = l[0]

for i in range(1, n):

    if current + l[i] > l[i]:
        current = current + l[i]
    else:
        current = l[i]

    if current > maximum:
        maximum = current

print("Maximum subarray sum =", maximum)
