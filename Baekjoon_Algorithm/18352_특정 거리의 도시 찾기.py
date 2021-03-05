from collections import deque
import sys
n,m,k,x = map(int,input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int,sys.stdin.readline().split())
    arr[s].append(e)
INF = float('inf')
distance = [INF] *(n+1)
distance[x] = 0
q = deque()
q.append(x)
while q:
    target = q.popleft()
    for i in arr[target]:
        # 방문하지 않은 노드 체크
        if distance[i] == INF:
            distance[i] = distance[target] + 1
            q.append(i)
for i in range(n+1):
    if distance[i] == k:
        print(i)
if k not in distance:
    print(-1)