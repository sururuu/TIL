from collections import deque

def bfs():
    q=deque()
    q.append(n)
    while q:
        position = q.popleft()

        if position == k:
            return visited[position]

        for case in (position+1,position-1,2*position):
            if (0<=case<100001):
                if visited[case] == 0:
                    visited[case] = visited[position] + 1
                    q.append(case)

n,k = map(int,input().split())
visited = [0]*100001

print(bfs())
