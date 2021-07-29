from itertools import combinations
n, m = map(int,input().split())
h = list(map(int, input().split()))
def prime():
    s = sum(h)
    visit = [True] * (s+1)
    for i in range(2, s+1):
        for j in range(i+i,s+1,i):
            visit[j] = False
    return visit
visit = prime()
case = list(combinations(h,m))
res = []
for target in case:
    s = sum(target)
    if visit[s]:
        res.append(s)
if res:
    res = sorted(list(set(res)))
    print(*res)
else:
    print(-1)