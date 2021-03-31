import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
q = deque()
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
rx,ry,bx,by = [0]*4
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j
q.append((rx,ry,bx,by,1))
visit[rx][ry][bx][by] = True

def move(x,y,dir):
    # 다음칸이 벽이거나 구멍일때까지 움직이기
    count = 0
    dx,dy = dir
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x,y,count
# 상 하 좌 우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution():
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt > 10:
            cnt = -1
            return cnt
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,direction[i])
            nbx,nby,bcnt = move(bx,by,direction[i])
            # 파란구슬이 구멍이 들어가면 실패
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return cnt
            # 겹치는 경우 한칸 뒤로 가기
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= direction[i][0]
                    nry -= direction[i][1]
                else:
                    nbx -= direction[i][0]
                    nby -= direction[i][1]
            # 방문처리
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                q.append((nrx,nry,nbx,nby,cnt+1))

    return -1


print(solution())
