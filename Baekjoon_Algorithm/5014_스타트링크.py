from collections import deque
def bfs(idx,f,G,U,D):
    q = deque()
    q.append(idx)
    visit = [0] * (f+1)
    visit[idx] = 1
    while q:
        next = q.popleft()
        if next == G:
            print(visit[G] - 1)
            return
        up = next + U
        down = next - D
        if up <= f and visit[up] == 0:
            q.append(up)
            visit[up] = visit[next] + 1
        if down > 0 and visit[down] == 0:
            q.append(down)
            visit[down] = visit[next] + 1
    print('use the stairs')
    return

F,S,G,U,D = map(int,input().split())
bfs(S,F,G,U,D)