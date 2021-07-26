import sys
input = sys.stdin.readline
m, n = map(int, input().split())
k = int(input())
dp_j = [[0]*(n+1) for _ in range(m+1)]
dp_o = [[0]*(n+1) for _ in range(m+1)]
dp_i = [[0]*(n+1) for _ in range(m+1)]
for i in range(m):
    arr = list(input())
    for j in range(n):
        if arr[j] == 'J':
            dp_j[i+1][j+1] = (dp_j[i+1][j]+dp_j[i][j+1]-dp_j[i][j]) + 1
            dp_o[i+1][j+1] = (dp_o[i+1][j]+dp_o[i][j+1]-dp_o[i][j])
            dp_i[i+1][j+1] = (dp_i[i+1][j]+dp_i[i][j+1]-dp_i[i][j])
        elif arr[j] == 'O':
            dp_j[i+1][j+1] = (dp_j[i+1][j]+dp_j[i][j+1]-dp_j[i][j])
            dp_o[i+1][j+1] = (dp_o[i+1][j]+dp_o[i][j+1]-dp_o[i][j]) + 1
            dp_i[i+1][j+1] = (dp_i[i+1][j]+dp_i[i][j+1]-dp_i[i][j])
        elif arr[j] == 'I':
            dp_j[i+1][j+1] = (dp_j[i+1][j]+dp_j[i][j+1]-dp_j[i][j])
            dp_o[i+1][j+1] = (dp_o[i+1][j]+dp_o[i][j+1]-dp_o[i][j])
            dp_i[i+1][j+1] = (dp_i[i+1][j]+dp_i[i][j+1]-dp_i[i][j]) + 1
for target in range(k):
    a, b, c, d = map(int,input().split())
    cnt_j, cnt_o, cnt_i = 0, 0, 0
    cnt_j = dp_j[c][d] - (dp_j[a-1][d] + dp_j[c][b-1] - dp_j[a-1][b-1])
    cnt_o = dp_o[c][d] - (dp_o[a-1][d] + dp_o[c][b-1] - dp_o[a-1][b-1])
    cnt_i = dp_i[c][d] - (dp_i[a-1][d] + dp_i[c][b-1] - dp_i[a-1][b-1])

    print(cnt_j,cnt_o,cnt_i)
