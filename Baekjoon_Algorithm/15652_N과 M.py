def dfs(x):
    if x == m:
        print(*res)
        return
    for i in range(n):
        if visited[i]:
            continue
        res.append(n_list[i])
        dfs(x+1)
        visited[i]=True
        res.pop()

        for j in range(i+1,n):
            visited[j] = False

n,m=map(int,input().split())
n_list = [ _ for _ in range(1,n+1)]
visited = [False]*n
res = []
dfs(0)