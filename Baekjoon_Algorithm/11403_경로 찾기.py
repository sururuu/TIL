from collections import deque
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dic = {}
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            if i in dic:
                dic[i].append(j)
            else:
                dic[i] = [j]
for key, value in dic.items():
    q = deque(value)
    while q:
        j = q.popleft()
        dp[key][j] = 1
        if j in dic:
            for k in dic[j]:
                if not dp[key][k]:
                    q.append(k)
for i in range(n):
    for j in range(n):
        print(dp[i][j], end=' ')
    print()