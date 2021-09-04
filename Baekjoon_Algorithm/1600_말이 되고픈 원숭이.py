import sys
from collections import deque
input = sys.stdin.readline
K = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
dx2 = [-2, -2, -1, -1, 1, 1, 2, 2]
dy2 = [-1, 1, -2, 2, -2, 2, -1, 1]
visit = [[[0]*(K+1) for _ in range(w)] for _ in range(h)]
def bfs(x,y):
    q = deque()
    q.append([x, y, 0])
    visit[x][y][0] = 1
    while q:
        x, y, cnt = q.popleft()
        if [x, y] == [h-1, w-1]:
            return visit[x][y][cnt] - 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and not arr[nx][ny] and not visit[nx][ny][cnt]:
                q.append([nx, ny, cnt])
                visit[nx][ny][cnt] = visit[x][y][cnt] + 1
        if cnt < K:
            for k in range(8):
                nx = x + dx2[k]
                ny = y + dy2[k]
                if 0 <= nx < h and 0 <= ny < w and not arr[nx][ny] and not visit[nx][ny][cnt]:
                    q.append([nx, ny, cnt + 1])
                    visit[nx][ny][cnt+1] = visit[x][y][cnt] + 1

    return -1
print(bfs(0, 0))