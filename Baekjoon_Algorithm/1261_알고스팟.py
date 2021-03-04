from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs():
    q = deque()
    q.append((0,0))
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1:
                    if miro[nx][ny] == 0:
                        dist[nx][ny] = dist[x][y]
                        if nx == n-1 and ny == m-1:
                            return dist[n-1][m-1]
                        q.appendleft((nx,ny))
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx,ny))
    return dist[n-1][m-1]

m,n = map(int,input().split())
miro = [list(map(int,input())) for _ in range(n)]
cnt = 0
print(dfs())