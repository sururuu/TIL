import sys
sys.setrecursionlimit(10 ** 4)
m,n = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]
def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            X = dx[i] + x
            Y = dy[i] + y
            if 0 <= X < m and 0 <= Y < n:
                if Map[X][Y] < Map[x][y]:
                    dp[x][y] += dfs(X,Y)
    return dp[x][y]
print(dfs(0,0))