l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

candidate = None
count = 0

for x in l:

    if count == 0:
        candidate = x

    if x == candidate:
        count += 1
    else:
        count -= 1

# Verify
count = 0

for x in l:
    if x == candidate:
        count += 1

if count > n // 2:
    print("Majority element =", candidate)
else:
    print("No majority element")
