l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    l.append(x)

largest = float('-inf')
second = float('-inf')

for x in l:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

if second == float('-inf'):
    print("Second largest does not exist")
else:
    print("Second largest =", second)
