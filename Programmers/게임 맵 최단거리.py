from collections import deque
def solution(maps):
    answer = 0
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    q = deque()
    q.append((0,0,1))
    garo = len(maps[0])
    cero = len(maps)
    visit = [[False]*garo for _ in range(cero)]
    while q:
        x,y,distance = q.popleft()
        if x == cero-1 and y == garo-1:
            return distance
        visit[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<cero and 0<=ny<garo:
                if maps[nx][ny] == 1 and visit[nx][ny] == False:
                    q.append((nx,ny,distance+1))
                    visit[nx][ny] = True
    return -1