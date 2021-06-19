from collections import deque
n = int(input())
a = list(map(int,input().split()))
f = [0]*n
dic = {}
for i in range(n):
    if a[i] not in dic:
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1
for i in range(n):
    f[i] = dic[a[i]]
stack = deque()
stack.append(0)
idx = 0
res = [-1]*n
for i in range(1,n):
    while stack and f[a[stack[-1]]] < f[a[i]]:
        idx = stack.pop()
        res[idx] = a[i]
    stack.append(i)
print(*res)