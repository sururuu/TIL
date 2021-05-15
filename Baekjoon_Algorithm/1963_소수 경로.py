from collections import deque
def isPrime():
    visit = [1]*10001
    for i in range(2,int(10001**0.5)+1):
        for j in range(i+i,10001,i):
            visit[j] = 0
    return visit
def bfs(n,m):
    q = deque()
    q.append([n,0])
    visited = [0]*10001
    visited[n] = 1
    while q:
        now,cnt = q.popleft()
        strNow = str(now)
        if now == m:
            return cnt
        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i+1:])
                if temp >= 1000 and visited[temp] == 0 and prime[temp] == 1:
                    visited[temp] = 1
                    q.append([temp,cnt+1])
    return 'Impossible'
t = int(input())
prime = isPrime()
for tc in range(t):
    n,m = map(int,input().split())
    res = bfs(n,m)
    print(res)


