from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<= X < n and 0<= Y < m:
                if cabbage[X][Y] == 1:
                    q.append((X,Y))
                    cabbage[X][Y] = 0
    return



T = int(input())
for t in range(T):
    m,n,k = map(int,input().split())
    cabbage = [[0]*m for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        cabbage[y][x] = 1
    cnt = 0

    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                cabbage[i][j] = 0
                bfs(i,j)
                cnt += 1
    print(cnt)
