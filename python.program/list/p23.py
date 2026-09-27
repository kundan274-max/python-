l = []

n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

dp = [1] * n

for i in range(n):

    for j in range(i):

        if l[j] < l[i]:

            dp[i] = max(dp[i], dp[j] + 1)

print("Longest increasing subsequence length =", max(dp))
