r,c = map(int,input().split())
board = [list(input()) for _ in range(r)]
def dfs():
    global answer
    q = set([(0,0,board[0][0])])
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    while q:
        x,y,ans = q.pop()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0<=X<r and 0<=Y<c:
                # ans 안에 없는 알파벳 찾기
                if board[X][Y] not in ans:
                    q.add((X,Y,ans+board[X][Y]))
                    answer = (max(answer,len(ans)+1))

answer = 1
dfs()
print(answer)
