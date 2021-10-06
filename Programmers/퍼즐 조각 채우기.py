from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def find(table,visit,x1,y1):
    flag = 1
    if table[x1][y1] == 0:
        flag = 0
    q = deque()
    q.append([x1,y1])
    visit[x1][y1] = True
    x_min, x_max, y_min, y_max, cnt = x1, x1, y1, y1, 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(table) and 0 <= ny < len(table[0]):
                if table[nx][ny] == flag and not visit[nx][ny]:
                    q.append([nx,ny])
                    visit[nx][ny] = True
                    x_min = min(x_min, nx)
                    x_max = max(x_max, nx)
                    y_min = min(y_min, ny)
                    y_max = max(y_max, ny)
                    cnt += 1
    block = [x_min,y_min,x_max,y_max,cnt]
    return block

def solution(game_board, table):
    answer = 0
    case = []
    visit = [[False]*len(table[0]) for _ in range(len(table))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1 and not visit[i][j]:
                case.append(find(table,visit,i,j))
    visit = [[False]*len(table[0]) for _ in range(len(table))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            if game_board[i][j] == 0 and not visit[i][j]:
                empty = find(game_board,visit,i,j)
                x1, y1, x2, y2, cnt1 = empty
                # 빈공간 a*b 2차원 배열로 만들기
                empty_nemo = [[0]*(y2+1-y1) for _ in range(x2+1-x1)]
                for l in range(x1, x2+1):
                    for m in range(y1, y2+1):
                        if game_board[l][m] == 0:
                            empty_nemo[l-x1][m-y1] = 1
                for idx,target in enumerate(case):
                    x1, y1, x2, y2, cnt2 = target
                    if cnt1 == cnt2:
                        # 퍼즐 조각 a*b 2차원 배열로 만들기
                        puzzle = [[0]*(y2+1-y1) for _ in range(x2+1-x1)]
                        for l in range(x1, x2+1):
                            for m in range(y1, y2+1):
                                if table[l][m] == 1:
                                    puzzle[l-x1][m-y1] = 1
                        flag = False
                        if empty_nemo == puzzle:
                            flag = True
                        else:
                            # 비어있는 공간 회전
                            for _ in range(3):
                                empty_nemo = list(map(list, zip(*empty_nemo[::-1])))
                                print(empty_nemo)
                                if empty_nemo == puzzle:
                                    flag = True
                        if flag:
                            answer += cnt1
                            del case[idx]
                            break

    return answer