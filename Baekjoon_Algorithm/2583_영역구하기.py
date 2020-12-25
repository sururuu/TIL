from _collections import deque
m,n,k = map(int,input().split())
paper = [[0]*n for _ in range(m)]
# 영역에 색칠하기
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = (m-y1),x1,(m-y2),x2
    for x in range(x2,x1):
        for y in range(y1,y2):
            if paper[x][y] == 0:
                paper[x][y] = 1
# 분리된 영역 갯수와 넓이 구하기
def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    count = 0
    while q:
        count += 1
        x,y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<=X<m and 0<=Y<n:
                if paper[X][Y] == 0:
                    paper[X][Y] = 1
                    q.append((X,Y))
    area.append(count)

cnt = 0
area = []
for i in range(m):
    for j in range(n):
        if paper[i][j] == 0:
            paper[i][j] = 1
            cnt += 1
            bfs(i,j)

print(cnt)
area.sort()
print(' '.join(map(str,area)))