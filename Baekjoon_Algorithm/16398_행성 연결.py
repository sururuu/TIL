import sys
def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return parent[x]
def find_union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
input = sys.stdin.readline
n = int(input())
parent = [i for i in range(n+1)]
graph = []
arr = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        x, y, cost = i, j, arr[i][j]
        graph.append((cost,x,y))
graph.sort()
res = 0
for target in graph:
    cost, x, y = target
    if find_parent(x) != find_parent(y):
        find_union(x,y)
        res += cost
print(res)