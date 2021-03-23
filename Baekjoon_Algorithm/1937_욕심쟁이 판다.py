import sys
sys.setrecursionlimit(10**6)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
def dfs(i,j):
    if res[i][j]:
        return res[i][j]
    res[i][j] = 1
    for k in range(4):
        nx,ny = i+dx[k], j+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if forest[i][j] < forest[nx][ny]:
                res[i][j] = max(res[i][j],dfs(nx,ny)+1)
    return res[i][j]
n = int(input())
forest = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
res = [[0]*n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))
print(ans)

# PyPy3 vs Python3
# 메모리 사용량 PyPy3 > Python3
# 시간 PyPy3 < Python3
