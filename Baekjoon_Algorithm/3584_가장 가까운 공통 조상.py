t = int(input())
for tc in range(t):
    n = int(input())
    parent = [0 for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int,input().split())
        parent[b] = a
    a, b = map(int,input().split())
    a_parent = [a]
    b_parent = [b]
    while parent[a]:
        a_parent.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_parent.append(parent[b])
        b = parent[b]
    for i in range(len(a_parent)):
        if a_parent[i] in b_parent:
            print(a_parent[i])
            break
