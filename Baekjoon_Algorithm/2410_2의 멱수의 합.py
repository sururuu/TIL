n = int(input())
m = 1000001
div = 1000000000
dp = [0] * m
dp[0] = 1
idx = 1
while idx < m:
    for i in range(idx, n+1):
        dp[i] += dp[i-idx]
        dp[i] %= div
    idx *= 2

print(dp[n] % div)