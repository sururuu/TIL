from collections import deque
def bfs(idx):
    visit = [False]*(n+1)
    visit[idx] = True
    q = deque()
    q.append(idx)
    cnt = 1
    while q:
        index = q.popleft()
        cnt += 1
        for target in graph[index]:
            if visit[target] == False:
                q.append(target)
                visit[target] = True
    return cnt

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    # graph[s].append(e)
    graph[e].append(s)
res = [0]*(n+1)
for i in range(1,n+1):
    res[i] = bfs(i)

Max = max(res)
for i in range(1,n+1):
    if Max == res[i]:
        print(i,end=' ')