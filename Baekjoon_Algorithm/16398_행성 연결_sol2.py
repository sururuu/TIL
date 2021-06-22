# 최소 신장 트리
import heapq
def prim(idx,v):
    visit = [False] * (v+1)
    visit[idx] = True
    h = []
    cnt = 1
    res = 0
    for target in graph[idx]:
        heapq.heappush(h,target)
    while h:
        cost, a = heapq.heappop(h)
        if not visit[a]:
            visit[a] = True
            res += cost
            cnt += 1
            for target in graph[a]:
                heapq.heappush(h,target)
        if cnt == v:
            return res
    return 0

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(i+1,n):
        x, y, cost = i, j, arr[i][j]
        graph[x].append((cost,y))
        graph[y].append((cost,x))
print(prim(1,n))