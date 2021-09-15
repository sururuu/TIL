m = 100001
dp = [[0, 0, 0] for _ in range(m)]
dp[:4] = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]
r = 1000000009
for i in range(4, m):
    dp[i][0] = (dp[i-1][1] % r) + (dp[i-1][2] % r)
    dp[i][1] = (dp[i-2][0] % r) + (dp[i-2][2] % r)
    dp[i][2] = (dp[i-3][0] % r) + (dp[i-3][1] % r)
t = int(input())
for tc in range(t):
    n = int(input())
    print(sum(dp[n]) % r)