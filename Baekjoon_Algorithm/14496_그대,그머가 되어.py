import heapq
INF = float('inf')
def dijkstra(a,b):
    distance = [INF] * (n+1)
    distance[a] = 0
    q = []
    heapq.heappush(q,[0,a])
    while q:
        dis,idx = heapq.heappop(q)
        if idx == b:
            return distance[b]
        for k in graph[idx]:
            if dis + 1 < distance[k]:
                distance[k] = dis + 1
                heapq.heappush(q,[distance[k],k])
    return -1

a,b = map(int,input().split())
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
print(dijkstra(a,b))