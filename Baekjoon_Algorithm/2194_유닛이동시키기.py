from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs(start):
    q = deque()
    x, y, cnt = start[0], start[1], 0
    q.append((x,y,cnt))
    visit[x][y] = True
    while q:
        x, y, cnt = q.popleft()
        if [x,y] == end:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0< nx <= N-A+1 and 0< ny <= M-B+1:
                flag = True
                if visit[nx][ny] == 0:
                    for k in range(nx, nx + A):
                        for p in range(ny, ny + B):
                            if visit[k][p] != -1:
                                continue
                            else:
                                flag = False
                                break
                    if flag:
                        q.append((nx, ny, cnt+1))
                        visit[nx][ny] = 1
    return -1

N, M, A, B, K = map(int,input().split())
visit = [[0]*(M+1) for _ in range(N+1)]
for _ in range(K):
    x,y = map(int,input().split())
    visit[x][y] = -1
start = list(map(int,input().split()))
end = list(map(int,input().split()))

print(bfs(start))
