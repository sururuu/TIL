n = int(input())
dp = [[0]*(n+1) for _ in range(n+1)]
res = -1000
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[j-1]
for k in range(n):
    for i in range(1, n-k+1):
        for j in range(1, n-k+1):
            square = dp[i+k][j+k] - dp[i-1][j+k] - dp[i+k][j-1] + dp[i-1][j-1]
            res = max(res, square)
print(res)