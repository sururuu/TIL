n = int(input())
# dp[n] = (n-1)*(dp[n-1]+dp[n-2)
dp = [0,1]
if n < 2:
    print(dp[n-1])
    exit()
for i in range(n):
    dp.append((i+2)*(dp[-2]+dp[-1])%1000000000)
print(dp[n-1])