n, m = map(int,input().split())
case = list(map(int,input().split()))
dp = [10000000]*(n+1)
check = [0]*20001
for i in range(m):
    check[case[i]] = 1
    for j in range(i+1,m):
        check[case[i]+case[j]] = 1
dp[0] = 0
for i in range(1, n+1):
    if check[i]:
        for j in range(i, n+1):
            dp[j] = min(dp[j], dp[j-i]+1)
if dp[-1] == 10000000:
    print(-1)
else:
    print(dp[-1])