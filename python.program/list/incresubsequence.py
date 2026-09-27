l = [10, 9, 2, 5, 3, 7, 101, 18]

dp = [1] * len(l)

for i in range(len(l)):

    for j in range(i):

        if l[j] < l[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
