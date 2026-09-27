l = [2, 3, 1, 1, 4]

jumps = 0
current_end = 0
farthest = 0

for i in range(len(l) - 1):

    farthest = max(farthest, i + l[i])

    if i == current_end:
        jumps += 1
        current_end = farthest

print(jumps)
