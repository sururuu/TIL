
def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    # print(v,end='')
    while q :
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w]  = visited[v] + 1
                # print(w,end='')
t = int(input())
for tc in range(1,t+1):
    N,M=map(int,input().split())
    G = [[] for _ in range(N+1)]
    # 1~N 각각의 인접하는 수는 해당 인덱스에 저장
    for i in range(M):
        ind,val = map(int,input().split())
        G[ind].append(val)
        G[val].append(ind)

    visited = [0] *(N+1)
    bfs(1)
    cnt = 0
    for i in range(N+1):
        if visited[i] == 2 or visited[i] == 3:
            cnt += 1

    print("#{} {}".format(tc,cnt))