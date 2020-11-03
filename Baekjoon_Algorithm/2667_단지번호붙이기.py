n = int(input())
map = [list(map(int,input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
def dfs(x,y):
    map[x][y] = 0
    visited[x][y] = True
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    stack = []
    stack.append((x,y))
    size = 1
    while stack:
        x,y = stack.pop()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<= X <n and 0<= Y < n:
                if map[X][Y] != 0 and visited[X][Y] == False:
                    size+=1
                    map[X][Y] =0
                    visited[X][Y] = True
                    stack.append((X,Y))
    return size
cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if map[i][j] != 0:
            cnt += 1
            res.append(dfs(i,j))
print(cnt)
res.sort()
for i in range(len(res)):
    print(res[i])
