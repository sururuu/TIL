import sys
input = sys.stdin.readline
n, k = map(int, input().split())
INF = sys.maxsize
visit = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    s, e = map(int, input().split())
    visit[s][e] = max(visit[s][e], 1)
for p in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if visit[i][p] == 1 and visit[p][j] == 1:
                visit[i][j] = 1
s = int(input())
for _ in range(s):
    start, end = map(int, input().split())
    if visit[start][end]:
        print(-1)
    else:
        if visit[end][start]:
            print(1)
        else:
            print(0)
