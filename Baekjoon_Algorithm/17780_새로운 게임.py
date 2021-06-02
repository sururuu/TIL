dx = [0,0,-1,1]
dy = [1,-1,0,0]

def move(idx):
    x,y,d = ball[idx]
    if idx != chess_map[x][y][0]:
        return 0
    nx = x + dx[d]
    ny = y + dy[d]
    # 가려고 하는 곳이 파란색인 경우, 범위를 벗어나는 경우 방향 바꾸기
    if not 0 <= nx <n or not 0 <= ny < n or chess[nx][ny] == 2:
        if d == 0:
            ball[idx][2] = 1
            d = 1
        elif d == 1:
            ball[idx][2] = 0
            d = 0
        elif d == 2:
            ball[idx][2] = 3
            d = 3
        elif d == 3:
            ball[idx][2] = 2
            d = 2
        nx = x + dx[d]
        ny = y + dy[d]
        # 방향 반대로 했을 때 파란색인 경우 방향만 바꾸기
        if not 0 <= nx < n or not 0 <= ny < n or chess[nx][ny] == 2:
            return 0
    # 가려고 하는 곳이 빨간색인 경우
    # 말의 쌓인 순서 바꾸기
    ball_rev = []
    ball_rev.extend(chess_map[x][y])
    chess_map[x][y] = []
    if chess[nx][ny] == 1:
        ball_rev.reverse()
    # 이동한 칸에 쌓인 말 넣기
    for target in ball_rev:
        chess_map[nx][ny].append(target)
        ball[target][:2] = [nx,ny]
    # 4개 이상 쌓이면 끝
    if len(chess_map[nx][ny]) >=4 :
        return 1
    return 0


n,k = map(int,input().split())
chess = [list(map(int,input().split())) for _ in range(n)]
# 해당 칸에 말을 쌓는 변수
chess_map = [[[] for _ in range(n)] for _ in range(n)]
ball = [0]*k
for i in range(k):
    x,y,d = map(int,input().split())
    chess_map[x-1][y-1].append(i)
    ball[i] = [x-1,y-1,d-1]
cnt = 0
while cnt <= 1000:
    cnt += 1
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            exit()
print(-1)