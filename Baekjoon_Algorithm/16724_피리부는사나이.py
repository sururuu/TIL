n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
cnt = 0
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def dfs(x, y, q):
    global cnt
    if arr[x][y] == 'U':
        d = dirs[0]
    elif arr[x][y] == 'D':
        d = dirs[1]
    elif arr[x][y] == 'L':
        d = dirs[2]
    elif arr[x][y] == 'R':
        d = dirs[3]
    visit[x][y] = True
    nx = x + d[0]
    ny = y + d[1]
    if visit[nx][ny]:
        if (nx, ny) in q:
            cnt += 1
        return
    else:
        q.append((x,y))
        dfs(x + d[0], y + d[1], q)

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            dfs(i, j, [])
print(cnt)

