from collections import deque
import copy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 빙산 높이 줄이기
def minus(arr):
    new = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] == 0:
                            cnt += 1
                new[i][j] = arr[i][j] - cnt
                if new[i][j] < 0:
                    new[i][j] = 0
    return new
# 빙산 개수 구하기
def ice_cnt(x,y):
    q = deque()
    q.append((x,y))
    ice_copy[x][y] = 0
    while q:
        x,y = q.popleft()
        visit[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == False:
                if ice_copy[nx][ny] != 0:
                    ice_copy[nx][ny] = 0
                    q.append((nx,ny))

n,m = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(n)]
res = 0
while True:
    cnt = 0
    visit = [[False]*m for _ in range(n)]
    ice_copy = copy.deepcopy(ice)
    for i in range(n):
        for j in range(m):
            if ice_copy[i][j] != 0 and visit[i][j] == False:
                ice_cnt(i, j)
                cnt += 1
    if cnt > 1:
        break
    if cnt == 0:
        res = 0
        break
    ice = minus(ice)
    res += 1
print(res)