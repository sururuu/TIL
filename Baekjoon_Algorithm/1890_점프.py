n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        x, y = i, j
        distance = arr[x][y]
        if x == n-1 and y == n-1:
            print(dp[-1][-1])
            break
        if x + distance < n:
            dp[x+distance][y] += dp[x][y]
        if y + distance < n:
            dp[x][y+distance] += dp[x][y]
