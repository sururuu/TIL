t = int(input())
for tc in range(t):
    n = int(input())
    if n % 2 == 1:
        print(0)
    else:
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(2,n+1,2):
            for j in range(2,i+1,2):
                dp[i] += (dp[j-2] * dp[i-j]) % 1000000007
        print(dp[n] % 1000000007)
# 카탈란 수