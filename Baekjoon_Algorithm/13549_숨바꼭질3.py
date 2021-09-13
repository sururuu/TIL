from collections import deque
n, k = map(int, input().split())
visit = [-1] * 100001
visit[n] = 0
def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visit[x])
            return
        if 0 <= x*2 < 100001 and visit[x*2] == -1:
            visit[x*2] = visit[x]
            q.append(x*2)
        if 0 <= x-1 < 100001 and visit[x-1] == -1:
            visit[x-1] = visit[x] + 1
            q.append(x-1)
        if 0 <= x+1 < 100001 and visit[x+1] == -1:
            visit[x+1] = visit[x] + 1
            q.append(x+1)

bfs(n)