l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

result = [1] * n

left = 1

for i in range(n):
    result[i] = left
    left *= l[i]

right = 1

for i in range(n - 1, -1, -1):
    result[i] *= right
    right *= l[i]

print(result)
