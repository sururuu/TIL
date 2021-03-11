from collections import deque
def bfs(i,j):
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    q = deque()
    q.append((i,j,0))
    visit = [[False]*m for _ in range(n)]
    while q:
        x,y,cnt = q.popleft()
        visit[x][y] = True
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < n and 0<= ny < m:
                if Map[nx][ny] == 1:
                    return cnt + 1
                if visit[nx][ny] == False and Map[nx][ny] == 0:
                    q.append((nx,ny,cnt+1))
                    visit[nx][ny] = True


n,m = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if Map[i][j] == 0:
            res = max(res,bfs(i,j))
print(res)
