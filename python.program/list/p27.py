l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter positive element: ")))

target = int(input("Enter target sum: "))

start = 0
current_sum = 0

found = False

for end in range(n):

    current_sum += l[end]

    while current_sum > target and start <= end:
        current_sum -= l[start]
        start += 1

    if current_sum == target:

        print("Subarray =", l[start:end + 1])
        print("Start index =", start)
        print("End index =", end)

        found = True
        break

if not found:
    print("No subarray found")
