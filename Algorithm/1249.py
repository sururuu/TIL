from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def deque_():
    que = deque()
    que.append([0, 0])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] > Map[nx][ny] + dist[x][y]:
                    dist[nx][ny] = Map[nx][ny] + dist[x][y]
                    que.append([nx, ny])

t = int(input())
for tc in range(1,t+1):
    N = int(input())
    Map = [list(map(int,(input()))) for _ in range(N)]
    inf = float('inf')
    dist = [[inf] * N for _ in range(N)]
    dist[0][0] = 0

    deque_()
    res = dist[N-1][N-1]

    print("#{} {}".format(tc,res))