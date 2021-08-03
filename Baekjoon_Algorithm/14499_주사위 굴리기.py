def move(arr, dir):
    # 동 서 북 남
    if dir == 1:
        arr = [0, arr[3], arr[2], arr[6], arr[1], arr[5], arr[4]]
    elif dir == 2:
        arr = [0, arr[4], arr[2], arr[1], arr[6], arr[5], arr[3]]
    elif dir == 3:
        arr = [0, arr[2], arr[6], arr[3], arr[4], arr[1], arr[5]]
    elif dir == 4:
        arr = [0, arr[5], arr[1], arr[3], arr[4], arr[6], arr[2]]
    return arr

n, m, x, y, k = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
case = list(map(int,input().split()))
dice = [0] * 7
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for i in range(k):
    nx = x + dx[case[i]]
    ny = y + dy[case[i]]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        dice = move(dice, case[i])
        if Map[x][y] == 0:
            Map[x][y] = dice[6]
        else:
            dice[6] = Map[x][y]
            Map[x][y] = 0
        print(dice[1])
