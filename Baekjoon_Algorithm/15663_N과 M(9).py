def dfs(i):
    if i == M:
        temp = ' '.join(map(str,ans))
        if temp not in res:
            res.append(temp)
        return
    for k in range(N):
        if not visit[k]:
            ans.append(arr[k])
            visit[k] = True
            last = arr[k]
            dfs(i+1)
            ans.pop()
            visit[k] = False


N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visit = [False]*N
res = []
ans = []
dfs(0)
for target in res:
    print(target)
