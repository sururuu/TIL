import sys
from collections import deque

dx = [1,1,1,0,0,-1,-1,-1]
dy = [-1,0,1,-1,1,-1,0,1]
def island(a,b):
    q = deque()
    q.append((a,b))
    while q:
        x,y = q.popleft()
        for k in range(8):
            X = x + dx[k]
            Y = y + dy[k]
            if 0<=X<h and 0<=Y<w:
                if  Map[X][Y]==1:
                    Map[X][Y] = 0
                    q.append((X,Y))


# 마지막 인풋이 (0,0) 
# h+w=0 이 될떄가지 인풋 받기
input = sys.stdin.readline
w,h = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(h)]
while h+w!=0:
    cnt = 0
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                Map[i][j] = 0
                cnt += 1
                island(i, j)

    print(cnt)
    w, h = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(h)]


