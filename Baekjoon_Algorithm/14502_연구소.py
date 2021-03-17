from collections import deque
from itertools import combinations
import copy
n,m = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 0. 바이러스 퍼트린후 안전영역 크기 반환
def birus(birus_list,map):
    q = deque(birus_list)
    arr = copy.deepcopy(map)
    while q:
        x,y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<=X<n and 0<=Y<m:
                if arr[x][y] == 2 and arr[X][Y] == 0:
                    arr[X][Y] = 2
                    q.append((X,Y))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    return cnt
# 1.  0인 곳을 저장하기, 바이러스 저장
change = []
birus_list= []
for i in range(n):
    for j in range(m):
        if Map[i][j] == 2:
            birus_list.append([i,j])
        if Map[i][j] == 0:
            change.append([i,j])

# 2. 1의 저장된 곳 중 3개씩 조합 구하기
change_combi = list(combinations(change,3))
# 3. 2의 조합을 돌면서 0의 갯수 구하기
res = 0

for l in range(len(change_combi)):
    cnt = 0
    for k in range(3):
        x = change_combi[l][k][0]
        y = change_combi[l][k][1]
        Map[x][y] = 1
    cnt = birus(birus_list,Map)

    for k in range(3):
        x = change_combi[l][k][0]
        y = change_combi[l][k][1]
        Map[x][y] = 0

    res = max(res,cnt)

print(res)
