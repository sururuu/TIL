t = int(input())
dp = [0]*(1000001)
dp[:3] = [1, 1, 2]
r = 1000000009
for i in range(3, 1000001):
    dp[i] = (dp[i-1] % r + dp[i-2] % r + dp[i-3] % r) % r
for _ in range(t):
    num = int(input())
    print(dp[num])