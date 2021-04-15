def solution(dirs):
    answer = 0
    board = [[[] for i in range(11)] for j in range(11)]
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    change = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
    x, y = 5, 5
    direction = ['U', 'D', 'L', 'R']
    for target in dirs:
        for i in range(4):
            if direction[i] == target:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 > nx or 0 > ny or nx > 10 or ny > 10:
                    continue
                if target not in board[x][y]:
                    answer += 1
                    board[nx][ny].append(change[target])
                    board[x][y].append(target)
                x = nx
                y = ny

    return answer
