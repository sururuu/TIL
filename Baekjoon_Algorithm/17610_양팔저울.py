def dfs(idx,total):
    global s, res
    if total > s:
        return
    if idx == k:
        if 0 < total <= s:
            res.add(total)
    else:
        dfs(idx+1, total+g[idx])
        dfs(idx+1, total-g[idx])
        dfs(idx+1, total)
k = int(input())
g = list(map(int,input().split()))
s = sum(g)
res = set()
dfs(0, 0)
print(s-len(res))