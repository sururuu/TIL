from collections import deque
from math import log2
N = int(input())
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visit = [False] * (N+1)
parent = [0] * (N+1)
depth = [0] * (N+1)
q = deque()
q.append(1)
while q:
    idx = q.popleft()
    visit[idx] = True
    for i in tree[idx]:
        if not visit[i]:
            q.append(i)
            parent[i] = idx
            depth[i] = depth[idx] + 1
logN = int(log2(N) + 1)
dp = [[0]*logN for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = parent[i]
for i in range(1, logN):
    for j in range(1, N+1):
        dp[j][i] = dp[dp[j][i-1]][i-1]
M = int(input())
for i in range(M):
    a, b = map(int,input().split())
    # 깊이가 같아지게 하기
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 부모가 같아지게 하기
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)