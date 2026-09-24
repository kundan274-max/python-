l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

jumps = 0
current_end = 0
farthest = 0

for i in range(n - 1):

    farthest = max(farthest, i + l[i])

    if i == current_end:

        jumps += 1
        current_end = farthest

print("Minimum jumps =", jumps)
