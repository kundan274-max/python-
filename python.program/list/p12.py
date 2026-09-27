l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

target = int(input("Enter target sum: "))

found = False

for i in range(len(l)):

    for j in range(i + 1, len(l)):

        if l[i] + l[j] == target:
            print(l[i], "+", l[j], "=", target)
            found = True

if not found:
    print("No pair found")
