from _collections import deque
n = int(input())
m = int(input())
person = dict()
for i in range(m):
    a,b  = map(int,input().split())
    if a not in person:
        person[a] = list()
    if b not in person:
        person[b] = list()
    person[a].append(b)
    person[b].append(a)

res = set()
for key in person[1]:
    res.add(key)
    for item in person[key]:
        res.add(item)
        
print(len(res)-1)