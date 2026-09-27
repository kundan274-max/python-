l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

k = int(input("Enter K: "))

k = k % n

result = l[k:] + l[:k]

print("After left rotation:")
print(result)

