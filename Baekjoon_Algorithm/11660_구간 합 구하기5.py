import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    arr = list(map(int,input().split()))
    for k in range(n):
        dp[i+1][k+1] = (dp[i+1][k]+arr[k])
for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    s = 0
    for k in range(x1,x2+1):
        s += dp[k][y2]
        s -= dp[k][y1-1]
    print(s)