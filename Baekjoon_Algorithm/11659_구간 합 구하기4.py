import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))
dp = [0]
for k in range(1,n+1):
    dp.append(dp[-1] + num[k-1])
for tc in range(m):
    i,j = map(int,input().split())
    s = dp[j] - dp[i-1]
    if i == 1:
        print(dp[j])
    else:
        print(s)