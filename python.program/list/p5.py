l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

result = []

for x in l:
    if x not in result:
        result.append(x)

print("After removing duplicates:")
print(result)
