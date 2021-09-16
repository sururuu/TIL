def dfs(k, idx):
    if k == m:
        print(*res)
        return
    for i in range(idx, n):
        if visit[i]:
            continue
        visit[i] = True
        res.append(arr[i])
        dfs(k+1, i+1)
        visit[i] = False
        res.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [False] * n
res = []
dfs(0, 0)