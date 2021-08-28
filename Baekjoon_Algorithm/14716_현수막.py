import sys
from collections import deque
input = sys.stdin.readline
def bfs(x,y):
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny]:
                    arr[nx][ny] = 0
                    q.append((nx,ny))

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
for i in range(m):
    for j in range(n):
        if arr[i][j]:
            arr[i][j] = 0
            bfs(i, j)
            cnt += 1
print(cnt)