def dfs(x):
    if x == m :
        print(*res)
        return
    for i in range(n):
        if visited[i]:
            pass
        visited[i]=True

        res.append(n_list[i])
        visited[i]=False

        dfs(x+1)
        res.pop()
        visited[i]=False




n,m=map(int,input().split())
n_list = [ _ for _ in range(1,n+1)]
visited = [False]*n
res=[]
dfs(0)