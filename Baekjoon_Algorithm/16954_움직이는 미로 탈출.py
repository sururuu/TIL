from collections import deque
chess = [list(input()) for _ in range(8)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, -1, 1, -1, 0, 1, 0]
# nx -= 1 => 벽을 내리지 않고 땅을 올려서 높이가 0에 도달하면 return
def bfs(x, y, h):
    q = deque()
    q.append([x, y, h])
    while q:
        x, y, h = q.popleft()
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < 8 and chess[nx][ny] == '.':
                if nx == 0:
                    return 1
                nx -= 1
                if chess[nx][ny] == '.':
                    if nx == 0:
                        return 1
                    q.append([nx, ny, h-1])
    return 0

def bfs2(x, y, h):
    q = deque()
    board = deque(chess)
    q.append([x, y])
    while q:
        visit = [[False]*8 for _ in range(8)]
        for _ in range(len(q)):
            x, y = q.popleft()
            if board[x][y] == '#':
                continue
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == '.' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append([nx, ny])
                    if nx == 0:
                        return 1
        board.pop()
        board.insert(0, ['.']*8)
    return 0
print(bfs2(7, 0, 8))