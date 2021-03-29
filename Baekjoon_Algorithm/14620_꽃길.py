from itertools import combinations
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def solution():
    res = 100000000
    for target in case:
        cnt = 0
        visit = [[False] * n for _ in range(n)]
        flag = True
        for i in range(3):
            x, y = target[i]
            if visit[x][y] == False:
                visit[x][y] = True
                cnt += land[x][y]
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == False:
                        visit[nx][ny] = True
                        cnt += land[nx][ny]
                    else:
                        flag = False
                        break
            else:
                flag = False
        if flag:
            res = min(res, cnt)
    return res
n = int(input())
land = [list(map(int,input().split())) for _ in range(n)]
case = []
for i in range(1,n-1):
    for j in range(1,n-1):
        case.append((i,j))
case = list(combinations(case,3))
result = solution()

print(result)