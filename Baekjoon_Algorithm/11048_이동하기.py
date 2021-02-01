n,m = map(int,input().split())
maze = [[0]*(m+1)]
for i in range(n):
    maze.append([0]+list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,m+1):
        maze[i][j] += max(maze[i-1][j],maze[i-1][j-1],maze[i][j-1])

print(maze[n][m])