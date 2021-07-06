n = int(input())
arr = list(map(int,input().split()))
dp = [[0 for _ in range(21)] for _ in range(n-1)]
dp[0][arr[0]] = 1
for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]:
            prev = j
            now = arr[i]
            if 0 <= prev + now <= 20:
                dp[i][prev+now] += dp[i-1][prev]
            if 0 <= prev - now <= 20:
                dp[i][prev-now] += dp[i-1][prev]
target = arr[-1]
print(dp[-1][target])
