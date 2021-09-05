t = int(input())
dp = [0] * 10001
dp[:5] = [1, 1, 2, 3, 4]
for i in range(5, 10001):
    dp[i] = dp[i-1] + dp[i-2] - dp[i-3]
    if i % 3 == 0:
        dp[i] += 1
for _ in range(t):
    n = int(input())
    print(dp[n])