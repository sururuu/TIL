from _collections import deque
n = int(input())
grid = [list(input()) for _ in range(n)]
res = []
def dfs(x,y,z):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<=X<n and 0<=Y<n and visit[X][Y] == False:
                if grid[x][y] == grid[X][Y]:
                    visit[X][Y] = True
                    q.append((X,Y))
                if z == 1:
                    if grid[x][y] == 'R' and grid[X][Y] == 'G':
                        visit[X][Y] = True
                        q.append((X, Y))
                    if grid[x][y] == 'G' and grid[X][Y] == 'R':
                        visit[X][Y] = True
                        q.append((X, Y))

visit = [[False]*n for i in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            visit[i][j] = True
            dfs(i,j,0)
            cnt1 += 1
            
visit = [[False]*n for i in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            visit[i][j] = True
            dfs(i, j, 1)
            cnt2 += 1
print(cnt1,cnt2)