def dfs(i,ind):
    if i == M:
        print(*ans)
        return
    flag = 0
    for k in range(ind,N):
        if not visit[k] and flag != arr[k]:
            ans.append(arr[k])
            visit[k] = True
            flag = arr[k]
            dfs(i+1,k)
            ans.pop()
            visit[k] = False
            for j in range(k+1,N):
                visit[j] = False
N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visit = [False] * N
ans = []
dfs(0,0)