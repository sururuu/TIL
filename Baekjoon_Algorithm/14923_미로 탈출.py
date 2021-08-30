from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x,y):
    q = deque()
    q.append([x, y, 1])
    while q:
        x, y, magic = q.popleft()
        if x == Ex and y == Ey:
            return visit[x][y][magic]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny <m:
                # 벽인경우 magic을 사용
                if arr[nx][ny] and magic == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append([nx, ny, 0])
                # 벽이 아니고 방문하지 않은 곳 가는 경우
                elif not arr[nx][ny] and not visit[nx][ny][magic]:
                    visit[nx][ny][magic] = visit[x][y][magic] + 1
                    q.append([nx, ny, magic])
    return -1

n, m = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
Hx, Hy , Ex, Ey = Hx - 1, Hy - 1, Ex - 1, Ey - 1
arr = [list(map(int,input().split())) for _ in range(n)]
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
res = bfs(Hx, Hy)
print(res)
