from itertools import combinations
N,P,E = map(int,input().split())
arr = []
for i in range(N):
    s,e = map(int,input().split())
    arr.append([s,e])
person = [_ for _ in range(N)]
person = list(combinations(person,P))
res = [0]*N
for target in person:
    s_cnt = 0
    e_cnt = 0
    for i in range(P):
        s_cnt += arr[target[i]][0]
        e_cnt += arr[target[i]][1]
    if s_cnt <= E <= e_cnt:
        for i in range(P):
            res[target[i]] = arr[target[i]][0]
            E -= arr[target[i]][0]
            arr[target[i]] = arr[target[i]][1]-arr[target[i]][0]
        while E:
            for i in range(P):
                if arr[target[i]]:
                    res[target[i]] += 1
                    arr[target[i]] -= 1
                    E -= 1
                if E == 0:
                    break
        print(' '.join(map(str,res)))
        exit()
print(-1)