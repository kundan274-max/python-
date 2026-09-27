l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

leaders = []

max_right = l[-1]

leaders.append(max_right)

for i in range(n - 2, -1, -1):

    if l[i] > max_right:
        leaders.append(l[i])
        max_right = l[i]

leaders.reverse()

print("Leaders:", leaders)
