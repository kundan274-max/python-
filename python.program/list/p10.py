l = []

n = int(input("Enter n: "))

for i in range(n - 1):
    l.append(int(input("Enter element: ")))

print("Missing numbers:")

for i in range(1, n + 1):

    if i not in l:
        print(i)
