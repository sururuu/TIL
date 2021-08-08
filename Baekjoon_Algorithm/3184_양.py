from _collections import deque
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
o_cnt, v_cnt = 0, 0
visit = [[False] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    global w,s
    visit[x][y] = True
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        if arr[x][y] == 'v':
            w += 1
        elif arr[x][y] == 'o':
            s += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] != '#' and not visit[nx][ny]:
                    q.append([nx,ny])
                    visit[nx][ny] = True
for i in range(r):
    for j in range(c):
        if arr[i][j] != '#' and not visit[i][j]:
            w, s = 0, 0
            bfs(i,j)
            if w >= s:
                s = 0
            else:
                w = 0
            v_cnt += w
            o_cnt += s
print(o_cnt, v_cnt)
