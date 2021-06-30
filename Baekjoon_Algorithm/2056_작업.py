n = int(input())
arr = [[]]
for i in range(n):
    job = list(map(int, input().split()))
    if len(job) == 2:
        time, count = job[0], job[1]
        arr.append([time, count, [0]])
    else:
        time, count, case = job[0], job[1], job[2:]
        arr.append([time, count, case])
dp = [0] * (n+1)
for i in range(1,n+1):
    time, count, case = arr[i]
    if count == 0:
        dp[i] = 0
    else:
        m = 0
        for j in case:
            m = max(m, arr[j][0] + dp[j])
        dp[i] = m
for i in range(1,n+1):
    dp[i] += arr[i][0]
print(max(dp))