from itertools import combinations
n,m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))
ans = 100000000
# 치킨집 m 개 선택
for case in combinations(chicken,m):
    tmp = 0
    for h in home:
        m = 1000000
        for c in case:
            distance = abs(c[0]-h[0]) + abs(c[1]-h[1])
            m = min(m,distance)
        tmp += m
    ans = min(ans,tmp)
print(ans)