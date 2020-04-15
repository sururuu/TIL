def dfs(x):
    if x == m:
        print(*res)
        return
    for i in range(n):
        if visited[i]:
            continue
        if len(res)>0:
            if res[-1] < n_list[i]:
                res.append(n_list[i])
                visited[i] = True
            else:
                continue
        elif len(res)==0:
            res.append(n_list[i])
            visited[i]=True

        dfs(x+1)

        res.pop()
        visited[i]=False


n,m=map(int,input().split())
n_list = [ _ for _ in range(1,n+1)]
visited = [False]*n
res=[]
dfs(0)