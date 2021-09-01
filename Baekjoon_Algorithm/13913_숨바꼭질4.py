from collections import deque
def solution(x):
    q = deque()
    q.append(x)
    while q:
        idx = q.popleft()
        if idx == k:
            return
        for i in [idx-1, idx+1, idx*2]:
            if 0 <= i <= 100000 and prev[i] == -1:
                q.append(i)
                prev[i] = idx
n, k = map(int, input().split())
prev = [-1]*100001
solution(n)
res = [k]
while k != n:
    k = prev[k]
    res.append(k)

res.reverse()
print(len(res)-1)
print(*res)