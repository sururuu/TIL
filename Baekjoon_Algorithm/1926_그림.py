from _collections import deque
def bfs(i,j):
    q = deque()
    q.append((i,j))
    paper[i][j] = 0
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    color = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<=X<n and 0<=Y<m:
                if paper[X][Y]:
                    color += 1
                    q.append((X,Y))
                    paper[X][Y] = 0
    return color

n,m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
res = 0
for i in range(n):
    for j in range(m):
        if paper[i][j]:
           cnt += 1
           color = bfs(i,j)
           if res < color:
               res = color
print(cnt,res,sep='\n')