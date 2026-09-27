l = [1, 3, 4, 2, 2]

for i in range(len(l)):

    for j in range(i + 1, len(l)):

        if l[i] == l[j]:
            print("Duplicate:", l[i])
            break
