from _collections import deque
num = int(input())
visit = [False]*(num+1)
def bfs(x):
    q = deque()
    q.append((x,[x]))
    while q:
        x, arr = q.popleft()
        visit[x] = True
        if x == 1:
            return arr
        if x % 3 == 0 and not visit[x//3]:
            q.append((x//3,arr+[x//3]))
        if x % 2 == 0 and not visit[x//2]:
            q.append((x//2,arr+[x//2]))
        if not visit[x-1]:
            q.append((x-1,arr+[x-1]))

res = bfs(num)
print(len(res)-1)
print(' '.join(map(str,res)))