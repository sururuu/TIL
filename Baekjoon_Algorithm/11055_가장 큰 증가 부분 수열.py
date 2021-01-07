n = int(input())
arr = list(map(int,input().split()))
dp = [n for n in arr]
for i in range(n):
    for j in range(i):
        # 증가수열 판별
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+arr[i])
print(max(dp))