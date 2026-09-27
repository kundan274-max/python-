l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

maximum = l[0]
minimum = l[0]
answer = l[0]

for i in range(1, n):

    x = l[i]

    if x < 0:
        maximum, minimum = minimum, maximum

    maximum = max(x, maximum * x)
    minimum = min(x, minimum * x)

    answer = max(answer, maximum)

print("Maximum product =", answer)
