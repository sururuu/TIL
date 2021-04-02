from _collections import deque
n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
rx,ry,bx,by = [0]*4
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j
q = deque()
dir = ''

q.append((rx,ry,bx,by,1,dir))
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[rx][ry][bx][by] = True
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def move(x,y,dx,dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x,y,count
def solove():
    while q:
        rx,ry,bx,by,cnt,dir = q.popleft()
        if cnt > 10:
            print(-1)
            return
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i])
            nbx,nby,bcnt = move(bx,by,dx[i],dy[i])
            if i == 0:
                ndir = 'U'
            elif i == 1:
                ndir = 'D'
            elif i == 2:
                ndir = 'L'
            else:
                ndir = 'R'
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(cnt)
                print(dir+ndir)
                return
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                q.append((nrx,nry,nbx,nby,cnt+1,dir+ndir))
    print(-1)
    return
solove()