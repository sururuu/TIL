n = int(input())
fodo = [int(input()) for _ in range(n)]
dp = [0]*n
if n > 0:
    dp[0] = fodo[0]
if n > 1:
    dp[1] = sum(fodo[:2])
if n > 2:
    arr = fodo[:3]
    arr.sort()
    dp[2] = sum(arr[1:])
if n > 3:
    for i in range(3,n):
        m = max(fodo[i]+fodo[i-1]+dp[i-3],fodo[i]+dp[i-2],dp[i-1])
        dp[i] = m
print(dp[-1])