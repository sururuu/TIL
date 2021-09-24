import sys
def sol(x,y,n):
    visit = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != visit:
                for k in range(3):
                    for l in range(3):
                        sol(x+k*n//3, y+l*n//3, n//3)
                return
    if visit == -1:
        cnt[0] += 1
    elif visit == 0:
        cnt[1] += 1
    else:
        cnt[2] += 1
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0, 0]
sol(0,0,n)
for i in range(3):
    print(cnt[i])
