import sys
input = sys.stdin.readline
t = int(input())
n = 1000001
dp = [1]*n
for i in range(2, n):
    j = 1
    while i*j < n:
        dp[i*j] += i
        j += 1
    dp[i] += dp[i-1]

for i in range(t):
    num = int(input())
    print(dp[num])