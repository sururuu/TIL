def sol1():
    res = 0
    for i in range(n):
        case = list(set(sushi[i:i+k]))
        cnt = len(case)
        if c not in case:
            cnt += 1
        if cnt == k+1:
            res = k + 1
            break
        res = max(res, cnt)
    return res
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
plus = sushi[:k-1]
sushi += plus
print(sol1())
