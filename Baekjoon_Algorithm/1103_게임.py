dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(i,j):
    global flag
    # 구멍이거나 범위를 벗어나면 종료
    if not(0<=i<n and 0<=j<m) or board[i][j] == 'H':
        return 0
    if visit[i][j]:
        flag = True
        return -1
    if dp[i][j] != -1:
        return dp[i][j]

    visit[i][j] = True
    for k in range(4):
        nx = i + dx[k]*int(board[i][j])
        ny = j + dy[k]*int(board[i][j])
        dp[i][j] = max(dp[i][j],dfs(nx,ny)+1)
        if flag:
            return -1
    visit[i][j] = False

    return dp[i][j]

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
flag = False
print(dfs(0,0))