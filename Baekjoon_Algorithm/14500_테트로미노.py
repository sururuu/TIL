n,m = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(n)]
res = 0
case = [[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)],
        [(0,1),(0,2),(1,2)],[(0,1),(0,2),(1,0)],
        [(1,0),(2,0),(2,1)],[(1,0),(2,0),(2,-1)],
        [(1,0),(1,1),(1,2)],[(0,1),(0,2),(-1,2)],
        [(0,1),(1,0),(2,0)],[(0,1),(1,1),(2,1)],
        [(1,0),(1,1),(2,1)],[(0,1),(-1,1),(-1,2)],
        [(1,0),(0,1),(-1,1)],[(0,1),(1,1),(1,2)],
        [(0,1),(0,2),(1,1)],[(1,0),(2,0),(1,1)],
        [(1,-1),(1,0),(1,1)],[(-1,1),(0,1),(1,1)],
        [(0,1),(1,1),(1,0)]]
for i in range(n):
    for j in range(m):
        x,y = i,j
        for target in case:
            s = table[x][y]
            for k in range(3):
                nx = x + target[k][0]
                ny = y + target[k][1]
                if 0<=nx<n and 0<=ny<m:
                    s += table[nx][ny]
                else:
                    s = table[x][y]
                    break
            if s > table[x][y]:
                res = max(res,s)
print(res)