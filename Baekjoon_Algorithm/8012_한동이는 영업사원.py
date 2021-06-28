n = int(input())
parent = [0 for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int,input().split())
    if not parent[b]:
        parent[b] = a
    else:
        parent[a] = b
m = int(input())
city = [int(input()) for _ in range(m)]
time = 0
for i in range(m-1):
    a, b = city[i:i+2]
    a_parent = [a]
    b_parent = [b]
    while parent[a]:
        a_parent.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_parent.append(parent[b])
        b = parent[b]
    for j in range(len(a_parent)):
        if a_parent[j] in b_parent:
            time += j
            time += b_parent.index(a_parent[j])
            break
print(time)