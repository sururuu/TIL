import heapq
n,m = map(int,input().split())
inDegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
# 진입 차수 더하기
for i in range(m):
    a,b = map(int,input().split())
    inDegree[b] += 1
    graph[a].append(b)
# 진입 루트가 없는 정점 큐에 넣기
q = []
for i in range(1,n+1):
    if inDegree[i] == 0:
        heapq.heappush(q,i)

while q:
    num = heapq.heappop(q)
    for k in graph[num]:
        inDegree[k] -= 1
        if inDegree[k] == 0:
            heapq.heappush(q,k)
    print(num,end=' ')
