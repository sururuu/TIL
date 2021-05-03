def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n = int(input())
m = int(input())
arr = [[0]*(n+1)]
for i in range(n):
    new = [0] + list(map(int,input().split()))
    arr.append(new)
parent = [i for i in range(n+1)]
for i in range(1,n+1):
    for j in range(i,n+1):
        if arr[i][j]:
            union(i,j)
case = list(map(int,input().split()))
for i in range(m-1):
    a,b = case[i:i+2]
    if find(a) == find(b):
        continue
    else:
        print('NO')
        exit()
print('YES')