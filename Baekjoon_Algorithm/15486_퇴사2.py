n = int(input())
time = []
price = []
for i in range(n):
    t, p = map(int,input().split())
    time.append(t)
    price.append(p)
dp = [0] * (n+1)
for i in range(n):
    if time[i] <= n-i:
        dp[i+time[i]] = max(dp[i]+price[i], dp[i+time[i]])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[-1])