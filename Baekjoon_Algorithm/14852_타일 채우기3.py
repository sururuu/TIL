n = int(input())
dp = [0]*(n+1)
s = [0]*(n+1)
dp[:3] = [1, 2, 7]
s[:3] = [1, 3, 10]
for i in range(3, n+1):
    dp[i] = (s[i-1]*2 + dp[i-2]) % 1000000007
    s[i] = (s[i-1] + dp[i]) % 1000000007
print(dp[n])
# dp[4] = dp[3]*dp[1] + dp[2]*2 + dp[1]*2 + 2, dp[0] = 1
# dp[n] = 2(dp[0] + ``` + dp[n-1) + dp[n-2]