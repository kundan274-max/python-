l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

target = int(input("Enter target: "))

found = False

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):

            if l[i] + l[j] + l[k] == target:

                print(l[i], l[j], l[k])
                found = True

if not found:
    print("No triplet found")
