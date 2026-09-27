l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

max_count = 0
answer = None

for i in range(len(l)):

    count = 0

    for j in range(len(l)):
        if l[i] == l[j]:
            count += 1

    if count > max_count:
        max_count = count
        answer = l[i]

print("Most frequent element =", answer)
print("Frequency =", max_count)
