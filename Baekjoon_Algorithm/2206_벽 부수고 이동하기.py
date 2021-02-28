from _collections import deque
dx = [0,-1,0,1]
dy = [-1,0,1,0]
def bfs():
    q = deque()
    q.append((0,0,1)) # x,y,wall
    visit[0][0][1] = 1 # x,y,distance
    while q:
        x,y,w = q.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][w]
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<=X<n and 0<=Y<m:
                # 벽일때 뚫을 수 있는 경우
                if Map[X][Y] == 1 and w == 1:
                    visit[X][Y][0] = visit[x][y][1] + 1
                    q.append((X,Y,0))
                # 벽이 아니고 방문하지 않은 곳을 가는 경우
                elif Map[X][Y] == 0 and visit[X][Y][w] == 0:
                    visit[X][Y][w] = visit[x][y][w] + 1
                    q.append((X,Y,w))
    return -1


n,m = map(int,input().split( ))
Map = [list(map(int,input())) for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
print(bfs())
