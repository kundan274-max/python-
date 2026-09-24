l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

first = float('-inf')
second = float('-inf')
third = float('-inf')

for x in l:
    if x > first:
        third = second
        second = first
        first = x

    elif x > second and x != first:
        third = second
        second = x

    elif x > third and x != first and x != second:
        third = x

if third == float('-inf'):
    print("Third largest does not exist")
else:
    print("Third largest =", third)
