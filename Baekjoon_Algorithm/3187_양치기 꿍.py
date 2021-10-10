import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    visit[x][y] = True
    q = deque()
    q.append([x,y])
    k_cnt, v_cnt = 0, 0
    while q:
        x, y = q.popleft()
        if arr[x][y] == 'k':
            k_cnt += 1
        elif arr[x][y] == 'v':
            v_cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visit[nx][ny]:
                if arr[nx][ny] != '#':
                    q.append([nx, ny])
                    visit[nx][ny] = True
    return [k_cnt, v_cnt]
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visit = [[False]*c for _ in range(r)]
k_count, v_count = 0, 0
for i in range(r):
    for j in range(c):
        if not visit[i][j]:
            if arr[i][j] == 'v' or arr[i][j] == 'k':
                k_cnt, v_cnt = bfs(i,j)
                if k_cnt > v_cnt:
                    k_count += k_cnt
                else:
                    v_count += v_cnt
print(k_count,v_count)