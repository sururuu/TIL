from collections import deque
for tc in range(10):
    n = int(input())
    miro = [list(map(int,input())) for _ in range(16)]
    # 시작 점 찾기
    start = 0
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                start = (i,j)
                break

    def solution(start):
        q = deque()
        q.append(start)
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        while q:
            x,y = q.popleft()
            for i in range(4):
                X = dx[i] + x
                Y = dy[i] + y
                if 0<=X <16 and 0<=Y <16 :
                    if miro[X][Y] == 0:
                        q.append((X,Y))
                        miro[X][Y] = 1
                    if miro[X][Y] == 3:
                        return 1
        return 0

    print("#{} {}".format(n,solution(start)))