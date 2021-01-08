from _collections import deque
n = int(input())
land = [list(map(int,input().split())) for _ in range(n)]

def bfs(i,j,num):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<=X<n and 0<=Y<n:
                if land[X][Y] > num and new[X][Y] == 0:
                    new[X][Y] = 1
                    q.append((X,Y))

answer = 0
minimum = min(map(min,land))
maximum = max(map(max,land))
for num in range(maximum):
    cnt = 0
    new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if land[i][j] > num and new[i][j] == 0:
                new[i][j] = 1
                bfs(i,j,num)
                cnt += 1
    if answer < cnt:
        answer = cnt

print(answer)
