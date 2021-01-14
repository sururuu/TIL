from _collections import deque
def bfs(i,j):
    q = deque()
    q.append((i,j))
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 1<=X<(n+1) and 1<=Y<(m+1) and Map[X][Y] == 1:
                if (X,Y) not in visit:
                    cnt += 1
                    q.append((X,Y))
                    visit.add((X,Y))
    res.append(cnt)

n,m,k = map(int,input().split())
Map = [[0]*(m+1) for i in range(n+1)]
for i in range(k):
    x,y = map(int,input().split())
    Map[x][y] = 1

res = []
visit = set()
for i in range(1,n+1):
    for j in range(1,m+1):
        if Map[i][j] == 1:
            if (i,j) not in visit:
                visit.add((i,j))
                bfs(i,j)
print(max(res))