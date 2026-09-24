l = [2, 3, -2, 4]

maximum = l[0]
minimum = l[0]
answer = l[0]

for i in range(1, len(l)):

    x = l[i]

    if x < 0:
        maximum, minimum = minimum, maximum

    maximum = max(x, maximum * x)
    minimum = min(x, minimum * x)

    answer = max(answer, maximum)

print(answer)
