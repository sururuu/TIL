from itertools import combinations
n = int(input())
case = [list(map(int,input().split())) for _ in range(n)]
arr = [_ for _ in range(n)]
res = 1000000000
for count in range(1,n+1):
    combi = list(combinations(arr,count))
    for target in combi:
        a,b = 1,0
        for k in range(len(target)):
            idx = target[k]
            a *= case[idx][0]
            b += case[idx][1]
        res = min(res,abs(a-b))
print(res)