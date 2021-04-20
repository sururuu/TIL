def dfs(idx):
    visit[idx] = True
    next_idx = arr[idx]
    if not visit[next_idx]:
        dfs(next_idx)

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visit = [False] * (n+1)
    res = 0
    for i in range(1,n+1):
        if not visit[i]:
            dfs(i)
            res += 1
    print(res)