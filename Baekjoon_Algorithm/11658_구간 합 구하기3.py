import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + arr[i-1][j-1]
for i in range(m):
    case = list(map(int,input().split()))
    if case[0] == 0:
        w, x, y, c = case
        arr[x-1][y-1] = c
        for k in range(1,n+1):
            dp[x][k] = dp[x][k-1] + arr[x-1][k-1]
    elif case[0] == 1:
        w, x1, y1, x2, y2 = case
        s = 0
        for k in range(x1,x2+1):
            s += dp[k][y2]
            s -= dp[k][y1-1]
        print(s)