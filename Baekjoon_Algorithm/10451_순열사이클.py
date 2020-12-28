def bfs(idx):
    visit[idx] = True
    q = []
    q.append(idx)
    while q:
        id = q.pop(0)
        if visit[case[id - 1][1]] == False:
            visit[case[id - 1][1]] = True
            q.append(case[id - 1][1])

t = int(input())
for tc in range(t):
    n = int(input())
    input_list = list(map(int,input().split()))
    case = []
    for i in range(n):
        case.append((i+1,input_list[i]))
    visit = [False]*(n+1)
    cnt= 0
    for i in range(n):
        if visit[i+1] == False:
            cnt += 1
            bfs(case[i][1])
    print(cnt)