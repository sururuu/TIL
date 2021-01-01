from collections import deque


def solution(n, edge):
    answer = 0
    node = [[] for i in range(n + 1)]
    for i in range(len(edge)):
        a, b = edge[i]
        node[a].append(b)
        node[b].append(a)
    q = deque()
    q.append(1)
    visit = [-1]*(n+1)
    visit[1] = 0
    while q:
        next = q.popleft()
        for i in node[next]:
            if visit[i] == -1:
                visit[i] = visit[next] + 1
                q.append(i)
    answer = (visit.count(max(visit)))
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))