import sys
input = sys.stdin.readline
m, n = map(int, input().split())
K = int(input())
dp = [[[0, 0, 0] for _ in range(n+1)] for _ in range(m+1)]
dp_o = [[0]*(n+1) for _ in range(m+1)]
dp_i = [[0]*(n+1) for _ in range(m+1)]
for i in range(m):
    arr = list(input())
    for j in range(n):
        for k in range(3):
            dp[i+1][j+1][k] = dp[i+1][j][k] + dp[i][j+1][k] - dp[i][j][k]
        if arr[j] == 'J':
            dp[i+1][j+1][0] += 1
        elif arr[j] == 'O':
            dp[i+1][j+1][1] += 1
        elif arr[j] == 'I':
            dp[i+1][j+1][2] += 1
for _ in range(K):
    a, b, c, d = map(int,input().split())
    cnt_j, cnt_o, cnt_i = 0, 0, 0
    for i in range(3):
        print(dp[c][d][i]-(dp[a-1][d][i]+dp[c][b-1][i]-dp[a-1][b-1][i]), end=' ')
    print()

