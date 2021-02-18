from _collections import deque
def bfs(Xi,Yi,Xe,Ye,power):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    q = deque()
    q.append((Xi,Yi,power))
    visit[Xi][Yi] = 1
    while q:
        x,y,f = q.popleft()
        if x == Xe and y == Ye:
            return "잘했어!!"
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 < X <= H and 0 < Y <= W :
                if visit[X][Y] == 0:
                    if miro[x][y] >= miro[X][Y] and f > 0:
                        visit[X][Y] = 1
                        q.append((X,Y,f-1))
                    elif miro[x][y] < miro[X][Y] and f > 0:
                        if miro[X][Y] - miro[x][y] <= f:
                            visit[X][Y] = 1
                            q.append((X,Y,f-1))

    return "인성 문제있어??"


t = int(input())
for tc in range(t):
    H,W,O,F,Xi,Yi,Xe,Ye = map(int,input().split())
    miro = [[0]*(W+1) for i in range(H+1)]
    visit = [[0]*(W+1) for i in range(H+1)]
    for i in range(O):
        x,y,num = map(int,input().split())
        miro[x][y] = num
    # print(miro)
    print(bfs(Xi,Yi,Xe,Ye,F))