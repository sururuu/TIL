from collections import deque
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
inDegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time = [0]
for i in range(n):
    new = arr[i][1:-1]
    time.append(arr[i][0])
    if new:
        for idx in new:
            inDegree[i+1] += 1
            graph[idx].append(i+1)

q = deque()
for i in range(1,n+1):
    if not inDegree[i]:
        q.append(i)
res = [0]*(n+1)

while q:
    node = q.popleft()
    res[node] = max(res[node],time[node])
    for target in graph[node]:
        inDegree[target] -= 1
        res[target] = max(res[target],res[node]+time[target])
        if inDegree[target] == 0:
            q.append(target)
for i in range(1,n+1):
    print(res[i])