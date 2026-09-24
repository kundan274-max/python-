l = [1, 4, 20, 3, 10, 5]
target = 33

start = 0
current_sum = 0

for end in range(len(l)):

    current_sum += l[end]

    while current_sum > target and start <= end:
        current_sum -= l[start]
        start += 1

    if current_sum == target:
        print("Subarray:", l[start:end + 1])
        print("Start:", start)
        print("End:", end)
        break
