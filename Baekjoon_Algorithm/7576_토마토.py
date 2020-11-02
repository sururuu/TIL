from collections import deque

def go():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while index:
        x,y = index.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<= X < n and 0<= Y < m and tomato[X][Y] == 0:
                tomato[X][Y]  = tomato[x][y] + 1
                index.append([X,Y])




m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n) ]

index = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1 :
            index.append((i,j))

go()
res = -1
flag = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0 :
            flag = -1
            break
        res = max(res,tomato[i][j])
if flag == -1 :
    res = -1
elif flag == 0 :
    res -= 1
print(res)