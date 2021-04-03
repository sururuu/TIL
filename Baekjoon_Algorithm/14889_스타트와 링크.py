from itertools import combinations
n = int(input())
link = [list(map(int,input().split())) for _ in range(n)]
m = n//2
num = [_ for _ in range(n)]
case = list(combinations(num,m))
res = 1000000000
for target in case:
    new = []
    for i in range(n):
        if num[i] not in target:
            new.append(num[i])
    target = list(target)
    s1 = 0
    s2 = 0
    target_case = list(combinations(target,2))
    new_case = list(combinations(new,2))
    for t in target_case:
        x,y = t
        s1 += link[x][y]
        s1 += link[y][x]
    for t in new_case:
        x,y = t
        s2 += link[x][y]
        s2 += link[y][x]
    res = min(res,abs(s1-s2))
print(res)