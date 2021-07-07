n, m, k = map(int,input().split())
money = [0] + list(map(int,input().split()))
parent = [i for i in range(n+1)]
def find_parent(num):
    if parent[num] != num:
        return parent[num]
    return parent[num]
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if money[a] < money[b]:
        parent[b] = a
        for i in range(1,n+1):
            if parent[i] == b:
                parent[i] = a
        money[b] = money[a]
    else:
        parent[a] = b
        for i in range(1,n+1):
            if parent[i] == a:
                parent[i] = b
        money[a] = money[b]

for i in range(m):
    a, b = map(int,input().split())
    union(a, b)
parent = set(parent[1:])
s = 0
for cost in parent:
    s += money[cost]
if s > k:
    print("Oh no")
else:
    print(s)

#
# 5 4 100
# 1 1 1 1 1
# 1 5
# 2 4
# 4 3
# 5 4