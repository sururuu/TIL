from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    q = deque()
    q.append([x, y])
    arr[x][y] = '.'
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == '#':
                q.append([nx, ny])
                arr[nx][ny] = '.'
t = int(input())
for tc in range(t):
    h, w = map(int,input().split())
    arr = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#':
                cnt += 1
                bfs(i, j)
    print(cnt)