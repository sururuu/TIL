n = int(input())
time = []
price = []
for i in range(n):
    t, p = map(int,input().split())
    time.append(t)
    price.append(p)
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if i + time[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+time[i]]+price[i])
print(dp[0])