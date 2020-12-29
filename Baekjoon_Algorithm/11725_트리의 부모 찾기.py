n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    x,y = map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

visit = [False]*(n+1)
q = [1]
res = {}

while q:
    idx = q.pop(0)
    for i in tree[idx]:
        if visit[i] == False:
            res[i] = idx
            visit[i] = True
            q.append(i)

for i in range(2,n+1):
    print(res[i])