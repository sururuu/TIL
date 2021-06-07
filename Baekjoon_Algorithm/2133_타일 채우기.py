n = int(input())
dp = [0]*31
dp[2] = 3
for i in range(4,n+1,2):
    dp[i] = dp[i-2]*3
    for j in range(i-4,1,-2):
        dp[i] += dp[j]*2
    dp[i] += 2
print(dp[n])
# dp[n] = dp[n-2] * 3 + (dp[n-4] + ```` dp[2]) * 2 + 2