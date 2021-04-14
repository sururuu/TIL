dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solution(x,y,depth,stack):
    global answer
    visit[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not visit[nx][ny]:
            if depth >= NUM:
                answer += stack * percent[i]
            else:
                solution(nx,ny,depth+1,stack * percent[i])
    visit[x][y] = False


NUM, E, W, S, N = map(int,input().split())
percent = [E/100, W/100, S/100, N/100]
visit = [[False]*29 for _ in range(29)]
answer = 0
solution(14,14,1,1)
print(answer)