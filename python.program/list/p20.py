l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

longest = 0

for x in l:

    if x - 1 not in l:

        current = x
        count = 1

        while current + 1 in l:
            current += 1
            count += 1

        if count > longest:
            longest = count

print("Longest consecutive length =", longest)
