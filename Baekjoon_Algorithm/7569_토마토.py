from collections import deque
dx = [0,0,1,-1,0,0]
dy = [-1,1,0,0,0,0]
dz = [0,0,0,0,-1,1]
def dfs():
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = 1
                    count[nz][nx][ny] = count[z][x][y] + 1
                    q.append((nz,nx,ny))

m,n,h = map(int,input().split())
tomato = [[] for _ in range(h)]
count = [[[0]*m for _ in range(n)] for _ in range(h)]
for i in range(h):
    arr = [list(map(int,input().split())) for _ in range(n)]
    tomato[i] = arr
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1 and count[i][j][k] == 0:
                q.append((i,j,k))
                count[i][j][k] = 1
dfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1,)
                exit()
res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            res = max(res,count[i][j][k])
if res > 0:
    print(res-1)
else:
    print(0)


