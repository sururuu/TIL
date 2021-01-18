def solution(board):
    answer = 1
    h = len(board)
    w = len(board[0])
    for y in range(1,h):
        for x in range(1,w):
            # 위, 왼쪽, 대각선 체크
            m = min(board[y-1][x-1],board[y-1][x],board[y][x-1])
            if m == 0 or board[y][x] == 0:
                pass
            else:
                board[y][x] = max(m+1,board[y][x])
    m = max(map(max,board))
    return m**2