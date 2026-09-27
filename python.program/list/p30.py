l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

# Normal maximum subarray
current_max = l[0]
max_sum = l[0]

# Minimum subarray
current_min = l[0]
min_sum = l[0]

total = l[0]

for i in range(1, n):

    total += l[i]

    current_max = max(l[i], current_max + l[i])
    max_sum = max(max_sum, current_max)

    current_min = min(l[i], current_min + l[i])
    min_sum = min(min_sum, current_min)

# All elements negative
if max_sum < 0:
    answer = max_sum
else:
    circular_sum = total - min_sum
    answer = max(max_sum, circular_sum)

print("Maximum circular subarray sum =", answer)
