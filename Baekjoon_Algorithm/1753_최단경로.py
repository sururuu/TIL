import sys, heapq
v, e = [int(x) for x in sys.stdin.readline().split()]
k = int(input())
graph = [[] for _ in range(v+1)]
for i in range(e):
    start,end,value = [int(x) for x in sys.stdin.readline().split()]
    graph[start].append([end,value])
INF = float('inf')

def dijkstra(v,k):
    distance = [INF] * (v + 1)
    heap = []
    heapq.heappush(heap, (0, k))
    distance[k] = 0

    while heap:
        cost,idx = heapq.heappop(heap)
        if cost > distance[idx]:
            continue
        for end,value in graph[idx]:
            value += distance[idx]
            if value  < distance[end]:
                distance[end] = value
                heapq.heappush(heap,(distance[end],end))

    for i in range(1,v+1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print("INF")

dijkstra(v,k)