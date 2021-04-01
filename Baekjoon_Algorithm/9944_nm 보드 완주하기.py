import sys
sys.setrecursionlimit(1000001)
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x,y,cnt):
    global res,count
    # res 보다 현재 돌고 있는 cnt 가 더 크면 그만하기
    if res <= cnt:
        return

    case = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0<=nx<n and 0<=ny<m and board[nx][ny] == '.':
            case.append((nx,ny))
            board[nx][ny] = '*'
            count -= 1
            nx += dx[i]
            ny += dy[i]
        if case:
            # nx,ny 는 범위를 벗어난 상태이므로 - 해주기
            dfs(nx-dx[i],ny-dy[i],cnt+1)
        # visit 처리
        for i in range(len(case)):
            cx,cy = case.pop()
            board[cx][cy] = '.'
            count += 1
    if count == 0:
        res = min(res,cnt)
idx = 1
while True:
    try:
        n,m = map(int,input().split())
        count = 0
        res = 1000001
        board = [list(input()) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    count += 1
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    # visit 처리
                    board[i][j] = '*'
                    count -= 1
                    dfs(i,j,0)
                    # visit 초기화
                    board[i][j] = '.'
                    count += 1
        if res == 1000001:
            res = -1

        print('Case {}: {}'.format(idx,res))
        idx += 1
    except EOFError:
        break
