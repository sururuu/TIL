from collections import deque

def bfs(start):
    x0, y0 = start
    x1, y1 = end
    q = deque()
    q.append((x0, y0))
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    while q:
        x, y = q.popleft()
        if x == x1 and y == y1:
            break
        for i in range(8):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < n and 0 <= Y < n and visit[X][Y] == 0:
                q.append((X, Y))
                visit[X][Y] = visit[x][y] + 1


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    visit = [[0]*n for _ in range(n)]
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    visit[start[0]][start[1]] = 1

    if start == end :
        print(0)
        continue
    bfs(start)
    print(visit[end[0]][end[1]]-1)
