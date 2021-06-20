import heapq
def prim(idx, v):
    visit = [False]*(v+1)
    visit[idx] = True
    cnt = 1
    res = 0
    h = []
    for target in graph[idx]:
        heapq.heappush(h, target)
    while h:
        cost, a = heapq.heappop(h)
        if not visit[a]:
            visit[a] = True
            cnt += 1
            res += cost
            for target in graph[a]:
                heapq.heappush(h, target)
        if cnt == v:
            return res
    return 0

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    a, b, cost = map(int,input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))
print(prim(1,V))