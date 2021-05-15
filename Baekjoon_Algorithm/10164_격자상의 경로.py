n,m,k = map(int,input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 1
if k > 0:
    x = (k-1) // m + 1
    y = (k-1) % m + 1
    for i in range(1,x+1):
        for j in range(1,y+1):
            if i == 1 and j == 1:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    res = dp[x][y]
    dp[x][y] = 1
    for i in range(x,n+1):
        for j in range(y,m+1):
            if i == x and j == y:
                continue
            else:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
    res *= dp[-1][-1]
    print(res)
else:
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1])