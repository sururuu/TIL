import sys
n = int(input())
m = int(input())
input = sys.stdin.readline
INF = sys.maxsize
board = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    board[i][i] = 0
for _ in range(m):
    start, end, cost = map(int, input().split())
    if board[start][end] > cost:
        board[start][end] = cost

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                board[i][j] = 0
            else:
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == INF:
            print(0, end=' ')
        else:
            print(board[i][j], end=' ')
    print()