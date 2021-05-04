import heapq
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())

INF = float('inf')
def dijkstra(start):
    distance = [INF] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dis, idx = heapq.heappop(heap)
        if dis > distance[idx]:
            continue
        for index,value in graph[idx]:
            value += distance[idx]
            if value < distance[index]:
                distance[index] = value
                heapq.heappush(heap,(distance[index],index))
    return distance

# 특정 최단 경로
# 1. 1 -> v1 -> v2 -> n
# 2. 1 -> v2 -> v1 -> n
n1 = dijkstra(1)
n2 = dijkstra(v1)
n3 = dijkstra(v2)
case1 = n1[v1] + n2[v2] + n3[n]
case2 = n1[v2] + n3[v1] + n2[n]
res = min(case1,case2)
if res == INF:
    print('-1')
else:
    print(res)