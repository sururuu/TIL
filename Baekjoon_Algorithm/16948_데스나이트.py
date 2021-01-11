from _collections import deque
n = int(input())
r1,c1,r2,c2 = map(int,input().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

visit = [[False]*(n+1) for _ in range(n+1)]
q = deque()
q.append((r1,c1,0))
visit[r1][c1] = True
def dfs():
    while q:
        x,y,cnt = q.popleft()
        if x == r2 and y == c2:
            return cnt
        for i in range(6):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<=X<n and 0<=Y<n and visit[X][Y] == False:
                q.append((X,Y,cnt+1))
                visit[X][Y] = True
    return -1
print(dfs())