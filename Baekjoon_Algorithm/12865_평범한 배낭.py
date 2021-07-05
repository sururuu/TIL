n, k = map(int,input().split())
arr = [0] + [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= arr[i][0]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-arr[i][0]]+arr[i][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
