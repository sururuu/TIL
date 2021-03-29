from collections import deque
def solution():
    cnt = 0
    x,y = 1,1
    # 뱀
    wall[1][1] = 2
    tail = deque()
    tail.append((x,y))
    case = [[0,1],[0,-1],[-1,0],[1,0]]
    # 초기 설정 오른쪽
    dx,dy = case[0]
    # 0 => 2,3
    # 1 => 3,2
    # 2 => 1,0
    # 3 => 0,1
    count, d = direction.popleft()
    while True:
        cnt += 1
        x += dx
        y += dy
        if 0 < x <= n and 0 < y <= n:
            # 뱀과 마주치면
            if (x, y) in tail:
                return cnt
            # 사과가 있다면
            if wall[x][y] == 1:
                wall[x][y] = 2
                tail.append((x, y))
            # 사과 가 없다면
            elif wall[x][y] == 0:
                fx, fy = tail.popleft()
                wall[fx][fy] = 0
                wall[x][y] = 2
                tail.append((x, y))
            else:
                return cnt
        else:
            return cnt
        if cnt == int(count):
            # 방향 전환
            if dx == case[0][0] and dy == case[0][1]:
                if d == 'L':
                    dx, dy = case[2]
                elif d == 'D':
                    dx, dy = case[3]
            elif dx == case[1][0] and dy == case[1][1]:
                if d == 'L':
                    dx, dy = case[3]
                elif d == 'D':
                    dx, dy = case[2]
            elif dx == case[2][0] and dy == case[2][1]:
                if d == 'L':
                    dx, dy = case[1]
                elif d == 'D':
                    dx, dy = case[0]
            elif dx == case[3][0] and dy == case[3][1]:
                if d == 'L':
                    dx, dy = case[0]
                elif d == 'D':
                    dx, dy = case[1]
            if direction:
                count, d = direction.popleft()

    return cnt

n = int(input())
k = int(input())
wall = [[0]*(n+1) for _ in range(n+1)]
for i in range(k):
    x,y = map(int,input().split())
    wall[x][y] = 1
L = int(input())
direction = deque([list(input().split()) for _ in range(L)])
res = solution()
print(res)