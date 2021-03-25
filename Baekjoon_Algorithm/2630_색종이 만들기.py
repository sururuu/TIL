def divide(x,y,size):
    target = paper[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if target != paper[i][j]:
                m = size//2
                # 왼쪽 위
                divide(x,y,m)
                # 오른쪽 위
                divide(x+m,y,m)
                # 왼쪽 아래
                divide(x,y+m,m)
                # 오른쪽 아래
                divide(x+m,y+m,m)
                return
    res[target] += 1
n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
res= [0,0]
divide(0,0,len(paper))
for sol in res:
    print(sol)