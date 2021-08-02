import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
dp = [0]
for k in range(1, n+1):
    dp.append(dp[-1]+a[k-1])
for _ in range(m):
    i, j = map(int, input().split())
    s = dp[j] - dp[i-1]
    print(s)
