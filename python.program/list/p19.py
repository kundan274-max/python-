a = []
b = []

n1 = int(input("Enter size of first list: "))

for i in range(n1):
    a.append(int(input("Enter element: ")))

n2 = int(input("Enter size of second list: "))

for i in range(n2):
    b.append(int(input("Enter element: ")))

i = 0
j = 0

result = []

while i < n1 and j < n2:

    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

while i < n1:
    result.append(a[i])
    i += 1

while j < n2:
    result.append(b[j])
    j += 1

print("Merged list:", result)
