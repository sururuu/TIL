import sys, heapq
def dijkstra(start_index):
    distance = [float('inf')] * (n+1)
    h = []
    heapq.heappush(h,[0,start_index])
    distance[start_index] = 0
    while h:
        cost,node = heapq.heappop(h)
        for next_cost, next_node in graph[node]:
            next_cost += cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(h,[next_cost,next_node])
    return distance

n,m,x= map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e,distance = map(int,sys.stdin.readline().split())
    graph[s].append((distance,e))
answer = [0] * (n+1)
for person in range(1,n+1):
    # 내 위치에서 x 까지 가는데 시간
    arr = dijkstra(person)
    answer[person] += arr[x]
    # x 에서 돌아오는 시간
    arr2 = dijkstra(x)
    answer[person] += arr2[person]
print(max(answer))