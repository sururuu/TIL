from collections import deque
a,b,n,m = map(int,input().split())
q = deque()
q.append(n)
visit = [0]*100001
flag = True
while q:
    if not flag:
        break
    node = q.popleft()
    for num in [node-1,node+1,node+a,node+b,node-a,node-b,node*a,node*b]:
        if (0 <= num <= 100000) and not visit[num]:
            q.append(num)
            visit[num] = visit[node] + 1
            if n == m:
                flag = False
                break
print(visit[m])